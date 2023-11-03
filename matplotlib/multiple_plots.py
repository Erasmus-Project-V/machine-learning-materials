import matplotlib.pyplot as plt
import numpy as np

range = (-100,100)
#generiramo 10 brojeva od 0 do 5 jednako razdaljenih
x_1 = np.linspace(range[0],range[1],20)
# note the matrix operacija dolje
func = lambda a:a**2+(a*4)+5*a
y_1 = func(x_1)

# rows pa columns te id sublota koji trentuno crtamo
plt.subplot(1,2,1)
plt.title("happy")
plt.plot(x_1,y_1,"r")



plt.subplot(1,2,2)
plt.title("sad")
plt.plot(x_1,y_1*-1,"g")
plt.show()