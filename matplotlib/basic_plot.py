###Basic stuff
import numpy as np
import matplotlib.pyplot as plt


range = (-100,100)
#generiramo 10 brojeva od 0 do 5 jednako razdaljenih
x_1 = np.linspace(range[0],range[1],20)
# note the matrix operacija dolje
func = lambda a:a**2+a*4+5
y_1 = func(x_1)
#kada se plt.plot zove sam po sebi, crtamo graf
plt.plot(x_1,y_1)
plt.title("a^2+(a*4)+5*a")
plt.xlabel("horizontal")
plt.ylabel("vertical")
plt.show()