## Compile install
```bash
conda install -y cmake cairo pillow eigen pkg-config
conda install -y boost-cpp boost

```

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
```

5. Some structure gives overlap of atoms by UFF, so try MMFF first. e.g. EmbedMultipleConfs + UFF for [N+](=O)([O-])c1c(cc(c(c1)OC)OC)N (EmbedMolecule + UFF/MMFF and EmbedMultipleConfs + MMFF is fine)

6. In EmbedMultipleConfs, useBasicKnowledge=True can not embed endocycle molecule, use useBasicKnowledge=False

7. When removing atom formal charge, need to reset ExplicitHs, otherwise cause Sanitize error, e.g. Explicit valence for atom # ... is greater than permitted
```python
for atom in mol.GetAtoms():
    if atom.GetFormalCharge() != 0:
        atom.SetFormalCharge(0)
        # otherwise cause Sanitize error
        atom.SetNumExplicitHs(0)
```

8. when loading sdf with given Hs:
```python
# otherwise Hs are removed
suppl = Chem.SDMolSupplier(finp, removeHs=False)
```

9. After copy a mol, remember to sanitize it.
```python
mol = Chem.Mol(prod_mol)
Chem.SanitizeMol(mol)
# Or the following
# mol.updatePropertyCache(); it just calculates valence states of the atoms. There are no topology changes.
# https://github.com/rdkit/rdkit/issues/1596
#mol.UpdatePropertyCache()
```
Otherwise will have error
```bash
Pre-condition Violation getNumImplicitHs() called without preceding call to calcImplicitValence()
```

10. In the case of several colors on the image, Draw.MolToImage not work (seems highlightAtomColors highlightAtomColors no logner supported), need to use rdMolDraw2D.PrepareAndDrawMolecule
```python
# Use the MolDraw2DSVG drawer
drawer = rdMolDraw2D.MolDraw2DSVG(350, 350)

# The highlight colors are provided directly to the drawer
drawer.drawOptions().highlightBondColors = {
    0: (0, 0, 1),    # Blue
    1: (0, 0.5, 0)   # Green
}

bondcolors = {
    0: (0, 0, 1),    # Blue
    1: (0, 0.5, 0)   # Green
}

rdMolDraw2D.PrepareAndDrawMolecule(drawer, mol, 
                                   highlightBonds=[0,1],
                                   highlightBondColors=bondcolors)

#drawer.DrawMolecule(mol, highlightBonds=[0, 1])
drawer.FinishDrawing()

# Get the image as SVG text and save it
svg = drawer.GetDrawingText()
with open('test_alternative_drawing.svg', 'w') as f:
    f.write(svg)

# 3. Get the SVG data as a string
svg_data = drawer.GetDrawingText()

# 4. Convert the SVG string to a PNG file
cairosvg.svg2png(bytestring=svg_data.encode('utf-8'), write_to="molecule_drawing.png")

print("Image successfully saved as 'molecule_drawing.png'")
```

11. SetProp('atomNote',str(idx)) for indices in rdMolDraw2D
```python
    # Find atoms in highlighted bonds
    highlight_bond_atoms = set()

    for typ, atoms, v, dE in unstables:
        if dE > e_thres:
            if typ == "Torsion" and len(atoms) == 4:
                for a1, a2 in zip(atoms[:3], atoms[1:4]):
                    bond = mol.GetBondBetweenAtoms(a1, a2)
                    if bond:
                        highlight_bonds.add(bond.GetIdx())
                        bond_colors[bond.GetIdx()] = (0, 1, 1)
                        highlight_bond_atoms.add(a1)
                        highlight_bond_atoms.add(a2)
            elif typ in ("ES", "VdW"):
                for idx in atoms:
                    highlight_atoms.add(idx)
                    atom_colors[idx] = (1, 0.5, 0)

    # Union of all atoms to label
    atoms_to_label = highlight_atoms | highlight_bond_atoms

    # Prepare atomLabels dictionary
    #atomLabels = {idx: str(idx) for idx in atoms_to_label}
    #atomLabels = {0: 'Si'}


    [mol.GetAtomWithIdx(idx).SetProp('atomNote',str(idx)) for idx in atoms_to_label]


    # Create SVG drawer
    drawer = rdMolDraw2D.MolDraw2DSVG(600, 600)
    # Enable atom indices display
    opts = drawer.drawOptions()
    #opts.addAtomIndices = True # for all indices

    opts.annotationFontScale = 0.75
    #opts.minFontSize = 48 # not work
    drawer.SetFontSize(20)
    #print(drawer.FontSize())

    rdMolDraw2D.PrepareAndDrawMolecule(
        drawer, 
        mol, 
        highlightAtoms=list(highlight_atoms),
        highlightBonds=list(highlight_bonds),
        highlightAtomColors=atom_colors,
        highlightBondColors=bond_colors
        #atomLabels=atomLabels # not work
    )
    drawer.FinishDrawing()
    svg = drawer.GetDrawingText()
```
