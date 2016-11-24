#!/bin/bash
data_dir=data
model_dir=model_tmp
max_sequence_length=50  # max length for train/valid/test sequence
task=intent  # available options: intent; tagging; joint
bidirectional_rnn=True  # available options: True; False

python preprocess_test.py $1

cp data/test/test.seq.in data/test/test.seq.out
cp data/test/test.seq.in data/test/test.label

python intent.py $2  --data_dir $data_dir \
      --train_dir   $model_dir\
      --max_sequence_length $max_sequence_length \
      --task $task \
      --bidirectional_rnn $bidirectional_rnn


