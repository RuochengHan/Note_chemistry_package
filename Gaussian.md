# Some differences between G03 G09 and G16
1. G03 use scf=conver=6, G09 and G16 use scf=conver=8 (scf=tight)
2. G03 and G09 use integral=finegrid, G16 use integral=ultrafine

# SCF
1. scf=(fermi,conver=6,maxcycle=128)


# ECP
1. Chinese: http://sobereva.com/60
```bash
%mem=10gb
%nprocshared=4

#p B3LYP/genecp

NaH

0 1
Na 0. 0. 0.
H  0. 0. 0.

Na 0
Lanl2DZ
****
H 0
6-31G**
****
Na 0
Lanl2
```

# Vibrational resolved electronic spectrum
1. http://sobereva.com/223
2. http://bbs.keinsci.com/thread-774-1-1.html

