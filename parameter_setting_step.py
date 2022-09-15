import matplotlib.pyplot as plt

def scanning(t,V,tn,Vn,n1,n2,std):

#gain=input('did you use an amplification? Set the gain used in the experiment, although write 1:')
#gain2=input('Write the gain used for the noise acquisition:')  
    gain=10**10;
    gain2=10**10;
  
    'plot of the total time trace-figure divided by the gain'
    # plotting the points 
    plt.plot(t,V/gain)
  
    # naming the x axis
    plt.xlabel('time[s]')
    # naming the y axis
    plt.ylabel('Current [A]')
  
    # giving a title to my graph


    plt.title('total time trace')
  
# function to show the plot
    plt.show()

    V=V/gain2;
    V=V[n1:n2];
    t=t[n1:n2];
    Vn=Vn/gain2;
    k_factor=max(Vn)/std;
    noise=k_factor*std 
    print('the max/min value of the noise is bigger than the standard deviation value of about:',k_factor)
#k_factor=input('choose the multiplication factor for the peak extraction above the std value',k_factor)


    'plot of the choosen partial time trace-figure divided by the gain'
    # plotting the points 
    plt.plot(t,V)
  
    # naming the x axis
    plt.xlabel('time[s]')
    # naming the y axis
    plt.ylabel('Current [A]')
  
    # giving a title to my graph
    plt.title('your choosen partial time trace')
  
    # function to show the plot
    plt.show()


#choice=input('do you have peaks on negative or positive side of the trace?Select negative [n] or positive [p]')
    choice='n';
    
#    if choice=='n':
#       'call negative scanning function'
#       negative_scanning(choice)
#    else:
#       'call positive scanning function'
#       positive_scanning(choice)
       
   
    return 0








