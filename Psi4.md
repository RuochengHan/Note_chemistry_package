# Geom Opt
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
4. Geom not converge after many iters, calculate full Hessain matrix every step:
```bash
set full_hess_every 1
```

SCF
1. Check the geometry

2. Use second-order SCF convergence methods:
```bash
set soscf true
```
