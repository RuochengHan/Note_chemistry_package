# xtb4stda
Cannot compile, use binary one!

Example of running:
```bash
~/softwares/stddft_stda/binary/xtb4stda coord.xyz -parx ~/softwares/stddft_stda/xtb4stda/.param_stda2.xtb -parv ~/softwares/stddft_stda/xtb4stda/.param_stda1.xtb -chrg -1  > gs.stda-xtb.out
```

# stda
## Install:
Need ifort and intel-mkl to compile

Installation or binary are both fine.

For xtb
```bash
stda -xtb -e 10
```
For gaussian
```bash
stda -f ../molden.input -ax 0.2 -e 10 -sty 3 > output # 0.2 is Hartree--Fock exchange factor
```

note that stda output need to add UV (or substitute VOLE). ANd need to correct Fortran number
```bash
# Add E to 1.1234-104 -> 1.1234E-104
sed -i -E "s/([0-9])\-([0-9])/\1E\-\2/g" $1
```
