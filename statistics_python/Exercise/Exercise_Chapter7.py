#Practice chapter 7

#3.4, p=0.2
import numpy as np
import matplotlib.pyplot as plt

n=5
num_samples = 10000

a=np.random.binomial(n,0.2,size=num_samples)
b=np.bincount(a,minlength=n+1)
p=b/float(b.sum())
plt.bar(np.arange(len(b))+0.5, p, width=1, facecolor='blue')
plt.xlim(0, n + 1)

plt.show()

#3.4, p=0.5
import numpy as np
import matplotlib.pyplot as plt

n=5
num_samples = 100000000

a=np.random.binomial(n,0.5,size=num_samples)
b=np.bincount(a,minlength=n+1)
p=b/float(b.sum())
plt.bar(np.arange(len(b))+0.5, p, width=1, facecolor='blue')
plt.xlim(0, n + 1)

plt.show()

#3.4, p=0.8
import numpy as np
import matplotlib.pyplot as plt

n=5
num_samples = 10000

a=np.random.binomial(n,0.8,size=num_samples)
b=np.bincount(a,minlength=n+1)
p=b/float(b.sum())
plt.bar(np.arange(len(b))+0.5, p, width=1, facecolor='blue')
plt.xlim(0, n + 1)

plt.show()

#6.16, (2)
import numpy as np
import matplotlib.pyplot as plt

n=5
num_samples = 10000

a=np.random.binomial(n,0.4,size=num_samples)
b=np.bincount(a,minlength=n+1)
p=b/float(b.sum())
plt.bar(np.arange(len(b))+0.5, p, width=1, facecolor='blue')
plt.xlim(0, n + 1)

plt.show()

#6.34
#(1)
from scipy import stats

stats.binom.cdf(8,12,0.64)
stats.binom.pmf(8,12,0.64)

#(2)
from scipy import stats

stats.binom.cdf(15,30,0.42)-stats.binom.cdf(9,30,0.42)