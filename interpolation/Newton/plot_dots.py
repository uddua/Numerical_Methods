import numpy as np
import matplotlib.pyplot as plt
import math

X = []
Y = []


with open("output.txt", 'r') as file:
	for line in file:
		asd= line.rstrip('\n').split()
		X.append( float(asd[0]) )
		Y.append( float(asd[1]) )

plt.axes([0., 0., 1, 1])

plt.scatter(X, Y, s=10, c='black', alpha=.5)

plt.rc('grid', linestyle="-", color='black')
plt.grid(True)

plt.show()
