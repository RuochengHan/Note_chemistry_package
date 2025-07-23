## Clean Stucture
1. clean sdf structure in 2D (bond length recompute, etc.), without rotating or reordering
```python
def clean_layout(mol_block):
    indigo = Indigo()

    mol_indigo = indigo.loadMolecule(mol_block)
    mol_indigo.clean2d()

    cleaned_mol_block = mol_indigo.molfile()
    return cleaned_mol_block
```
