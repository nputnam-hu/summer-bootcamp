"""
~~~spam-classifyer.py~~~
Noah Putnam
program to classify how close a give string is to spam using NLTK, pulling strings for users gmail account
"""

import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.tokenize import word_tokenize
import random
import time
import os

from email_getter import get_emails
import bootcamp

# feeds a list of words into a dict where all the values map to True (important for NaiveBayesClassifier)
def cast_todict(words):
    return dict( [ (word, True) for word in words] )

# clears the terminal screen using escape sequence
def clear():
  os.system("printf '\033c'")

# loads the data in from the corpus/ dir into our classifier
def load_data():
  ham_emails = []
  spam_emails = []
  dircount = 0
  filecount = 0
  num_dirs = 285

  walkdir = os.path.abspath('corpus/')
  for root, subdirs, files in os.walk(walkdir):
    clear()
    print('gathering training data...\nprocessed %i/%i directories, %i files' % (dircount, num_dirs, filecount)),
    if 'ham' in os.path.abspath(root):
      for filename in files:      
        filecount += 1
        with open(os.path.join(root, filename), encoding='latin-1') as f:
          ham = f.read()
          words = word_tokenize(ham)
          ham_emails.append((cast_todict(words), 'ham'))

    if 'spam' in os.path.abspath(root):
      for filename in files:
        filecount += 1
        with open(os.path.join(root, filename), encoding='latin-1') as f:
          spam = f.read()
          words = word_tokenize(spam)
          spam_emails.append((cast_todict(words), 'spam'))

    dircount += 1


  return (ham_emails, spam_emails)

def get_classifier():
  ham_emails, spam_emails = load_data()
  total_emails = ham_emails + spam_emails
  print('finished gathering data')

  # shuffle our list and split it up
  random.shuffle(total_emails)
  training_proportion = int(len(total_emails) * .7)
  training_set = total_emails[:training_proportion]
  test_set =  total_emails[training_proportion:]

  print('creating classifier...')
  classifier = NaiveBayesClassifier.train(training_set)

  return classifier

def main():
  classifier = get_classifier()

  num_emails = -1
  while num_emails < 0:
    num_emails = bootcamp.get_int("number of emails?")

  print('gathering emails...')
  emails = get_emails(num_emails)

  print('classifying emails...')
  spam_out = open('spam.txt', 'w')
  ham_out = open('ham.txt', 'w')
  for email in emails:
    if email:
      classification = classifier.classify(cast_todict(word_tokenize(email))) 
      if classification == 'spam':
        spam_out.write(email + '\n\n')
      if classification == 'ham':
        ham_out.write(email + '\n\n')
  print('finished')


if __name__ == '__main__':
  main()
