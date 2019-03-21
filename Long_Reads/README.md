# ConTest - Long Reads

## List of software and files

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


## Install dependencies with conda (channel:bioconda) 

You can either install the software as listed above in a new conda environment (recommended) or use your own software versions. Note that this might result in incompatibilities (more about this in the individual Readme files). Conda co
mmands to install software are in all Readme files. You need to have the bioconda channel added to your conda config (conda config --add channels bioconda).


```
conda create -n contest_LR snakemake==5.1.4 diamond==0.9.10 seqtk==1.2 RepeatMasker==4.0.7 blast
```


## Modify configuration files config.yaml and cluster.json

You need to modify the config.yaml and cluster.json according to your data and computing resources. The example config file works on a lsf system. For more information see https://snakemake.readthedocs.io/en/stable/snakefiles/configura
tion.html . If you are not using a cluster system, omit the cluster.json and the cluster flags in the snakemake command.



## RUN SNAKEMAKE

```
conda activate contest_LR

mkdir -p logs/cluster

snakemake -j 1 --cluster-config cluster.json --cluster "bsub -n {cluster.nCPUs} -W {cluster.time} -e {cluster.error} -o {cluster.output} -M {cluster.memory} -R {cluster.resources}"
``` 

