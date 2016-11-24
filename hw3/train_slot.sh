#!/bin/bash
data_dir=data
model_dir=model_slot
max_sequence_length=50  # max length for train/valid/test sequence
task=tagging  # available options: intent; tagging; joint
bidirectional_rnn=True  # available options: True; False
max_training_steps=10000
num_layers=1
word_embedding_size=128

#rm -rf model_slot/
python slot.py --data_dir $data_dir \
      --train_dir   $model_dir\
      --max_sequence_length $max_sequence_length \
      --task $task \
      --bidirectional_rnn $bidirectional_rnn \
      --max_training_steps $max_training_steps \
      --num_layers $num_layers \
      --word_embedding_size $word_embedding_size
