ConTest - Paired-end reads with reference genome

## LISTS OF SOFTWARE AND DATA NEEDED

List of software
- snakemake (v5.1.4) NOTE: newer versions might not be compatible with cluster config
- bowtie2 (v2.3.4.3) NOTE: older versions might produce unreadable sam files for samtools
- bedtools (v2.24.0)
- samtools (v1.5) 
- bioawk
- RepeatMasker (v4.0.7)
- blast (v2.4.0+)
- other: sed, awk, grep

List of files
- raw reads in fastq format
- fasta file with TE DNA sequence of interest
- Repbase TE database including TE of interest
- genomes

File structure
- raw reads in separate folder
- genomes: one folder with subfolders containing all genomes per taxon (e.g. 'genomes/mammals' and 'genomes/nematodes'. Genomes need to be gzipped.

Other information needed:
- name of test genome (without '.gz' ending)
- database size (size of largest genome of all compared taxa) 
- names of self and non-self taxa (same as taxa above, e.g. 'mammals' and 'nematodes')
- reads accessions and insert size


## INSTALL SOFTWARE with conda (channel:bioconda) 

You can either install the software as listed above in a new conda environment (recommended) or use your own software versions. Note that this might result in incompatibilities. Conda command to install software in a new environment is noted below. You need to have the bioconda channel added to your conda config (conda config --add channels bioconda). 


## GET FILES

Make sure you have all read and genome files in directories as described above. 


## MODIFY SNAKEMAKE FILES

You need to modify the config.yaml and cluster.json according to your data and computing resources. The example config file works on a lsf system. For more information see https://snakemake.readthedocs.io/en/stable/snakefiles/configuration.html . If you are not using a cluster system, omit the cluster.json and the cluster flags in the snakemake command.


## RUN SNAKEMAKE

If you have everything prepared, you can start running snakemake. The -j flag specifies the maximum number of jobs submitted simultaneously to the cluster. 


```
# Create conda contest environment (openssl1.0 for samtools; conda pulls automatically openssl1.1 which is incompatible)
conda create -n contest_R snakemake==5.1.4 bowtie2==2.3.4.3 bedtools==2.24.0 samtools==1.5 bioawk RepeatMasker==4.0.7 blast seqtk==1.2 openssl=1.0

conda activate contest_R

mkdir -p logs/cluster

# edit config.yaml and cluster.json as described above

# Run SnakeMake
snakemake -j 56 --cluster-config cluster.json --cluster "bsub -n {cluster.nCPUs} -W {cluster.time} -e {cluster.error} -o {cluster.output} -M {cluster.memory} -R {cluster.resources}"
``` 


