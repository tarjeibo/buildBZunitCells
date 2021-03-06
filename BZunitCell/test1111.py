from __future__ import division
from ase.visualize import *
from numpy import sqrt
import numpy as np
from numpy import identity
from ase import Atoms
from ase import Atom
import ase
from ase.build import stack
from shutil import move
from os import rename


#Define BZ unit cell, with lattice parameter
atoms = Atoms('2Ba', [(0, 0, 0), (0.5, 0.5, 0.5)])
a_0 = 4.1972899437
cell = a_0*identity(3)
atoms.set_cell(cell, scale_atoms=True)
unitCell = atoms.get_cell()



atomsLeft = Atoms(atoms)
atomsRight = Atoms(atoms)
atomsRight.rotate((0, 0, np.pi/12), rotate_cell = True)

print atomsLeft.get_positions()
print atomsRight.get_positions()
print atomsLeft.get_cell()
print atomsRight.get_cell()

stackedAtoms = stack(atomsLeft, atomsLeft, axis=0, cell=None, fix=0, maxstrain=None)
stackedAtoms = stack(stackedAtoms, atomsLeft, axis=0, cell=None, fix=0, maxstrain=None)
stackedAtoms = stack(stackedAtoms, atomsRight, axis=0, cell=None, fix=0, maxstrain=None)
stackedAtoms = stack(stackedAtoms, atomsRight, axis=0, cell=None, fix=0, maxstrain=None)
stackedAtoms = stack(stackedAtoms, atomsRight, axis=0, cell=None, fix=0, maxstrain=None)


write("BZ1111.vasp", atomsLeft)
write("BZ1111_rotated.vasp", stackedAtoms)
#move("/BZ1111_rotated.vasp", "/vaspFiles/BZ1111_rotated.vasp")
os.rename('BZ1111_rotated.vasp', "/vaspFiles/BZ1111_rotated.vasp")
'''
atomsStacked = stack(atomsLeft, atomsRight, axis=0, cell=None, fix=0.5, maxstrain=None)
atomsStackRotated = Atoms(atomsStacked)
#Rotation about the center of the unit cell
atomsStackRotated.rotate((0, 0, np.pi/48), rotate_cell=True)
#print atomsStackRotated.get_positions()
superStack = stack(atomsStacked, atomsStackRotated, axis=0, cell=None, fix=0.5, maxstrain=None)
'''
