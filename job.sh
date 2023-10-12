#!/bin/bash

SBATCH -n 16                              # Number of cores
SBATCH --time=80:00:00                      # hours:minutes:seconds
SBATCH --mem-per-cpu=2000
SBATCH --tmp=4000                        # per node!!
SBATCH --job-name=bkt_cr4
SBATCH --output=./bkt_cr4.out
SBATCH --error=./bkt_cr4.err

# run experiment
python ./BasicForgets.py