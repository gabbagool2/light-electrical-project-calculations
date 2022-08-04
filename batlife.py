#####-----battery life calculator-----######



def batcalc():
    V = float(input("volts?"))
    Ah = float(input("capacity?(Ah)"))
    P = float(input("power?(watts)"))

    answer = V*Ah/P

    print("battery life will be approx: ", answer, "hours")
    
if __name__ == "__main__":
    batcalc()