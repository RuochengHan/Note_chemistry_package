For read molden file, **cclib** does not work, **orbkit** is the best choice, but need to compile:
Follow github.com/orbkit/orbkit/

and 
```bash
pip install scikit-image h5py # 0.21.0, 3.8.0
or 
conda install scikit-image h5py
```

Weird points for **orbkit**:
Molden read and integration of (PS) does not give correct number of electrons. 
Test for Psi4 B3LYP/6-31(d) 34.17 vs 34, and GFN2-xTB 21.4 vs 26.
