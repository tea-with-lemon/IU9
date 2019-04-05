import matplotlib.pylab as plt
from mpl_toolkits.mplot3d import Axes3D
from numpy import *
from scipy.optimize import minimize


def makeData():
    x = arange(-10, 10, 0.1)
    y = arange(-10, 10, 0.1)
    x_1, y_1 = meshgrid(x, y)

    z_1 = 158 * (x_1**2 - y_1)**2 + 2 * (x_1 - 1)**2 + 40
    return x_1, y_1, z_1


x, y, z = makeData()


fig = plt.figure()
axes = Axes3D(fig)

#axes.plot_surface(X, Y, R, linewidth=0.05, cmap=plt.cm.coolwarm, alpha=0.8, antialiased=True)


axes.plot_surface(x, y, z, cmap=plt.cm.coolwarm)

# axes.set_zlim3d(0, 20)
# axes.set_xlim3d(-5, 5)
# axes.set_ylim3d(-5, 5)
# cset = axes.contour(x, y, z, [1, 4, 9, 16], cmap=plt.cm.coolwarm)

plt.show()
#plt.savefig('plt.png', bbox_inches='tight')

