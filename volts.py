#---volts calculator---# 





def voltcalc():
    
    I = input("what is amperes?")
    W = input("what is wattage?")
    R = input("what is ohms?")
   
    if len(W) == 0:
        print(f"calculating values using {I}, {R} ")
        w = float(I)*float(R)
        print(f"voltage is : ", w)
        
    elif len(R) == 0:
        print(f"calculating values using {W}, {I} ")
        r = float(W)/float(I)
        print(f"voltage is : ", r)
        
    elif len(I) == 0:
        print(f"calculating values using {R}, {W} ")
        i = sqrt(float(W)*float(R))
        print(f"voltage is : ", i)
        


    

 
            
if __name__ == "__main__": 
    voltcalc()