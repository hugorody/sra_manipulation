#!/usr/bin/python3

import subprocess

#output directories
HD80gb = "/media/hugo/487e2510-80e1-459c-a071-53e6ee542f70/"
HD59gb = "/media/hugo/C8E88607E885F44A/sra/"
HD1 = "/home/hugo/Documents/"

#list of SRR numbers to filter out from list
downloadHD80gb = ["SRR063590","SRR063591","SRR063592","SRR063593","SRR063594",
			"SRR063595","SRR063596","SRR063597","SRR063598","SRR063599",
			"SRR063600","SRR063601","SRR063602","SRR063603","SRR063604",
			"SRR063605","SRR063606","SRR063607","SRR063608","SRR063609"]
			
downloadHD59gb = ["SRR063610","SRR063611","SRR063612","SRR063613","SRR063614",
			"SRR063615","SRR063616","SRR063617","SRR063618","SRR063619",
			"SRR063620","SRR063621"]

print ("Número de rquivos baixados:",int(len(downloadHD80gb) + len(downloadHD59gb)))

#download from file list
with open("SraAccList.txt","r") as set1:
	for i in set1:
		i = i.rstrip()
		abrev = i[0:6]
		if i not in downloadHD80gb and i not in downloadHD59gb:
			print ("Downloading " + i)
			link = "ftp://ftp.ncbi.nlm.nih.gov/sra/sra-instant/reads/ByRun/sra/SRR/" + abrev + "/" + i + "/" + i + ".sra -O " + HD1 + i + ".sra"
			download = subprocess.Popen("wget " + link, shell=True)
			download.wait()
