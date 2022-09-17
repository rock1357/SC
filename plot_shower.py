import matplotlib.pyplot as plt

def parameter_setter(tr,Vr,t,V):


    'plot of the total time trace-figure divided by the gain'
    # plotting the points 
    plt.plot(t,V)
  
    # naming the x axis
    plt.xlabel('time[s]')
    # naming the y axis
    plt.ylabel('Current [A]')
  
    # giving a title to my graph


    plt.title('total time trace')
  
# function to show the plot
    plt.show()
    
    'now we reinitialize the V and t variables with the choosen time range'





    'plot of the choosen partial time trace-figure divided by the gain'
    # plotting the points 
    plt.plot(tr,Vr)
  
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








