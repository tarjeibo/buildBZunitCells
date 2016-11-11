from __future__ import division
from ase.visualize import *
from numpy import sqrt
import numpy as np
from numpy import identity
from ase import Atoms
from ase import Atom
import ase
from ase.build import stack

#Define BZ unit cell, with lattice parameter
atoms = Atoms('BaZrOOO', [(0.5, 0.5, 0.5), (0, 0, 0), (0.5, 0, 0), (0, 0.5, 0), (0, 0, 0.5)])
a_0 = 4.1972899437
cell = a_0*identity(3)
atoms.set_cell(cell, scale_atoms=True)


write("BZ1011.vasp", atoms)

atomsLeft = Atoms(atoms)
atomsRight = Atoms(atoms)
#atomsRight.rotate((0, 0, np.pi/6), rotate_cell=True)



atomsStacked = stack(atomsLeft, atomsRight, axis=0, cell=None, fix=0.5, maxstrain=None)
atomsStacked = stack(atomsStacked, atomsStacked, axis=0, cell=None, fix=0.5, maxstrain=None)
atomsStackRotated = Atoms(atomsStacked)
#Rotation about the center of the unit cell
atomsStackRotated.rotate((0, 0, np.pi/6), center=(0,0,0))
#print atomsStackRotated.get_positions()
superStack = stack(atomsStacked, atomsStackRotated, axis=0, cell=None, fix=0.5, maxstrain=None)

write("BZ_rotated.vasp", superStack)
