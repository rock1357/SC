import plot_shower as ps
import numpy as np
import negative_peak_levelling as npl

def negative_scanner(t,V,tn,Vn,std,test):
    
    print('-----------------start negative_scanner method-----------------')
    '''define the variables used for the negative peak extraction'''
    
    """the last point of the voltage must be positive to avoid an incomplete extraction of the 
    negative peak"""
    l=len(t)
    
    
    if l<500 :
        print("too few points")
        return 
    
    for s in range(0,l):
       
        if s>l-1-100: 
            
            
            if V[s]>0:
                
                l=round(s)
                print('length=l:',l)
                
                break
    
    
             
        
    
    peak_n=0
    points_nth_peak=[0]*l
    w_parameter=0
    first_while_parameter=0
    second_while_parameter=0
    save_starting_parameter=[0]*l
    save_ending_parameter=[0]*l
    t_peak=[0]*l
    V_peak=[0]*l
    
    k_factor=min(Vn)/(std);
    noise=abs(0.5*k_factor*std) 
    print('the min value of the noise is negativly bigger than the standard deviation value of about:',abs(k_factor))
    
    if test==0: 
        k_factor=float(input('choose the multiplication factor for the peak extraction above the std value:'))
   
    
    while w_parameter<=l-2:
        
        
        '''if a negative peak is found to be lower than -k*std(data) start the
        peak recording '''
        
        
        if w_parameter==l-2:
            
            
            print('number of extracted peaks:',peak_n)
            
            
        
        
        
    
        w_parameter=w_parameter+1;
        
        if V[w_parameter-1] < -noise:
           
           
            peak_n=peak_n+1;'%enhance the counting of the peaks when if cond.% is true'

            first_while_parameter=w_parameter; ''' the first while parameter serves for the
                             % second while parameter-(w.p) (see below)'''
            
                             
            save_starting_parameter[peak_n-1]=first_while_parameter-1;'save the number of the starting t value of the peak for next integration function'
            
            
            
            
            while 1:
                
                
                
                
                
                
                'i want the while to see the condition not at the starting' 
        
                first_while_parameter=first_while_parameter-1; 'decrease the first w.p.'
        
        
                if first_while_parameter<1:
                    
                    ' if the condition is already true break the while loop'
                    V_peak[first_while_parameter]=V[first_while_parameter];
                    first_while_parameter=first_while_parameter+2;
                    break 
    
                elif V[first_while_parameter]>0 :
                    
                    'else continue untill V>=0'
        
                    save_starting_parameter[peak_n-1]=first_while_parameter;
               
        
                    break
                
                
             
        

            second_while_parameter=first_while_parameter;'% the second w.p should start from the last value of the first w.p.'
        
           
            while 2:
                
                
                if second_while_parameter==l-2 :
                    print('while 2-1')
                   
                    break 
                t_peak[second_while_parameter]=float(t[second_while_parameter]);'record t_points of the peak'
                V_peak[second_while_parameter]=float(V[second_while_parameter]);'record the V point of the peak'
            
            
                second_while_parameter=second_while_parameter+1;'encrease the second wp'
                if second_while_parameter>l-2 :
                    print('while 2-2')
                   
                    break
               
                
            
                if V[second_while_parameter]>=0:
                   
                    ' make a condition for the last peak point'
               
                    t_peak[second_while_parameter]=float(t[second_while_parameter]); 'save the last peak point before exit from the while loop'
                    V_peak[second_while_parameter]=float(V[second_while_parameter]); '//////////same/////'
                
                    save_ending_parameter[peak_n-1]=second_while_parameter;
                    points_nth_peak[peak_n-1]=save_ending_parameter[peak_n-1]-save_starting_parameter[peak_n-1]+1;'% counts the n.of point constituting the peak'
               
                    break
                  
            
                
            
            
            
        
            w_parameter=second_while_parameter;
            
            
            
    if w_parameter==l-1 :
        
        
        
                            


        print('-----------------end negative_scanner method-----------------')
        
    '''reinitialize the tr=trestricted and Vr=Vrestricted with the precessed variable by the ns method'''
   
    for i in range(0,l):
        
        if V_peak[i]==0:
            t_peak[i]=np.nan
            V_peak[i]=np.nan
    
        
        
            
        

        
          

    def test_outp_ns():
        for i in range(0,len(t)):
            assert type(t_peak[i])==np.float64
            assert type(V_peak[i])==np.float64
            
        
   
    def test_t_V():
         assert len(t_peak)==l
         assert len(V_peak)==l
        
    
 
    ps.plot_shower(t_peak,V_peak,1)
    
    
    npl.negative_peak_levelling(save_starting_parameter,save_ending_parameter,peak_n,l,t_peak,V_peak)
    
  
        
    return 0
    