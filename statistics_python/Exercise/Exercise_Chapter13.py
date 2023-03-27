
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels import regression
from scipy import stats
import pylab
from matplotlib import font_manager, rc, rcParams
font_name = font_manager.FontProperties(fname = 'C:/Windows/Fonts/malgun.ttf').get_name()
rc('font', family = font_name, size = 10)
rcParams['axes.unicode_minus'] = False

# 13장_2.1
x_1 = [1,4]
y_1 = [5,11]
plt.plot(x_1, y_1, 'b')
plt.xlabel('C1')
plt.ylabel('C2')

# 13장_2.2
x_2 = [0,3]
y_2 = [10,1]
plt.plot(x_2, y_2, 'o')
plt.plot(x_2, y_2, 'b')
plt.xlabel('x')
plt.ylabel('y')
plt.xlim([0,8])

# 13장_3.1
x_4 = [1, 2, 3, 4, 5]
y_4 = [0.9, 2.1, 2.5, 3.3, 3.8]
slope_1, intercept_1 = np.polyfit(x_4, y_4, 1)
abline_values_1 = [slope_1 * i + intercept_1 for i in x_4]
plt.plot(x_4, y_4, 'o')
plt.plot(x_4, abline_values_1, 'b')
plt.xlabel('X')
plt.ylabel('FITS1')

# 13장 3.2
x_5 = [0, 1, 6, 3, 5]
y_5 = [4, 3, 0, 2, 1]
slope_2, intercept_2 = np.polyfit(x_5, y_5, 1)
abline_values_2 = [slope_2 * i + intercept_2 for i in x_5]
plt.plot(x_5, y_5, 'o')
plt.plot(x_5, abline_values_2, 'b')
plt.xlabel('X')
plt.ylabel('Y')

# 13장 3.3
x_6 = [0, 3, 5, 8, 9]
y_6 = [1, 2, 4, 3, 5]
slope_3, intercept_3 = np.polyfit(x_6, y_6, 1)
abline_values_3 = [slope_3 * i + intercept_3 for i in x_6]
plt.plot(x_6, y_6, 'o')
plt.plot(x_6, abline_values_3, 'b')
plt.xlabel('X')
plt.ylabel('Y')

# 13장 3.4
x_7 = [1, 2, 3, 5, 6, 7]
y_7 = [4, 6, 3, 1, 3, 1]
slope_4, intercept_4 = np.polyfit(x_7, y_7, 1)
abline_values_4 = [slope_4 * i + intercept_4 for i in x_7]
plt.plot(x_7, y_7, 'o')
plt.plot(x_7, abline_values_4, 'b')
plt.xlabel('X')
plt.ylabel('Y')

# 13장 3.5 - (1)
x_8 = [0, 1, 6, 3, 5]
y_8 = [4, 3, 0, 2, 1]
slope_5, intercept_5 = np.polyfit(x_8, y_8, 1)
abline_values_5 = [slope_5 * i + intercept_5 for i in x_8]
plt.plot(x_8, y_8, 'o')
plt.xlabel('X')
plt.ylabel('Y')

# 13장 3.5 - (4)
plt.plot(x_8, y_8, 'o')
plt.plot(x_8, abline_values_5, 'b')
plt.xlabel('X')
plt.ylabel('Y')

# 13장 3.6 - (1)
x_9 = [1, 2, 3, 3, 4, 5]
y_9 = [9, 5, 6, 3, 3, 1]
slope_6, intercept_6 = np.polyfit(x_9, y_9, 1)
abline_values_6 = [slope_6 * i + intercept_6 for i in x_9]
plt.plot(x_9, y_9, 'o')
plt.xlabel('X')
plt.ylabel('Y')

# 13장 3.6 - (4)
plt.plot(x_9, y_9, 'o')
plt.plot(x_9, abline_values_6, 'b')
plt.xlabel('X')
plt.ylabel('Y')

# 13장 4.4 - (1)
x_10 = [200.8, 194.6, 183.5, 190.5, 210.2, 170.5, 220.0]
y_10 = [207.0, 199.0, 188.0, 191.2, 211.0, 176.2, 218.0]
slope_7, intercept_7 = np.polyfit(x_10, y_10, 1)
abline_values_7 = [slope_7 * i + intercept_7 for i in x_10]
plt.plot(x_10, y_10, 'o')
plt.plot(x_10, abline_values_7, 'b')
plt.xlabel('X')
plt.ylabel('Y')

# 13장 4.8 - (1)
x_11 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 ,13 ,14 ,15]
y_11 = [355, 211, 197, 166, 142, 106, 104, 60, 56, 38, 36, 32, 21, 19, 15]
slope_8, intercept_8 = np.polyfit(x_11, y_11, 1)
abline_values_8 = [slope_8 * i + intercept_8 for i in x_11]
plt.plot(x_11, y_11, 'o')
plt.plot(x_11, abline_values_8, 'b')
plt.xlabel('X')
plt.ylabel('Y')

