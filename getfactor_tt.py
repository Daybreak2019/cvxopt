import math
from cvxopt import base, blas, lapack, cholmod, misc_solvers
from cvxopt.base import matrix, spmatrix

def GetF ():
   A = spmatrix([10, 3, 5, -2, 5, 2], [0, 2, 1, 3, 2, 3], [0, 0, 1, 1, 2, 3])
   Fn = cholmod.symbolic(A)
   cholmod.numeric(A, Fn)
   return Fn

F = GetF ()

cholmod.getfactor(F)
