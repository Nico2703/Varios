import matplotlib.pyplot as plt
import numpy as np
x = np.arange(-8*np.pi,8*np.pi,0.1)
y = (np.sin(x))/x
plt.plot(x,y)
plt.show()