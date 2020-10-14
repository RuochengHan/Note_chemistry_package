## Geom Opt
1. More opt iterations than 30:
```bash
set geom_maxiter 200
```
2. When geom convergence fails, molecule has long 'arms':
```bash
set opt_coordinated both
```
3. Error 'Unable to compute torsion value':
```bash
set opt_coordinated cartesian
```
4. Geom not converge after many iters, use other method for gradient or calculate full Hessain matrix every n step:
```bash
set step_type nr
set full_hess_every n
```

## SCF
1. Check the geometry

2. Use second-order SCF convergence methods:
```bash
set soscf true
```

## Others
1. Psi4 1.4 always use RIJK approximation by default, use the usual one:
```bash
set scf_type direct
```
2. Even you set the above variable, still it will use some intermediate step with RI.
3. For MP2 RI (density fitting) is ok, but for CCSD, the printed out orbital/FCIDUMP/Amplitudes cannot be used to reproduce the correlation
energy. You need to set it to direct or pk. However for triple bond systems like C2H2, even with direct or pk, the printed out infos cannot 
reproduce the results. In this case, you need to use PYSCF. 
