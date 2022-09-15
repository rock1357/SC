
#importing data from a csv file 
'importing data from a csv file'
import numpy as np
c=10
#c=input('write the number of rows of your file data from which the numerical data starts from:')
data = np.genfromtxt("electrode2-gain10-Fs10k-nofilter-bias-500mV-dark.csv", delimiter=",",skip_header=c)

t= data[:,0]
V= data[:,1]


#print(V,t)


'''Once introduced the amperometric recording with name t and V here we can make the user to 
choose the range of data to be scanned '''


' calculating the total duration of the '

T=(t[1]-t[0]); 'inverse of the sampling frequency'
Fs=(t[1]-t[0])**-1;'sampling frequency'
print("you used a sampling frequency:",Fs)

N=len(t); 'number of points of the recording' 
print('number of points of the trace:',N)

duration=N*T;
print('the total duration of the trace is',duration)



#[time_interval1,time_interval2]=[input('enter the initial time you want the scanner to start:t_i='),input('enter the final time you want the scanner to finish:t_i=')]
time_interval1= 1;
time_interval2= 100;

n1=time_interval1/T
n2=time_interval2/T



for s in range(round(n1),round(n2)):
    if s>n2-100:
        if V[s]>0:
            print(s)
            break 
    break 
    break


