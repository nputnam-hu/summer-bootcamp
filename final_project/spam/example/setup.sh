#!/bin/bash
pip3 install -r requirements.txt
for filename in courpus_tars/*/*.tar.gz
do
  tar zxf $filename
done