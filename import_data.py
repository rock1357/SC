#importing data from a csv file 
import numpy as np
c=10
#c=input('write the number of rows of your file data from which the numerical data starts from:')
data = np.genfromtxt("electrode2-gain10-Fs10k-nofilter-bias-500mV-dark.csv", delimiter=",",skip_header=c)

time = data[:,0]
Volt = data[:,1]


print(Volt,time)

#print(array)sss