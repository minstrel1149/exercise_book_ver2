##연습문제4.17
import numpy as np
m = []
for i in range(100):
    np.random.seed(i)
    sample=np.random.poisson(lam = 3, size = 9)
    m.append(np.mean(sample))

m = np.array(m)
print (np.round(m,4))

np.mean(m)
np.std(m,ddof=1)
np.sqrt(3)/3
##히스토그램

import matplotlib.pyplot as plt
plt.hist(m, bins=7)
plt.show()

#정규 확률 그림
import matplotlib.pyplot as plt
sm.qqplot(m,line='s')

np.random.seed(1)
sample = np.random.poisson(lam=3, size=9)
m.append(np.mean(sample))
