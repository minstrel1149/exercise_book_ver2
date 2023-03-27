#��������11�� 6.28
#1
data=np.array([89,74,91,88,72,84])
#2
xbar=np.mean(data);print(xbar)
var=np.var(data,ddof=1);print(var)
sd=np.std(data,ddof=1);print(sd)
sum=np.sum(data);print(sum)
n=data.size;print(n)
#3
import math
from scipy import stats
tval=(xbar-75)/(sd/math.sqrt(n));print(tval)
pval=2*(1-stats.t.cdf(tval,n-1));print(pval)
#4
tval=(xbar-90)/(sd/math.sqrt(n));print(tval)
pval=stats.t.cdf(tval,n-1);print(pval)

#5
se=stats.sem(data);print(se)
t_alpha=stats.t.ppf(1-0.05/2,n-1);print(t_alpha)
interval=t_alpha*se;print(interval)
CI=[xbar-interval,xbar+interval];print(CI)