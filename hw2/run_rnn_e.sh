#!/bin/bash

#bash run_rnn_e.sh input_file tree_file output_file

# get model
#mkdir weights
#wget "http://www.csie.ntu.edu.tw/~b02902034/model.zip"
#unzip model.zip
#mv rnn_embed=300_l2=0.020000_lr=0.001000.weights.temp weights/

# preprocess testing data
python3 preprocess.py $2

# test the model
python rvnn.py test $3