# 13장 4.9 - (1)
x_12 = [0, 1, 2, 3, 4]
y_12 = [195, 216, 244, 260, 284]
slope_9, intercept_9 = np.polyfit(x_12, y_12, 1)
abline_values_9 = [slope_9 * i + intercept_9 for i in x_12]
plt.plot(x_12, y_12, 'o')
plt.plot(x_12, abline_values_9, 'b')
plt.xlabel('X')
plt.ylabel('Y')

# 13장 6.1
y_hat_1 = [11.3, 14.8, 18.4, 22.0, 25.5, 27.0, 31.2, 32.7,
           34.1, 36.2, 39.8, 43.4, 45.5, 46.2, 46.9, 46.9]
e_1 = [-0.3, 0.2, -5.4, 2.0, 0.5, 5.0, -9.2, 6.3,
       12.9, -4.2, -14.8, 7.6, -1.5, 15.8, 1.1, -16.9]
plt.plot(y_hat_1, e_1, 'o')
plt.xlabel('y_fit')
plt.ylabel('e')

# 13장 6.2
y_hat_2 = [4.01, 5.53, 6.21, 6.58, 8.17, 8.34, 8.81, 9.62,
           10.05, 10.55, 10.77, 10.77, 10.94, 10.98, 10.98]
e_2 = [0.28, -0.33, -0.21, 0.24, -0.97, 0.46, 0.79, -1.02,
       1.35, -1.55, 0.63, 1.73, -2.14, 1.92, -1.18]
plt.plot(y_hat_2, e_2, 'o')
plt.xlabel('y_fit')
plt.ylabel('e')

# 13장 6.3 - (1), (2)
C_23 = [2.2, 3.1, 2.5, 3.3, 2.3, 3.6, 2.6, 2.5,
        3.0, 3.2, 2.9, 3.3, 2.7, 3.2]
C_24 = [-1, -2, 3, -3, -1, 5, 0, 0, 3, -2, 2, -5, 0, 1]
C_25 = [9, 6, 13, 1, 7, 14, 8, 3, 12, 4, 11, 2, 10, 5]
plt.plot(C_23, C_24, 'o')
plt.xlabel('C23')
plt.ylabel('C24')
plt.plot(C_25, C_24, 'o')
plt.xlabel('C25')
plt.ylabel('C24')

# 13장 6.4
time = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
        14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
y_111 = [300.9, 323.7, 324.1, 355.3, 383.4, 395.1, 412.8, 407.0,
         438.0, 446.1, 452.5, 447.3, 475.9, 487.7, 497.2, 529.8,
         551, 581.1, 617.8, 658.1, 675.2, 706.6, 725.6, 722.5,
         745.4, 790.7]
y_hat_111 = [283.1, 301.9, 320.6, 339.4, 358.2, 376.9, 395.7, 414.5,
             433.2, 52.0, 470.8, 489.5, 508.3, 527.1, 545.8, 564.6,
             583.4, 602.1, 620.9, 639.7, 658.4, 677.2, 696.0, 714.7,
             733.5, 752.3]
res_1 = [26.8, 21.8, 3.5, 15.9, 25.2, 18.2, 17.1, -7.5,
         4.8, -5.9, -18.3, -42.2, -32.4, -39.4, -48.6, -34.8,
         -32.4, -21.0, -3.1, 18.4, 16.8, 29.4, 29.6, 7.8,
         11.9, 38.4]
plt.plot(y_hat_111, res_1, 'o')
plt.xlabel('y_fit')
plt.ylabel('e')
plt.plot(time, res_1, 'o')
plt.xlabel('time')
plt.ylabel('e')

# 13장 7.1
x_13 = [1, 1, 1, 2, 3, 3, 4, 5, 5]
y_13 = [9, 7, 8, 10, 15, 12, 19, 24, 21]
slope_10, intercept_10 = np.polyfit(x_13, y_13, 1)
abline_values_10 = [slope_10 * i + intercept_10 for i in x_13]
plt.plot(x_13, y_13, 'o')
plt.plot(x_13, abline_values_10, 'b')
plt.xlabel('X')
plt.ylabel('Y')

# 13장 7.6 - (1)
x_14 = [0.257, 0.295, 0.284, 0.272, 0.277, 0.245, 0.255,
        0.284, 0.265, 0.302, 0.241, 0.310, 0.239]
y_14 = [1.35, 1.50, 1.33, 1.39, 1.28, 1.06, 1.32,
        1.23, 1.15, 1.35, 1.08, 1.20, 1.15]
slope_11, intercept_11 = np.polyfit(x_14, y_14, 1)
abline_values_11 = [slope_11 * i + intercept_11 for i in x_14]
plt.plot(x_14, y_14, 'o')
plt.plot(x_14, abline_values_11, 'b')
plt.xlabel('X')
plt.ylabel('Y')

