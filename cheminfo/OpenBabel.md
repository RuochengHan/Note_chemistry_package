1. Openbabel GetSymbol() and GetType() are different. \
   GetType() is returning the atom type (which may be "Car", "Npl", etc.) instead of the element symbol ("C", "N", ...).


2. 3.x and 2.x are different in GetSymbol
```python
# 3.x:
openbabel.GetSymbol(atom.GetAtomicNum())

# 2.x
atom.GetSymbol()
```
