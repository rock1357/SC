
def negative_scanner(t,V,tn,Vn,std,test):
    
    print('-----------------start negative_scanner method-----------------')
    '''define the variables used for the negative peak extraction'''
    
    """the last point of the voltage must be positive to avoid an incomplete extraction of the 
    negative peak"""
    l=len(t)
    
    if l<500 :
        print("too few points")
        return 
    
    for s in range(1,l):
       
        if s>len(t)-100: 
            
            
            if V[s]>0:
                
                l=round(s)
                print('length',l)
                
                break
    print(l)
            
             
        
    
    peak_n=0
    points_nth_peak=[0]*l
    for_parameter=0
    first_while_param=0
    second_while_param=0
    save_starting_param_for_int=[0]*l
    save_ending_parameter=[0]*l
    t_peak=[0]*l
    V_peak=[0]*l
    
    k_factor=min(Vn)/(std);
    noise=abs(0.5*k_factor*std) 
    print('the min value of the noise is negativly bigger than the standard deviation value of about:',abs(k_factor))
    
    if test==0: 
        k_factor=float(input('choose the multiplication factor for the peak extraction above the std value'))
   
    
    while for_parameter<=l-2:
        
        '''if a negative peak is found to be lower than -k*std(data) start the
        peak recording '''
        
        if for_parameter==l-2:
            
            print('number of extracted peaks:',peak_n)
            
            
        
        
        
    
        for_parameter=for_parameter+1;

        if V[for_parameter] < -noise:
           
            
            peak_n=peak_n+1;'%enhance the counting of the peaks when if cond.% is true'

            first_while_param=for_parameter; ''' the first while parameter serves for the
                             % second while parameter-(w.p) (see below)'''
                             
            save_starting_param_for_int[peak_n]=first_while_param;'save the number of the starting t value of the peak for next integration function'
            
            
            
        
            while 1:
                
                
                
                
                
                
                
                'i want the while to see the condition not at the starting' 
        
                first_while_param=first_while_param-1; 'decrease the first w.p.'
        
        
                if first_while_param<1:
                    
                    ' if the condition is already true break the while loop'
                    V_peak[first_while_param+1]=V[first_while_param+1];
                    first_while_param=first_while_param+2;
                    break 
    
                elif V[first_while_param]>0 :
                    
                    'else continue untill V>=0'
        
                    save_starting_param_for_int[peak_n]=first_while_param;
               
        
                    break
                
                
             
        

            second_while_param=first_while_param;'% the second w.p should start from the last value of the first w.p.'
        
           
            while 2:
                
                
                if second_while_param==l-2 :
                    print('while 2-1')
                   
                    break 
                t_peak[second_while_param]=float(t[second_while_param]);'record t_points of the peak'
                V_peak[second_while_param]=float(V[second_while_param]);'record the V point of the peak'
            
            
                second_while_param=second_while_param+1;'encrease the second wp'
                if second_while_param>l-2 :
                    print('while 2-2')
                   
                    break
               
                
            
                if V[second_while_param]>=0:
                   
                    ' make a condition for the last peak point'
               
                    t_peak[second_while_param]=float(t[second_while_param]); 'save the last peak point before exit from the while loop'
                    V_peak[second_while_param]=float(V[second_while_param]); '//////////same/////'
                
                    save_ending_parameter[peak_n]=second_while_param;
                    points_nth_peak[peak_n]=save_ending_parameter[peak_n]-save_starting_param_for_int[peak_n]+1;'% counts the n.of point constituting the peak'
               
                    break
                  
            
                
            
            
            
        
            for_parameter=second_while_param;
            
            
    if for_parameter==l-1 :
        
        
        
                            


        print('-----------------end negative_scanner method-----------------')
        
   
    def test_t_V():
         assert len(t_peak)==l
         assert len(V_peak)==l
        
        
        
    return [t_peak,V_peak,l]
    