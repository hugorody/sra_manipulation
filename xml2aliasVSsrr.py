#!/usr/bin/python3
#Generate output from SRA experiments with each alias and its correspondents SRR numbers
#Input: XML file obtained from NCBI

import xml.etree.ElementTree as ET
tree = ET.parse('SraExperimentPackage.xml')
root = tree.getroot()

experiment = "EXPERIMENT" #alias, accession: SRX number
sample = "SAMPLE" #alias, accession: SRS number
run = "RUN" #SRR number
member = "Member" #sample_name, accession: SRS number

finalcatalog = {}

for i in root:
    for k in i.iter(sample): #get alias
        alias = k.get('alias')
    for j in i.iter(run): #get SRR number
        SRR = j.get('accession')
    for o in i.iter(member):
        SRS = o.get('accession') #get SRS number

    if alias not in finalcatalog:
        finalcatalog[alias] = [SRR]
    else:
        addalias = finalcatalog[alias]
        addalias.append(SRR)
        finalcatalog[alias] = addalias

output = open("alias_correspondence2_SRRs.txt","w")
for i in finalcatalog.items():
    for j in i[1]:
        output.write(i[0] + " " + j + "\n")
output.close()
