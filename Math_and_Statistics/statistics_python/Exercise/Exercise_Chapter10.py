#�������� 10�� 5.38
#1
import numpy as np
height=np.array([163,161,168,161,157,162,153,159,164,170,
                 152,160,157,168,150,165,156,151,162,150,
                 156,152,161,165,168,167,165,168,159,156])
#2
xbar_h=np.mean(height);print(xbar_h)
var_h=np.var(height,ddof=1);print(var_h)
sd_h=np.std(height,ddof=1);print(sd_h)
median_h=np.median(height);print(median_h)
min_h=np.min(height);print(min_h)
max_h=np.max(height);print(max_h)
sum_h=np.sum(height);print(sum_h)
n=height.size;print(n)



#3
from scipy import stats
se_h=stats.sem(height);print(se_h)
z_alpha=stats.norm.ppf(1-0.03/2);print(z_alpha)
interval=z_alpha*se_h;print(interval)
CI=[xbar_h-interval,xbar_h+interval];print(CI)

#4
zval=(xbar_h-159)/se_h;print(zval)


#5
pval=2*(1-stats.norm.cdf(zval));print(pval)