fit_2 = sm.OLS(y_14, x_14).fit()
res_2 = statsmodels.regression.linear_model.RegressionResults.resid(fit_2)
oring =
plt.plot(res_2, ., 'o')

# 13장 7.8 - (1)
x_15 = [1, 2, 2, 3, 3, 4, 6, 7, 8, 10]
y_15 = [5.45, 4.80, 5.00, 4.00, 3.70, 3.20, 3.15, 2.69, 1.90, 1.47]
slope_12, intercept_12 = np.polyfit(x_15, y_15, 1)
abline_values_12 = [slope_12 * i + intercept_12 for i in x_15]
plt.plot(x_15, y_15, 'o')
plt.plot(x_15, abline_values_12, 'b')
plt.xlabel('X')
plt.ylabel('Y')

# 13장 7.14 - (1)
x_16 = [346, 272, 276, 350, 345, 304, 311, 338, 344, 346,
        272, 276, 239, 254, 238, 304, 311, 338, 344, 346, 272, 276]
y_16 = [45, 20, 20, 65, 65, 20, 30, 30, 55, 55,
        30, 30, 20, 20, 20, 30, 45, 45, 65, 65, 45, 40]
slope_13, intercept_13 = np.polyfit(x_16, y_16, 1)
abline_values_13 = [slope_13 * i + intercept_13 for i in x_16]
plt.plot(x_16, y_16, 'o')
plt.plot(x_16, abline_values_13, 'b')
plt.xlabel('X')
plt.ylabel('Y')

# 13장 7.14 - (6)

df_1 = {'x_16' : x_16, 'y_16' : y_16}
dat_1 = pd.DataFrame(data = df_1)
result_1 = smf.ols('y_16 ~ x_16', df_1).fit()
res_3 = result_1.resid
pred_1 = result_1.predict(df_1)
plt.plot(pred_1, res_3, 'o')



# 13장 7.19 - (1)
x_17 = [100, 260, 360, 360, 400, 650, 1000, 1600]
y_17 = [22, 21, 26, 17, 18, 10, 12, 8]
slope_14, intercept_14 = np.polyfit(x_17, y_17, 1)
abline_values_14 = [slope_14 * i + intercept_14 for i in x_17]
plt.plot(x_17, y_17, 'o')
plt.plot(x_17, abline_values_14, 'b')
plt.xlabel('X')
plt.ylabel('Y')

# 13장 7.19 - (2)
df_2 = {'x_17' : x_17, 'y_17' : y_17}
dat_2 = pd.DataFrame(data = df_2)
result_2 = smf.ols('y_17 ~ x_17', df_2).fit()
res_4 = result_2.resid
pred_2 = result_2.predict(df_2)
plt.plot(pred_2, res_4, 'o')
plt.plot(pred_2, [0, 0, 0, 0, 0, 0, 0, 0], ":")
plt.xlabel('Fitted Value')
plt.ylabel('Residual')
plt.title('Residuals Versus Fitted Values')

# 13장 7.20 - (1)
x_17 = [100, 260, 360, 360, 400, 650, 1000, 1600]
log_x_17 = [math.log10(100), math.log10(260),
            math.log10(360), math.log10(360),
            math.log10(400), math.log10(650),
            math.log10(1000), math.log10(1600)]
y_17 = [22, 21, 26, 17, 18, 10, 12, 8]
slope_14, intercept_14 = np.polyfit(log_x_17, y_17, 1)
abline_values_14 = [slope_14 * i + intercept_14 for i in log_x_17]
plt.plot(log_x_17, y_17, 'o')
plt.plot(log_x_17, abline_values_14, 'b')
plt.xlabel('X')
plt.ylabel('Y')

# 13장 7.20 - (2)
df_2 = {'log_x_17' : log_x_17, 'y_17' : y_17}
dat_2 = pd.DataFrame(data = df_2)
result_2 = smf.ols('y_17 ~ log_x_17', df_2).fit()
res_4 = result_2.resid
pred_2 = result_2.predict(df_2)
plt.plot(pred_2, res_4, 'o')
plt.plot(pred_2, [0, 0, 0, 0, 0, 0, 0, 0], ":")
plt.xlabel('Fitted Value')
plt.ylabel('Residual')
plt.title('Residuals Versus Fitted Values')

# 13장 7.25
x_18 = [1, 2, 2, 3, 3, 4, 6, 7, 8, 10]
y_18 = [5.45, 4.80, 5.00, 4.00, 3.70, 3.20, 3.15, 2.69, 1.90, 1.47]
dss = {'x_18' : x_18, 'y_18' : y_18}
datt = pd.DataFrame(data = dss)
fit_3 = smf.ols('y_18 ~ x_18', data=datt).fit()
print(fit_3.summary())