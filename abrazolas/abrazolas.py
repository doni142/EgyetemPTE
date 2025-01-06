# Ábrázolás Py Program

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(200) - 100.0 #[2, 3, 5, 7, 11, 13, 17, 19]
fx = np.pow(x, 2)
gx = np.pow(x, 3)
hx = np.pow(x, 4)
kx = np.sin(np.pi*100.0/x)

# print(y)
plt.subplot(1, 2, 1)

y = x/100*np.pi
ky = np.sin(y)

plt.plot(x, fx, color = 'k', label = '$f(x) = x*2$')
plt.plot(x, gx, color = 'g', label = '$g(x) = x*3$')
plt.plot(x, hx, color = 'r', label = '$h(x) = x*4$')
plt.plot(x, kx, color = 'y', label = '$k(x) = x*5$')
# plt.show()
# cím
plt.title("Függvények", fontsize = 20)

# tengely feliratok + betűméret
plt.xlabel("x", fontsize = 20)
plt.ylabel("y", fontsize = 20)

# címkék betűméret
plt.tick_params(axis="both", which="major", labelsize=10)

#Tengely intervallumok
plt.xlim([-100, 100])
plt.ylim([-1, 1])

# Kiírja a magyarázatot
plt.legend()
plt.show()