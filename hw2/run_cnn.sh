#!/bin/bash 

python bonus2/eval.py --positive_data_file=$1 --negative_data_file=$1 --eval_train --checkpoint_dir="bonus2/runs/checkpoints/" > $2

