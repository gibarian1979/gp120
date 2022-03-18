#!/usr/bin/env python3
import sys

f = None
for line in sys.stdin:
    line = line.strip()
    if(line.startswith("MODEL")):
        print(line)
        idx = line.split(" ")[-1]
        f = open(idx+".pdb","w")
    elif(line.startswith("ENDMDL")):
        if(f):
          f.close()
    elif(line.startswith("END")):
        continue
    else:
        f.write(line+"\n")



