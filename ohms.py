#---ohm calculator---#





def ohmcalc():
    
    I = input("what is amperes?")
    W = input("what is wattage?")
    V = input("what is voltage?")
   
    if len(W) == 0:
        print(f"calculating values using {V}, {I} ")
        w = float(V)/float(I)
        print(f"ohm is : ", w)
        
    elif len(I) == 0:
        print(f"calculating values using {V}, {W} ")
        i = float(sqrt(V))/float(W)
        print(f"ohm is : ", i)
        
    elif len(V) == 0:
        print(f"calculating values using {I}, {W} ")
        v = float(W)/float(sqrt(I))
        print(f"ohm is : ", v)
        


    

 
            
if __name__ == "__main__": 
    ohmcalc()