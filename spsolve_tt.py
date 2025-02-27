import math
from cvxopt import base, blas, lapack, cholmod, misc_solvers
from cvxopt.base import matrix, spmatrix

def Compute (F):
    X = spmatrix(1.0,range(4),range(4))
    cholmod.spsolve(F, X)
    
A = spmatrix([10, 3, 5, -2, 5, 2], [0, 2, 1, 3, 2, 3], [0, 0, 1, 1, 2, 3])
F = cholmod.symbolic(A)
cholmod.numeric(A, F)

Compute (F)
