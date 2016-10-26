#!/bin/bash 

mkdir $2
mkdir tmp

# data: text8
python word2vec.py --train_data=$1 --eval_data=eval/questions-words.txt --save_path=tmp

python filter/filterVocab.py filter/fullVocab.txt < word2vec > filter_word2vec.txt

python glove.py

python filter/filterVocab.py filter/fullVocab.txt < glove > filter_glove.txt

rm -r tmp