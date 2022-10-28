import numpy as np

a = np.eye(10)

x = np.loadtxt("x.txt")

z = a * x

np.savetxt('z.txt', z, fmt='%.18e', delimiter=' ', newline='\n', header='', footer='', comments='# ', encoding=None)