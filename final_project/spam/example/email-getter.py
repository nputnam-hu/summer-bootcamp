"""
~~~email-getter.py~~~
Noah Putnam
program to fetch emails from user account inbox 
"""

from gmail import GmailClient

from config import get
config = get()

def get_user_ham():
  c = GmailClient()
  c.login(config["USER_EMAIL"], config["USER_PASS"])
  
