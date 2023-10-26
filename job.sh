#!/bin/bash

# SBATCH -n 20                             # Number of cores
# SBATCH --time=3-5                      # hours:minutes:seconds
# SBATCH --mem-per-cpu=40G
# SBATCH --tmp=4000                        # per node!!
# SBATCH --job-name=bkt_cr4
# SBATCH --output=./bkt_cr4.out
# SBATCH --error=./bkt_cr4.err

SBATCH --mail-type=ALL                           # mail configuration: NONE, BEGIN, END, FAIL, REQUEUE, ALL
SBATCH --output=/absolute/path/to/log/%j.out     # where to store the output (%j is the JOBID), subdirectory "log" must exist
SBATCH --error=/absolute/path/to/log/log/%j.err  # where to store error messages
# run experiment
python ./BasicForgets.py