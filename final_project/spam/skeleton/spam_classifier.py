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
  return {}

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
          pass
    if 'spam' in os.path.abspath(root):
      for filename in files:
        filecount += 1
        with open(os.path.join(root, filename), encoding='latin-1') as f:
          pass
    dircount += 1


  return (ham_emails, spam_emails)

def get_classifier():
  ham_emails, spam_emails = load_data()
  total_emails = ham_emails + spam_emails
  print('finished gathering data')


  training_set = []
  print('creating classifier...')
  classifier = NaiveBayesClassifier.train(training_set)
  accuracy = nltk.classify.util.accuracy(classifier, test_set)
  print('Accuracy: ', accuracy * 100)
  print('Most predictive words: ')
  classifier.show_most_informative_features(20)

  return classifier

def main():
  pass

if __name__ == '__main__':
  main()