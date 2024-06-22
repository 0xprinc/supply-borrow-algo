import numpy as np
from scipy.optimize import linprog

# Coefficients for the objective function

# Coefficients for the inequality constraints (lhs)
#     a1   a2  a3  b1  b2  b3  c1  c2  c3  c4  c5  c6  d1  d2  d3  x1  x2  x3  x4  x5  y1  y2  y3  y4  y5  z1  z2  z3
A = [[0,   0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  -1, -1,-1, -1, -1,  0,  0,  0,  0,  0,  0,  0,  0],
     [0,   0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,   0,  0, 0,  0,  0, -1, -1, -1, -1, -1,  0,  0,  0],
     [0,   0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,   0,  0, 0,  0,  0,  0,  0,  0,  0,  0, -1, -1, -1],
     [1,   1,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,   0,  0, 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
     [0,   0,  0,  1,  1,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,   0,  0, 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
     [0,   0,  0,  0,  0,  0,  1,  1,  1,  1,  1,  1,  0,  0,  0,   0,  0, 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
     [0,   0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  1,  1,   0,  0, 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
     [0,-0.8,  0,  0, 0,-0.8,  0,  0, 0,-0.8,  0,  0,  0, 0,-0.8,   1,  0, 0,  0,  0,  1,  0,  0,  0,  0,  0,  0,  1],
     [-0.8,0,  0,-0.8, 0,  0,  0,  0,  0,  0,-0.8, 0,  0,  0,  0,   0,  1, 0,  0,  0,  0,  0,  1,  0,  0,  1,  0,  0],
     [0,   0,-0.8, 0,-0.8, 0,  0,  0,  0,  0,  0,-0.8, 0,  0,  0,   0,  0, 1,  0,  0,  0,  1,  0,  0,  0,  0,  1,  0],
     [0,   0,  0,  0,  0,  0,-0.8, 0,  0,  0,  0,  0,  0,  0,  0,   0,  0, 0,  0,  0,  0,  0,  0,  1,  0,  0,  0,  0],
     [0,   0,  0,  0,  0,  0,  0,-0.8, 0,  0,  0,  0,  0,  0,  0,   0,  0, 0,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0],
     [0,   0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,-0.8, 0,  0,   0,  0, 0,  0,  1,  0,  0,  0,  0,  0,  0,  0,  0],
     [0,   0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,-0.8, 0,   0,  0, 0,  0,  0,  0,  0,  0,  0,  1,  0,  0,  0]]

# Constants for the inequality constraints (rhs)
m = 1000000

c = [0.0776, 0.0437, 0.0392, 0.0998, 0.0675, 0.0612, 0.0866, 0.0856, 0.0732, 0.0163, 0.0109, 0.0033, 0.0338, 0.0338, 0.0242, -0.0813, -0.0828, -0.0915, -0.1505, -0.1505, -0.0437, -0.0768, -0.0908, -0.1493, -0.1493, -0.019, -0.0169, -0.0246]
while (len(c)<len(A[0])):
    c.append(0)
for i in range(len(c)):
    c[i]*=-1;
b = [-2*m, -3*m, -10*m, m, 2.5*m, 9*m, 15*m, 1.4*m,0,0,0,0,0,0]

while len(b)<len(A):
    b.append(0)

# Bounds for variables (all variables >= 0)
x_bounds = [(0, np.inf) for _ in range(28)]

# Solve the linear programming problem
result = linprog(c, A_ub=A, b_ub=b, bounds=x_bounds, method='highs', options={'disp': True})

# Check if the optimization was successful
if result.success:
    optimized_values = result.x
    print("Optimized values:", optimized_values)
else:
    print("Optimization failed:", result.message)

