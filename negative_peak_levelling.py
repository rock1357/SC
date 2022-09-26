import plot_shower as ps
import numpy as np

def negative_peak_levelling(ssp,sep,peak_n,l,t_peak,V_peak):
    
    
    
    
    time_constraint=input('choose the time constraint for peaks extraction:')
    time_constraint=0
    
    selected_peaks=0
    t_plot=[0]*l
    V_plot=[0]*l
    Delta_t=[0]*peak_n
    Delta_f=[0]*peak_n


    for i in range(0,peak_n):
                

        
     
        
       
        Delta_t[i]=float(t_peak[sep[i]])-float(t_peak[ssp[i]]);
        Delta_f[i]=Delta_t[i]**-1;
        
        
        
    
        if Delta_t[i]>float(time_constraint):
        
        
            selected_peaks=selected_peaks+1
    
            
            for j in range(ssp[i],sep[i]+1):
                

                t_plot[j]=t_peak[j]
                V_plot[j]=V_peak[j]
                if j==sep[i]:
                    t_plot[sep[i]]=t_peak[sep[i]]
                    V_plot[sep[i]]=1e-30
                    t_plot[ssp[i]]=t_peak[ssp[i]]
                    V_plot[ssp[i]]=1e-30
                    
               
                
         
             
           
        else : 
            for j in range(ssp[i],sep[i]+1): 
                
                t_plot[j]=np.nan
                V_plot[j]=np.nan
                if V_plot[ssp[i]]!=V_plot[sep[i]]:
                    
                    V_plot[sep[i]-1]=V_plot[ssp[i]]
        
    for i in range(0,l):
            
            
        if V_plot[i]==0:
            t_plot[i]=np.nan
            V_plot[i]=np.nan

       

    ps.plot_shower(t_plot,V_plot,2)
                
            
            
           
     
   
 


    return 0
