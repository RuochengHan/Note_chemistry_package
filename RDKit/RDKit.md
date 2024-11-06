1. Sometimes from `.sdf` file, number of bonds not correct (like C have 5).
Then use openbabel need to convert to `.xyz` and back to `.sdf` to let it be correct:
```bash
obabel -isdf input.sdf -oxyz -O input.xyz
obabel -ixyz input.xyz -osdf -O output.sdf
```

2. When using c++ rdkit on MacOS, one need to use ```bash brew install```, and at the same time modify the ` .rb ` file to turn on the static lib.

3. Remove atoms: 
```bash
# Given removed atom ids
remove_ids.sort(reverse=True)
edit_mol = Chem.EditableMol(mol)

for idx in remove_ids:
  edit_mol.RemoveAtom(idx)

new_mol = edit_mol.GetMol()
Chem.SanitizeMol(new_mol)
```

4. Remove atoms that with mapping: (Ref. https://sourceforge.net/p/rdkit/mailman/message/36699970/)
```bash
# very important! Mapped smiles always has extra H associate with C
# Allow implicit, otherwise after remove atom, it will generate radicals
for atom in mol.GetAtoms():
    atom.SetNoImplicit(False)

# Then remove atoms...

5. Some structure gives overlap of atoms by UFF, so try MMFF first. e.g. EmbedMultipleConfs + UFF for [N+](=O)([O-])c1c(cc(c(c1)OC)OC)N (EmbedMolecule + UFF/MMFF and EmbedMultipleConfs + MMFF is fine)
```
