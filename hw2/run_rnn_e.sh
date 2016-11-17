#!/bin/bash

# please download the model at https://drive.google.com/file/d/0B6z4WeJetpHgeTBaTGF1cmkzaDg/view?usp=sharing
# unzip the file and name the folder "weights"
# put "weights" folder in the same directory with rvnn.py and preprocess.py

mkdir trees

# preprocess testing data
python3 preprocess.py $2

# test the model
python rvnn.py test $3
