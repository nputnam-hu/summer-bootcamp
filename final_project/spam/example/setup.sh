#!/bin/bash
pip3 install -r requirements.txt
mkdir corpus
mkdir corpus/ham
mkdir corpus/spam
for filename in corpus_tars/ham/*.tar.gz
do
  echo unzipping "$filename"...
  tar zxf $filename -C corpus/ham
done
for filename in corpus_tars/spam/*.tar.gz
do 
  echo unzipping "$filename"...
  tar zxf $filename -C corpus/spam
done
echo All Done!