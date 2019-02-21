
I. LISTS OF SOFTWARE AND DATA NEEDED

List of software
- snakemake (v5.1.4) NOTE: don't use newer version, not compatible with cluster config
- bowtie2 (v2.3.3.1)
- bedtools (v2.24.0)
- samtools (v1.5) 
- bioawk
- RepeatMasker (v4.0.7)
- blast (v2.4.0+)
- other: sed, awk, grep

List of files
- raw reads
- fasta file with RTE of interest
- Repbase TE database
- genomes

File structure
- raw reads in folder
- genomes: one folder with subfolders containing all genomes per taxon

Other information needed:
- name of test genome
- database size (size of largest genome of all compared taxa) 
- names of self and non-self taxa
- reads accessions and insert size


II. INSTALL SOFTWARE with conda (channel:bioconda) 
conda search snakemake==5.1.4
conda search bowtie2==2.3.3.1
conda search bedtools==2.24.0
conda search samtools==1.5
conda search bioawk 
conda search RepeatMasker==4.0.7
conda search blast 


III. GET FILES

IV. MODIFY SNAKEMAKE CONFIG FILE

V. RUN SNAKEMAKE

```
snakemake -s Snakefile -j 1 --cluster-config cluster.json --cluster "bsub -n {cluster.nCPUs} -W {cluster.time} -e {cluster.error} -o {cluster.out} -M {cluster.memory} -R {cluster.resources}"
``` 


