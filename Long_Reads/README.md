# ConTest - Long Reads

## LISTS OF SOFTWARE AND DATA NEEDED

List of software
- snakemake (v5.1.4) NOTE: don't use newer version, not compatible with cluster config
- fastqc (v0.11.7)
- seqtk (v1.2-r94)
- RepeatMasker (v4.0.7)
- blast (v2.4.0+)
- other: cut, sort, uniq, sed, awk, grep

List of files
- raw reads
- RTE name and fasta file (RTE name must be the same as in Repbase TE database (see below)
- Repbase TE database (must include RTE of interest)
- genomes (gzipped)

File structure
- raw reads in folder
- genomes: one folder with subfolders containing all genomes per taxon

Other information needed:
- name of test genome
- database size (size of largest genome of all compared taxa) 
- names of self and non-self taxa
- read accessions


# INSTALL SOFTWARE with conda (channel:bioconda) 

```
conda create -n contest_LR snakemake==5.1.4 diamond==0.9.10 seqtk==1.2 RepeatMasker==4.0.7 blast
```

# GET FILES

# MODIFY SNAKEMAKE CONFIG FILE

# RUN SNAKEMAKE

```
conda activate contest_LR

mkdir -p logs/cluster

snakemake -j 1 --cluster-config cluster.json --cluster "bsub -n {cluster.nCPUs} -W {cluster.time} -e {cluster.error} -o {cluster.output} -M {cluster.memory} -R {cluster.resources}"
``` 


