#!/bin/bash

# preprocess testing data
python3 preprocess.py $2

# test the model
python rvnn.py test $3
