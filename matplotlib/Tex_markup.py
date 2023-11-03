import math

import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax_1 = fig.add_axes((0.1,0.1,0.85,0.85))


x_1 = np.linspace(-10,10,40)
y_1 = 2.73**np.tan(math.pi*x_1)

ax_1.set_title("Function representation")
ax_1.set_ylim([0,200])
# r - raw string, jer su backlashes vazan dio Tex-a
ax_1.text(-5,30,r"$y=e^{tan({\pi}x)}$",size=30)
ax_1.text(-5,100, r"$y=\frac{\sum_{i=0}^\infty e^{x_i}}{\acute \alpha_0}$",size=40)
ax_1.text(-5,180, r"$\bar a \hat a \tilde a \vec a \overline {a} \lim_{x \to 2} \geq \leq \neq$",size=15)

ax_1.plot(x_1,y_1,lw=4)
fig.show()