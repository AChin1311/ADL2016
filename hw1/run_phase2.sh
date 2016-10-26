#!/bin/bash 

mkdir $2
mkdir tmp

# data: ptt corpus
python phase2.py --train_data=$1 --eval_data=eval/questions-words-phase2-dev.txt --save_path=tmp --epochs_to_train=1

python filter/filterVocab.py filter/fullVocab_phase2.txt < tmp/ptt > $2/filter_vec.txt

