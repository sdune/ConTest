# ConTest - Test for contamination in sequence reads

ConTest consists of three different Snakemake pipelines to test for contamination


## Citation 

Sonja M. Dunemann and James D. Wasmuth (2018): A nematode retrotransposon in the common shrew: horizontal transfer between parasite and host. doi: https://doi.org/10.1101/424424 


## Snakemake pipelines

Pipelines are based on: long reads, paired-end reads with reference genome, and paired-end reads without reference genome. The paired-end reads with reference genome approach is computationally most expensive. 


## Install software with conda (channel:bioconda) 

You can either install the software as listed above in a new conda environment (recommended) or use your own software versions. Note that this might result in incompatibilities (more about this in the individual Readme files). Conda commands to install software are in all Readme files. You need to have the bioconda channel added to your conda config (conda config --add channels bioconda). 



## Modify configuration files

You need to modify the config.yaml and cluster.json according to your data and computing resources. The example config file works on a lsf system. For more information see https://snakemake.readthedocs.io/en/stable/snakefiles/configuration.html . If you are not using a cluster system, omit the cluster.json and the cluster flags in the snakemake command.



## Run Snakemake

If you have everything prepared, you can start running snakemake. The -j flag specifies the maximum number of jobs submitted simultaneously to the cluster. 


```
# Create and activate conda contest environment 

conda activate contest_environment

# Edit config.yaml and cluster.json

# Run Snakemake (Test with '-np' or '-n --quiet' option)

snakemake -j 1 --cluster-config cluster.json --cluster "bsub -n {cluster.nCPUs} -W {cluster.time} -e {cluster.error} -o {cluster.output} -M {cluster.memory} -R {cluster.resources}"
``` 


