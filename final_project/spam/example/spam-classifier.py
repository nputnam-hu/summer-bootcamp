"""
~~~spam-classifyer.py~~~
Noah Putnam
program to classify how close a give string is to spam using NLTK
"""

import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.tolkenize import word_tolkenize

import random
import os

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
        with open(os.path.join(directories, filename), encoding="utf-8") as f:
          ham = f.read()
          words = word_tolkenize(ham)
          ham_list.append((cast_todict(words), "ham"))

    if (os.path.split(directories)[1]  == 'spam'):
      for filename in files:
        with open(os.path.join(directories, filename), encoding="utf-8") as f:
          spam = f.read()
          words = word_tolkenize(spam)
          spam_list.append((cast_todict(words), "spam"))

  return (ham_list, spam_list)

def classifier():
  ham_list, spam_list = load_data()
  combined_list = ham_list + spam_list
  # shuffle our list 
  training_set = random.shuffle(combined_list)
  classifier = NaiveBayesClassifier.train(training_set)
  return classifier

