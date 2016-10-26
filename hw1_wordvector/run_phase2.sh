#!/bin/bash 

mkdir $2
mkdir tmp2

# data: ptt corpus
python phase2.py --train_data=$1 --eval_data=eval/questions-words-phase2-dev.txt --save_path=tmp2

python filter/filterVocab.py filter/fullVocab_phase2.tx < ptt > filter_vec.txt

rm -r tmp2
