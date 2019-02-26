#! ~/miniconda3/bin/python3

import itertools

def filter_mates(singles,mates,fasta,outfasta,transposon):
    reads={}

    with open(singles,'r') as input:         
        for line in itertools.islice(input,3,None):
            line.strip()
            read=line.split()[4][:-2]              
            te=line.split()[9]                     
            star=len(line.split())              
            if (transposon in te and star==15):
                if not read in reads:
                    reads[read]={}         
                reads[read]["single"]="yes"        
    
    with open(mates,'r') as input2:
        for line in itertools.islice(input2,3,None):
            line.strip()
            read=line.split()[4]
            if not read in reads:
                reads[read]={}
            reads[read]["mate"]="masked"
    
    outfile=open(outfasta,'w')
    
    with open(fasta,'r') as input3:
        for line in input3:
            line.strip()
            if line.startswith(">"):
                cols=line.split()
                read=cols[0][1:]
                if (read in reads and "single" in reads[read] and "mate" not in reads[read]):
                    outfile.write(cols[0]+"\n")
                    next="yes"
                else:
                    next="no"
            else:
                if next=="yes":
                    outfile.write(line)
         
    #for key,value in reads.items():
    #    if not "mate" in reads[key] and "single" in reads[key]:
    #        print (key,value)
    #
    #print (len(reads))

filter_mates(snakemake.input[0],snakemake.input[1],snakemake.input[2],snakemake.output[0],snakemake.params[0])
