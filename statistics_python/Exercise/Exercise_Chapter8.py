
##연습문제

#6.23 (1)
import numpy as np
import statsmodels.api as sm

data = np.array([9.51,0.28,1.63,1.39,
                 1.58,3.04,1.49,1.79,
                 3.89,0.98])

sm.qqplot(data,line='s')

data_log =  np.log(data)
sm.qqplot(data_log,line='s')


#6.23 (2)
import numpy as np
import statsmodels.api as sm

data = np.array([314.46,361.81,36.23,
                 2253.48,21.57,7.94,
                 46.38,2.60,3.71,37.26])

sm.qqplot(data,line='s')

data_log =  np.log(data)
sm.qqplot(data_log,line='s')

#6.24(1)
import numpy as np
import statsmodels.api as sm

data = np.array([2.97,4.35,2.67,3.27,
                 1.75,4.27,4.19,2.67,
                 1.04,1.93])

sm.qqplot(data,line='s')

#6.24(2)
data = np.array([-0.19,-1.15,-1.63,-0.35,
                 0.96,0.43,-1.05,-0.77,-0.24,1.72])

sm.qqplot(data,line='s')


