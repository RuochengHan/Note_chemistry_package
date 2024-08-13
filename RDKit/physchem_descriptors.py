from rdkit import Chem
from rdkit.Chem import AllChem, rdmolops, Descriptors, rdMolDescriptors, Lipinski
from rdkit.Chem import Draw
from rdkit.Chem import rdPartialCharges
from rdkit.Chem.MolStandardize import rdMolStandardize
import numpy as np
import sys

def flattuple(tups):
    return tuple(set(tuple(x for tup in tups for x in tup)))

def ToCanonical(smi):
    mol = Chem.MolFromSmiles(smi)
    smi = Chem.MolToSmiles(mol)

    return smi

smis = ###

rds = []
for n, smi in enumerate(smis):

    smi = ToCanonical(smi)
    mol = Chem.MolFromSmiles(smi)
    #fp = Descriptors.CalcMolDescriptors(mol)
    #fp = rdMolDescriptors.GetMorganFingerprintAsBitVect(mol, radius=2, nBits=2048).ToBitString()
    #fps.append(fp)

    rd = []
    nha = Descriptors.NumHAcceptors(mol)
    nhd = Descriptors.NumHDonors(mol)
    sa = Descriptors.LabuteASA(mol)

    rd.append(Descriptors.MolLogP(mol))
    rd.append(Descriptors.TPSA(mol))
    rd.append(Descriptors.ExactMolWt(mol))
    rd.append(Descriptors.MolMR(mol))
    rd.append(nha)
    rd.append(nhd)
    rd.append(sa)
    rd.append(nha*np.sqrt(nhd)/sa)
    rd.append(nhd/Descriptors.ExactMolWt(mol))
    rd.append(Descriptors.NumRotatableBonds(mol))
    
    rd.append(Descriptors.NumAromaticRings(mol))
    rd.append(Descriptors.NumAliphaticRings(mol))
    rd.append(Descriptors.NumSaturatedRings(mol))
    rd.append(Descriptors.FractionCSP3(mol))

    rd.append(Descriptors.Chi0(mol))
    rd.append(Descriptors.Chi4n(mol))
    rd.append(Descriptors.Chi4v(mol))
    rd.append(Descriptors.Chi1(mol))
    rd.append(Descriptors.HallKierAlpha(mol))
    rd.append(Descriptors.Kappa1(mol))
    rd.append(Descriptors.Kappa2(mol))
    rd.append(Descriptors.Kappa3(mol))
    rd.append(Descriptors.PEOE_VSA3(mol))
    rd.append(Descriptors.SMR_VSA1(mol))
    rd.append(Descriptors.SlogP_VSA3(mol))

    rds.append(rd)


fw = open('physchem.dat', 'w+')
fw.write("smi\physchem\n")
for i,smi in enumerate(smis):
    fw.write(smi + "\t" + str(rds[i]) + "\n")
