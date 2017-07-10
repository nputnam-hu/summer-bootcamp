#!/bin/bash
pip3 install -r requirements.txt
mkdir corpus
for filename in corpus_tars/*/*.tar.gz
do
  echo 
  tar zxf $filename -C corpus/
done
