#!/usr/bin/sh
#usage: sh teste_SRA_rfo.sh list_accessions.txt

cat "$1" | while read i
do
	date
	echo "Downloading FASTQ $i"
	fastq-dump -A "$i" -O ./
done
