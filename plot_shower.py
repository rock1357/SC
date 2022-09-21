import matplotlib.pyplot as plt

def plot_shower(tr,Vr,t=0,V=0):


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



   
    return 0








