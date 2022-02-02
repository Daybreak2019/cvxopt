import math
from cvxopt import base, blas, lapack, cholmod, misc_solvers
from cvxopt.base import matrix, spmatrix

A = spmatrix([10, 3, 5, -2, 5, 2], [0, 2, 1, 3, 2, 3], [0, 0, 1, 1, 2, 3])
X = spmatrix(1.0,range(4),range(4))

F = cholmod.symbolic(A)
cholmod.numeric(A, F)

cholmod.spsolve(F, X)
