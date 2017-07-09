"""
~~~email-getter.py~~~
Noah Putnam
program to fetch emails from user account inbox 
"""
from __future__ import print_function
import httplib2
import os
import base64
import email


from apiclient import discovery, errors
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

try:
  import argparse
  flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
  flags = None  

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/gmail-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/gmail.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'python_spam_checker'


def get_credentials():
  """Gets valid user credentials from storage.

  If nothing has been stored, or if the stored credentials are invalid,
  the OAuth2 flow is completed to obtain the new credentials.

  Returns:
      Credentials, the obtained credential.
  """
  home_dir = os.path.expanduser('~')
  credential_dir = os.path.join(home_dir, '.credentials')
  if not os.path.exists(credential_dir):
    os.makedirs(credential_dir)
  credential_path = os.path.join(credential_dir,
                               'gmail-python-quickstart.json')

  store = Storage(credential_path)
  credentials = store.get()
  if not credentials or credentials.invalid:
    flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
    flow.user_agent = APPLICATION_NAME
    if flags:
      credentials = tools.run_flow(flow, store, flags)
    else: # Needed only for compatibility with Python 2.6
      credentials = tools.run(flow, store)
    print('Storing credentials to ' + credential_path)
  return credentials


def clean(email_message):
  for part in email_message.walk():
   if part.get_content_type() == "text/plain": # ignore attachments/html
    body = part.get_payload(decode=True).decode('utf-8')
    bad_chars = ['\r', '\n', '>']
    for char in bad_chars:
      body = body.replace(char, '')
    return body
   else:
    continue

def get_emails(n):
  credentials = get_credentials()
  http = credentials.authorize(httplib2.Http())
  service = discovery.build('gmail', 'v1', http=http)

  results = service.users().messages().list(userId='me', includeSpamTrash = True, maxResults=n).execute()
  messages = []
  for message_id in results['messages']:
    body = ''
    message = service.users().messages().get(userId='me', id=message_id['id'], format='raw').execute()
    msg_str = base64.urlsafe_b64decode(message['raw'].encode('ASCII'))
    mime_msg = email.message_from_bytes(msg_str)      
    messages.append(clean(mime_msg))

  return messages
