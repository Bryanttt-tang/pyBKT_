#!/bin/bash

SBATCH -n 20                             # Number of cores
SBATCH --time=3-5                      # hours:minutes:seconds
SBATCH --mem-per-cpu=40G
SBATCH --tmp=4000                        # per node!!
SBATCH --job-name=bkt_cr4
SBATCH --output=./bkt_cr4.out
SBATCH --error=./bkt_cr4.err

# run experiment
python ./BasicForgets.py