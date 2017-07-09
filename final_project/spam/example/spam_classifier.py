"""
~~~spam-classifyer.py~~~
Noah Putnam
program to classify how close a give string is to spam using NLTK, pulling strings for users gmail account
"""

import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.tokenize import word_tokenize
import random
import os

from email_getter import get_emails

rootdir = '/Users/noahputnam/hsadev/summer-bootcamp/final_project/spam/example/corpus'


# feeds a list of words into a dict where all the values map to True (important for NaiveBayesClassifier)
def cast_todict(words):
  return_dict = {}
  for word in words:
    return_dict[word] = True

  return return_dict

def load_data():
  ham_list = []
  spam_list = []

  for directories, subdirs, files in os.walk(rootdir):
    if (os.path.split(directories)[1]  == 'ham'):
      for filename in files:      
        with open(os.path.join(directories, filename), encoding='latin-1') as f:
          ham = f.read()
          words = word_tokenize(ham)
          ham_list.append((cast_todict(words), 'ham'))

    if (os.path.split(directories)[1]  == 'spam'):
      for filename in files:
        with open(os.path.join(directories, filename), encoding='latin-1') as f:
          spam = f.read()
          words = word_tokenize(spam)
          spam_list.append((cast_todict(words), 'spam'))

  return (ham_list, spam_list)

def get_classifier():
  ham_list, spam_list = load_data()
  print(ham_list)
  combined_list = ham_list + spam_list
  # shuffle our list 
  training_set = random.shuffle(combined_list)
  classifier = NaiveBayesClassifier.train(training_set)
  return classifier

def main():
  emails = get_emails()
  classifier = get_classifier()

  file = open('spam.txt', 'w')
  for email in emails:
    if classifier.classify(email) == 'spam':
      file.write("SPAM:" + email)

if __name__ == '__main__':
  main()