import numpy as np
import matplotlib.pyplot as plt

A = [[0.6, 0.1, -0.3],
     [0.5, -0.4, 0.2],
     [1.0, -0.2, 1.1]]

b = [[12],
     [10],
     [-1]]

A, b = map(np.asarray, (A, b))

# Problem 1:
from scipy.linalg import eigvals, solve
evs = eigvals(A)
ρ = max(abs(evs))
print(ρ)

# successive approximations:
x = [[3],
     [1],
     [-1]]

def equation(A, b, x):
    return np.dot(A, x) + b

while True:
    x = equation(A, b, x)
    if np.amax(np.absolute(x - equation(A, b, x))) < 1e-10:
        break
    
print(x)
        
# Problem 3:
c_vals = np.linspace(1, 2, 100)

beta = 0.96
wvec = np.array([[0.5],[1.0],[1.5]])
pvec = np.array([[0.2],[0.4],[0.4]])

def wage_equation(x, c, args):
    beta, wvec, pvec = args
    sum_term = 0
    for i in range(3):
        sum_term += max(wvec[i],x)*pvec[i]
    return c*(1-beta) + beta*sum_term

def get_rwage(x, c, args):
    beta, wvec, pvec = args
    rwage = wage_equation(x, c, args)
    while True:
        rwage = wage_equation(rwage, c, args)
        if abs(rwage - wage_equation(rwage, c, args)) < 1e-5:
            return rwage
      
    
rwvec = np.zeros(100)
for i in range(100):
    rwvec[i] = get_rwage(1, c_vals[i], args=(beta, wvec, pvec))

plt.figure(figsize=(14,10))
plt.plot(c_vals, rwvec)
plt.xlabel("Unemployment Compensation")
plt.ylabel("Reservation Wage")
plt.grid()
plt.show()
print(rwvec)


    


    


# In[ ]:



