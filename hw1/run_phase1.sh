#!/bin/bash 

mkdir $2
mkdir tmp

# data: text8
python word2vec.py --train_data=$1 --eval_data=eval/questions-words.txt --save_path=tmp --epochs_to_train=100

python filter/filterVocab.py filter/fullVocab.txt < tmp/word2vec > $2/filter_word2vec.txt

python glove.py

python filter/filterVocab.py filter/fullVocab.txt < tmp/glove > $2/filter_glove.txt


