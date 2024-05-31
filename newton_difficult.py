import math
from scipy.optimize import newton_krylov

def F(x):
    return [
        math.sin(x[0] * x[1])-0.51 * x[0] - 0.32 * x[1],
         x[1] * math.cos(x[0]*x[1]) - 0.51,
         ]

guess = [1,1]

sol = newton_krylov(F, guess, method='lgmres')

print(sol)

# [x, y] = [1.05799449 0.94744028]