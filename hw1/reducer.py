# !/usr/bin/python

import sys

tcz = 0
tmean = 0
tvar = 0

for line in sys.stdin:
    cz, mean, var = line.rstrip().split('\t')
    try:
        cz, mean, var = int(cz), float(mean), float(var)
    except ValueError:
        continue
    tmean = (tcz * tmean + cz * mean) / (tcz + cz)
    tvar = ((cz * var + tcz * tvar) / (cz + tcz)) \
           + (tcz * cz) * ((tmean - mean) / (tcz + cz)) ** 2
    tcz += cz

print(tmean, tvar, sep='\t')
