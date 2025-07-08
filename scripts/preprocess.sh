#! /bin/bash

python main.py processtask --data_dir data/ml-100k --dataset ml-100k --n_neg_items 7

python main.py processtask --data_dir data/Beauty --dataset amazon --n_neg_items 7

python main.py sampletask --data_dir data/Beauty/test.csv --output_dir data/Beauty/test_1000.csv --random --samples 1000
