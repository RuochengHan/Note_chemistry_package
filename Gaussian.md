# Some differences between G03 G09 and G16
1. G03 use scf=conver=6, G09 and G16 use scf=conver=8 (scf=tight)
2. G03 and G09 use integral=finegrid, G16 use integral=ultrafine

# SCF
1. scf=(fermi,conver=6,maxcycle=128)
2. when use diffuse function, Gaussian automatically reduces the integration grid at the beginning of the calculation: \\
   SCF=NoVarAcc to stop reducing and int=acc2e=12 to increase integration accuracy.

Ref.:
https://wongzit.github.io/method-to-solve-the-scf-not-converged/

# OPT
1. not converge:
```bash
Opt=(maxcycles=50, calcall)
```

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

# external basis set
Example: Note the blank line!!
```bash
%mem=60gb
%nprocshared=16

#p b3lyp/gen

Name

0 1
C X Y Z
...

@/xxx/def2-svpd.gbs

```
/xxx/def2-svpd.gbs: Note that remove the blank lines before basis set and after basis set:
http://www.ccl.net/chemistry/resources/messages/2016/07/21.005-dir/index.html

```bash
!----------------------------------------------------------------------
! Basis Set Exchange
! Version 0.10
! https://www.basissetexchange.org
!----------------------------------------------------------------------
!   Basis set: def2-SVPD
! Description: def2-SVPD
!        Role: orbital
!     Version: 1  (Data from Turbomole 7.3)
!----------------------------------------------------------------------
-H     0
S    3   1.00
     13.0107010              0.19682158D-01
      1.9622572              0.13796524
      0.44453796             0.47831935
S    1   1.00
      0.12194962             1.0000000
P    1   1.00
      0.8000000              1.0000000
P    1   1.00
      0.11704099050          1.0000000
****
```

# Vibrational resolved electronic spectrum
1. http://sobereva.com/223
2. http://bbs.keinsci.com/thread-774-1-1.html

# chekcpoints file
move between machines
```bash
formchk file_name.chk file_name.fchk
unfchk file_name.fchk file_name.chk

chkmove f file_name.chk file_name.xfr # G03
chkmove u file_name.xfr file_name.chk # G03
```
