
import pyqtgraph as pg
import pyqtgraph.exporters
import numpy as np
import math

momento_x_min = 45
momento_x = 67
momento_y_min = 30
momento_y = 50
'''
theta = 30
z = []
w = []
for theta in range(360):
	theta_conv = (theta*math.pi)/180
	seno = math.sin(theta_conv)
	cosseno = math.cos(theta_conv)
	z.append(seno)
	w.append(seno)

print(z)
print(w)
'''

x = []
y = []
for i in range(360):
	theta = i
	theta_conv = (theta*math.pi)/180

	seno = math.sin(theta_conv)
	seno = momento_y_min * seno

	cosseno = math.cos(theta_conv)
	cosseno = momento_x_min * cosseno

	x.append(seno)
	y.append(cosseno)

z = []
w = []
for j in range(360):
	theta = j
	theta_conv = (theta*math.pi)/180

	seno = math.sin(theta_conv)
	seno = momento_y * seno

	cosseno = math.cos(theta_conv)
	cosseno = momento_x * cosseno

	z.append(seno)
	w.append(cosseno)

# create plot
'''plt = pg.plot(x, y, title='theTitle', pen='r')
plt.showGrid(x=True,y=True)
'''
# create plot
plt = pg.plot()
plt.showGrid(x=True,y=True)
plt.addLegend()

# set properties
plt.setLabel('left', 'Momentos Y', units='KN.m')
plt.setLabel('bottom', 'Momentos X', units='KN.m')
plt.setXRange(0,10)
plt.setYRange(0,20)
plt.setWindowTitle('pyqtgraph plot')

plt.enableAutoRange()

# plot
c1 = plt.plot(x, y, pen='r', name='Envoltória Momentos min')
c2 = plt.plot(z, w, pen='b', name='Envoltória Momentos máx')
#c2 = plt.plot(x, y2, pen='r', symbol='o', symbolPen='r', symbolBrush=0.2, name='blue')


## Start Qt event loop.
if __name__ == '__main__':
    import sys
    if sys.flags.interactive != 1 or not hasattr(pg.QtCore, 'PYQT_VERSION'):
        pg.QtGui.QApplication.exec_()