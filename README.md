# ConTest - Test for contamination in sequence reads

ConTest consists of three different Snakemake pipelines to test for contamination. It was designed to test with sequencing reads if a retrotransposon is endogenous in a species, or if it got into a genome assembly through contamination. 


## Citation 

Sonja M. Dunemann and James D. Wasmuth (2018): A nematode retrotransposon in the common shrew: horizontal transfer between parasite and host. doi: https://doi.org/10.1101/424424 


## Snakemake pipelines

Pipelines are based on: long reads, paired-end reads with reference genome, and paired-end reads without reference genome. The pipelines are independent of each other. 


## What is needed to run ConTest

To run any pipeline, these files are needed: sequence reads (and genome assembly for the reference based workflow) from the species to be tested, a transposon database, all genome assemblies from the taxon which is being tested for contamination, and all genome assemblies from the putative contaminating taxon. 

Software dependencies can be installed with conda. For more details, refer to the README files of each pipeline. 




