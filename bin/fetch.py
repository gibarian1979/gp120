#!/usr/bin/env python3
import os,sys,getopt
from Bio import SeqIO
from Bio import Entrez

# demo calls:
# ./fetch.py -d nuccore -i AY278554.2 -f "gb,xml"
# ./fetch.py -d nuccore -i AY278554.2 -f "gb,text"
# ./fetch.py -i AKR75206.1 -f "gp,xml"
# ./fetch.py -i AKR75206.1 -f "gp,text"

Entrez.email = "me@localhost.com" 

db = "protein"
out = sys.stdout
mode = ('fasta','text')
ids = None

try:
    opts, args = getopt.getopt(sys.argv[1:],"hd:o:i:f:",["help","db=","out=","ids=","fmt="])
except getopt.GetoptError:
    print('fetch.py -h -d <db> [-i <id-list> | STDIN ] [-o <outputfile> | STDOUT] [-f <type,mode>]]')
    sys.exit(2)
for opt, arg in opts:
    if opt in( "-h", "--help"):
        print('fetch.py -h -d <db> [-i <id-list> | STDIN ] [-o <outputfile> | STDOUT]')
        sys.exit()
    elif opt in ("-d", "--db"):
        # https://www.ncbi.nlm.nih.gov/books/NBK25497/table/chapter2.T._entrez_unique_identifiers_ui/?report=objectonly
        db = arg
    elif opt in ("-i", "--ids"):
        ids = arg.split(";|,")
    elif opt in ("-o", "--out"):
        out = open(arg,"w")
    elif opt in ("-f","--fmt"):
        # https://www.ncbi.nlm.nih.gov/books/NBK25499/table/chapter4.T._valid_values_of__retmode_and/?report=objectonly
        # gp,text
        # fasta,text
        # native,xml
        # fasta,xml
        mode = arg.split(",")

if not ids:
    ids = []
    for line in sys.stdin:
        id = line.strip()
        ids.append(id)

for id in ids:
    net_handle = Entrez.efetch(
        db=db, id=id, rettype=mode[0], retmode=mode[1]
    )
    data = net_handle.read()
    if(type(data)==bytes):
       out.buffer.write(data)
    else:
       out.write(data)
    net_handle.close()
out.close()

