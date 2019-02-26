# Contest - Paired-end reads without reference


## List of software and data

List of software
- snakemake (v5.1.4) NOTE: don't use newer version, not compatible with cluster config
- fastqc (v0.11.7)
- seqtk (v1.2-r94)
- RepeatMasker (v4.0.7)
- blast (v2.4.0+)
- other: cut, sort, uniq, sed, awk, grep

List of files
- raw reads
- fasta file with RTE of interest
- Repbase TE database (must include RTE of interest)
- genomes

File structure
- raw reads in folder
- genomes: one folder with subfolders containing all genomes per taxon

Other information needed:
- name of test genome
- database size (size of largest genome of all compared taxa) 
- names of self and non-self taxa
- read accessions


## Install software with conda (channel:bioconda) 

```
conda create -n contest_NRef snakemake==5.1.4 bioawk RepeatMasker==4.0.7 blast fastqc==0.11.7 seqtk=1.2
```

## GET FILES

## MODIFY SNAKEMAKE CONFIG FILE

## RUN SNAKEMAKE

```
# Create conda environment
conda activate contest_NRef

# Prepare log directories
mkdir -p logs/cluster

# Edit config.yaml and cluster.json

# Submit SnakeMake
snakemake -j 1 --cluster-config cluster.json --cluster "bsub -n {cluster.nCPUs} -W {cluster.time} -e {cluster.error} -o {cluster.output} -M {cluster.memory} -R {cluster.resources}"
``` 


