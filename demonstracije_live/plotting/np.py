import matplotlib.pyplot as plt
import numpy as np

x_koordinate = np.arange(-5,5,0.5)
y_koordinate = -x_koordinate**2
print(x_koordinate)
print(y_koordinate)




plt.plot(x_koordinate,y_koordinate)
plt.plot(x_koordinate,-y_koordinate)
plt.show()

