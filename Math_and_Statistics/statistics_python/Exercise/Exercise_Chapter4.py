#Practice chapter 4

#3.1
import numpy as np
import matplotlib.pyplot as plt

x_3_1 = np.array([0,1,6,3,5])
y_3_1 = np.array([4,3,0,2,1])

plt.figure()
plt.scatter(x_3_1, y_3_1, color ='black')
plt.xlabel('x')
plt.ylabel('y')

plt.show()

#3.2
import numpy as np
import matplotlib.pyplot as plt

x_3_2 = np.array([1,3,2,4,5])
y_3_2 = np.array([1,1,3,4,6])

plt.figure()
plt.scatter(x_3_2, y_3_2, color ='black')
plt.xlabel('x')
plt.ylabel('y')

plt.show()

#3.3
import numpy as np
import matplotlib.pyplot as plt

height_3_3 = np.array([165,170,167,166,165,168,167,170,167,175,170,166,172,170,172,175,172])
weight_3_3 = np.array([51,54,52,53,52,56,56,52,52,61,56,49,54,53,54,56,53])

plt.figure()
plt.scatter(height_3_3, weight_3_3, color ='black')
plt.xlabel('height')
plt.ylabel('weight')

plt.show()

#3.4
import numpy as np
import matplotlib.pyplot as plt

hydrogen_3_4 = np.array([120,82,90,8,38,20,2.8,66,2.0,20,85])
carbon_3_4 = np.array([105,110,99,22,50,50,7.3,74,7.7,45,51])

plt.figure()
plt.scatter(hydrogen_3_4, carbon_3_4, color ='black')
plt.xlabel('hydrogen(ppm)')
plt.ylabel('carbon(ppm)')

plt.show()

#3.5
import numpy as np
import matplotlib.pyplot as plt

midscore_3_5 = np.array([81,75,71,61,96,56,85,18,88,79,77,68,70,77,71,91])
finalscore_3_5 = np.array([80,82,83,57,100,30,68,56,82,57,75,47,40,87,65,86])

plt.figure()
plt.scatter(midscore_3_5, finalscore_3_5, color ='black')
plt.xlabel('midscore')
plt.ylabel('finalscore')

plt.show()

#5.8 (1)
import numpy as np
import matplotlib.pyplot as plt

x_5_8_1 = np.array([-1,3,1,5,2])
y_5_8_1 = np.array([2,4,0,6,3])

plt.figure()
plt.scatter(x_5_8_1, y_5_8_1, color ='black')
plt.xlabel('x')
plt.ylabel('y')

plt.show()

#5.8 (2)
import numpy as np
import matplotlib.pyplot as plt

x_5_8_2 = np.array([-1,3,1,5,2])
y_5_8_2 = np.array([6,0,3,2,4])

plt.figure()
plt.scatter(x_5_8_2, y_5_8_2, color ='black')
plt.xlabel('x')
plt.ylabel('y')

plt.show()

#5.9 (1)
import numpy as np
import matplotlib.pyplot as plt

x_5_9 = np.array([-1,3,6,5,2,7])
y_5_9 = np.array([5,4,4,2,7,2])

plt.figure()
plt.scatter(x_5_9, y_5_9, color ='black')
plt.xlabel('x')
plt.ylabel('y')

plt.show()

#5.10 (2)
import numpy as np
import matplotlib.pyplot as plt

x_5_10 = np.array([1,3,4,7,9,12,13,14])
y_5_10 = np.array([3.5,2.4,2.1,1.3,1.2,2.2,2.6,4.2])

plt.figure()
plt.scatter(x_5_10, y_5_10, color ='black')
plt.xlabel('x')
plt.ylabel('y')

plt.show()

#5.12 (1)
import numpy as np
import matplotlib.pyplot as plt

x_5_12 = np.array([6,7,5,21,13,5,13,14])
y_5_12 = np.array([28,23,29,22,20,19,28,19])

plt.figure()
plt.scatter(x_5_12, y_5_12, color ='black')
plt.xlabel('emotion index')
plt.ylabel('vigor index')

plt.show()

#5.13 (1)
import numpy as np
import matplotlib.pyplot as plt

x_5_13 = np.array([167,167,167,170,175,157,167,167,157,165,157,165])
y_5_13 = np.array([52,53,62,63,63,49,65,58,49,58,49,61])

plt.figure()
plt.scatter(x_5_13, y_5_13, color ='black')
plt.xlabel('height')
plt.ylabel('weight')

plt.show()

#5.14 (1)
import numpy as np
import matplotlib.pyplot as plt

x_5_14 = np.array([12.2,14.3,15.7,12.6,13.5,14.0])
y_5_14 = np.array([8.5,9.9,10.7,9.0,9.3,9.5])

plt.figure()
plt.scatter(x_5_14, y_5_14, color ='black')
plt.xlabel('average tar content')
plt.ylabel('average number of inhalations')

plt.show()

#5.17
import numpy as np
x_5_17 = np.array([8.7,9,11,8.5,9.2,12,12,18])
y_5_17 = np.array([25,25,26,48,65,87,90,100])

np.corrcoef(x_5_17,y_5_17)[1][0]

import matplotlib.pyplot as plt

plt.figure()
plt.scatter(x_5_17, y_5_17, color ='black')
plt.xlabel('x(magnesium)')
plt.ylabel('y(taste)')
plt.title('x(magnesium) and y(taste)')

plt.show()

#5.18
import numpy as np

x_5_18 = np.array([41,39,53,67,61,67,46,50,55,72,63,59,
                   53,62,65,48,32,64,59,54,52,64,51,62,
                   56,38,52,40,65,61,64,64,53,51,58,65])
y_5_18 = np.array([29,19,30,27,28,27,22,29,24,33,25,20,
                   28,22,27,22,27,28,30,29,21,26,20,29,
                   34,21,25,24,32,29,27,26,24,25,34,28])

np.corrcoef(x_5_18,y_5_18)[1][0]

import matplotlib.pyplot as plt

plt.figure()
plt.scatter(x_5_18, y_5_18, color ='black')
plt.xlabel('x(math)')
plt.ylabel('y(social science)')
plt.title('x(math) and y(social science)')

plt.show()