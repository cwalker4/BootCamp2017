import numpy as np
import pdb

A = [[0.6, 0.1, -0.3],
     [0.5, -0.4, 0,2],
     [1.0, -0.2, 1.1]]

b = [[12],
     [10],
     [-1]]

A, b = map(np.asarray, (A, b))

x = np.array(([1],[2],[3]))

dp = A.dot(x) 
print(dp)

while True:
#    pdb.set_trace()
    print(np.dot(A, x))
    break 
    xn = np.add(np.dot(A,x), b)
    if np.amax(xn - x) < 1:
        break


