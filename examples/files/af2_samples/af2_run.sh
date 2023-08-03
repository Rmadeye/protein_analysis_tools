#!/bin/bash 

#SBATCH -p gpu
#SBATCH -n 4
#SBATCH -N 1
#SBATCH --gres=gpu:1
#SBATCH --exclude=edi0[0,1,2,3]
#SBATCH --mem=16GB
#SBATCH -J files/af2_samples
source /opt/miniconda3/bin/activate cf_1.5
colabfold_batch af2input_fasta.csv . --num-models 5 --num-recycle 5   --num-seeds 1  