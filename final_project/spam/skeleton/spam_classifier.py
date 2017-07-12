"""
~~~spam-classifyer.py~~~
program to classify how close a give string is to spam using NLTK, pulling strings for users gmail account
"""

import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.tokenize import word_tokenize
import os

from email_getter import get_emails
import bootcamp

# feeds a list of words into a dict where all the values map to True (important for NaiveBayesClassifier)
def cast_todict(words): 
  """
  example input->output:
  ['apple', 'bannana', 'carrot'] -> {'apple':True,'bannana':True,'carrot':True}
  ['Alice', 'Alice', 'Alice', 'Bob'] -> {'Alice':True,'Bob':True}
  """
  return {}

# loads the data in from the corpus/ dir into our classifier
def load_data():
  walkdir = os.path.abspath('corpus/')
  # os.walk will recursively go through all of the files in the corpus directory
  # and place them in the files variable
  for root, subdirs, files in os.walk(walkdir):
    # if we're in the ham directory
    if 'ham' in os.path.abspath(root):
      for filename in files:      
        with open(os.path.join(root, filename), encoding='latin-1') as f:
          # TODO: read data and load it into the ham_emails list
          example_entry = ({}, 'ham')
    # if we're in the spam directory
    if 'spam' in os.path.abspath(root):
      for filename in files:
        with open(os.path.join(root, filename), encoding='latin-1') as f:
          # TODO: read data and load it into the ham_emails list
          example_entry = ({}, 'spam')



  return (ham_emails, spam_emails)

def get_classifier():
  ham_emails, spam_emails = load_data()

  # TODO: combine the lists and randomly shuffle them

  # TODO: partition the lists between training and test sets

  # TODO: format everything correctly using word_tokenize and cast_todict
  training_set = []
  classifier = NaiveBayesClassifier.train(training_set)
  accuracy = nltk.classify.util.accuracy(classifier, test_set)
  print('Accuracy: ', accuracy * 100)
  print('Most predictive words: ')
  classifier.show_most_informative_features(20)

  return classifier

def main():
  ## TODO: integrate everything

if __name__ == '__main__':
  main()
