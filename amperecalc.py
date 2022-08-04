#---ampere calculator---#



def ampcalc():
    
    V = input("what is voltage?")
    W = input("what is wattage?")
    R = input("what is ohms?")
   
    if len(W) == 0:
        print(f"calculating values using {V}, {R} ")
        w = float(V)/float(R)
        print(f"ampere is : ", w)
        
    elif len(R) == 0:
        print(f"calculating values using {W}, {V} ")
        r = float(W)/float(V)
        print(f"ampere is : ", r)
        
    elif len(V) == 0:
        print(f"calculating values using {R}, {W} ")
        v = sqrt(float(W)/float(R))
        print(f"ampere is : ", v)
        


    

 
            
if __name__ == "__main__": 
    ampcalc()