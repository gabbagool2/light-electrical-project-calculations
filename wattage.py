#####-----wattage -----######


def wattcalc():
    
    I = input("what is amperes?")
    V = input("what is voltage?")
    R = input("what is ohms?")
   
    if len(I) == 0:
        print(f"calculating values using {V}, {R} ")
        i = float(sqrt(V))/float(R)
        print(f"voltage is : ", i)
        
    elif len(V) == 0:
        print(f"calculating values using {R}, {I} ")
        v = float(sqrt(I))*float(R)
        print(f"voltage is : ", v)
        
    elif len(R) == 0:
        print(f"calculating values using {I}, {V} ")
        r = float(V)*float(I)
        print(f"voltage is : ", r)
        


    

 
            
if __name__ == "__main__": 
    wattcalc()