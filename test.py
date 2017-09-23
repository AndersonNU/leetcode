import numpy as np
P = 100
count = 0
nsim = 100000
for j in range(nsim):
    for i in range(10000):
        U = np.random.uniform(0, 1)
        if U <= 0.5:
            P = P * 2
        else:
            P = 0
            count = count + i
            break
print(count/nsim)