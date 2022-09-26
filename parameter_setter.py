#importing data from a csv file 
import numpy as np
import plot_shower as ps
import negative_scanner as ns

test=0

c=10
print('import the data of your recorded chronoamperometric experiment')
#c=input('write the number of rows of your file data from which the numerical data starts from:')
data = np.genfromtxt("electrode2-gain10-Fs10k-nofilter-bias-500mV-dark.csv", delimiter=",",skip_header=c)

print('import the data of your recorded noise (no bias)')
data2 = np.genfromtxt("electrode2-gain10-Fs10k-nofilter-bias-500mV-dark.csv", delimiter=",",skip_header=c)

t= data[:,0]
V= data[:,1]

tn= data2[:,0]
Vn= data2[:,1]

def test_data():
    for i in range(0,len(t)-1):
        assert type(t[i])==np.float64
        assert type(V[i])==np.float64
        
        
    
gain=10**10;
    
gain2=10**10;

if test==0:
    gain=int(input('did you use an amplification? Set the gain used in the experiment, although write 1:'))
    gain2=int(input('Write the gain used for the noise acquisition:')  )


std=np.std(Vn/float(gain2))


'''Once introduced the chronoamperometric recording with name t and V here we can make the user to 
choose the range of data to be scanned '''


' calculating the total duration of the '

T=(t[1]-t[0]); 'inverse of the sampling frequency'
Fs=(t[1]-t[0])**-1;'sampling frequency'
print("you used a sampling frequency:",round(Fs))

N=len(t); 'number of points of the recording' 
print('number of points of the trace:',N)

duration=N*T;
print('the total duration of the trace is',duration)




if test==0:
    [time_interval1,time_interval2]=[input('enter the initial time you want the scanner to start:t_i='),input('enter the final time you want the scanner to finish:t_i=')]
time_interval1= 0;
time_interval2= 0.1;

n1=round(time_interval1/T)
n2=round(time_interval2/T)


"""the last point of the voltage must be positive to avoid an incomplete extraction of the 
negative peak"""



V=V/gain2;
Vr=V[n1:n2];
tr=t[n1:n2];
Vn=Vn/gain2;


a=ps.plot_shower(tr,Vr,0,t,V)

       

def test_ps():
    a=ps.plot_shower(0,0,0,0,0)
    assert a==0



if test==0:
    choice=input('do you have peaks on negative or positive side of the trace?Select negative [n] or positive [p]')

choice='n'
    
if choice=='n':
    'call negative scanning function'
    b=ns.negative_scanner(tr,Vr,tn,Vn,std,test)
else:
    'call positive scanning function'
    #positive_scanning(choice)









    
    
    

