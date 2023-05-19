# 연습문제 ==========================================================================

# 12장 5.33_1
x = [15, 20, 11, 23, 16, 21, 18, 16, 27, 24]
y = [23, 31, 13, 19, 23, 17, 28, 16, 25, 28]

# 12장 5.33_2
import numpy as np
import math
var1 = np.var(x, ddof=1); print(var1)
var2 = np.var(y, ddof=1); print(var2)
n1 = len(x); print(n1)
n2 = len(y); print(n2)
var = (((n1 - 1) * var1 + (n2 - 1) * var2)) / (n1 + n2 - 2); print(var)
se = math.sqrt(var1/n1 + var2/n2); print(se)

# 12장 5.33_3
import scipy.stats as stats
import math
t_alpha = stats.t.ppf(1 - 0.03 / 2, n1 + n2 - 2); print(t_alpha)
interval_t = t_alpha * se; print(interval_t)
xbar1 = np.mean(x); print(xbar1)
xbar2 = np.mean(y); print(xbar2)
diff = xbar1 - xbar2; print(diff)
CI_2 = [diff - interval_t, diff + interval_t]; print(CI_2)

# 12장 5.34_1
import numpy as np
x = np.array([[33, 40, 55, 41, 62, 54, 40, 35, 59, 56],
              [35, 48, 65, 33, 61, 54, 49, 37, 58, 65]])
d = np.diff(x, axis = 0); print(d)

# 12장 5.34_2
dbar = np.mean(d); print(dbar)
var = np.var(d, ddof = 1); print(var)
sd = np.std(d, ddof = 1); print(sd)
n = d.size; print(n)

# 12장 5.34_3
import scipy.stats as stats
import math
se = sd / math.sqrt(n); print(se)
t_alpha = stats.t.ppf(1 - 0.02/2, n - 1); print(t_alpha)
t_alpha * se
interval_t = t_alpha * se
CI_3 = [dbar - interval_t, dbar + interval_t]; print(CI_3)

# 12장 5.34_4
import numpy as np
x = np.array([[138, 87, 110, 132, 96, 120, 86, 90, 129, 100],
              [140, 90, 125, 130, 95, 121, 85, 97, 131, 110]])
d = np.diff(x, axis = 0); print(d)

# 12장 5.34_5
dbar = np.mean(d); print(dbar)
var = np.var(d, ddof = 1); print(var)
sd = np.std(d, ddof = 1); print(sd)
n = d.size; print(n)

# 12장 5.34_6
import scipy.stats as stats
import math
se = sd / math.sqrt(n); print(se)
t_alpha = stats.t.ppf(1 - 0.1/2, n - 1); print(t_alpha)
t_alpha * se
interval_t = t_alpha * se
CI_4 = [dbar - interval_t, dbar + interval_t]; print(CI_4)