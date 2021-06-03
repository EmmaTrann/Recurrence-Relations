import numpy as np
import math
import matplotlib.pyplot as plt 

#evaluateRecurrence
def evaluateRecurrence(myfunction, nvec):
    value = myfunction(nvec)
    return value


#Merge sort 
def mergecost(n):
    #Base case
    if (n<2):
        value = 0;
    else: 
        value = 1 + 2*mergecost(n/2) +n
    return value


#Tower of Hanoi 
def Hanoicost(n):
    #Base case
    if (n<1):
        value = 0
    else: 
        value = 2*Hanoicost(n-1) + 1
    return value

#T3
def T3cost(n):
    #Base case
    if (n<3):
        value = 0 
    else:
        value = 5*T3cost(n/3) +n
    return value

#factorial
def factorialcost(n):
    #base case
    if (n<1):
        value = 1
    else: 
        value = n*factorialcost(n-1)
    return value

def main():
    arr_length = int(input("Enter size n for the problem: "))
    nvec = np.zeros((arr_length,1))
    
    for n in range(1,arr_length):
        nvec[n] = n
    
    #mergesort - numerical
    merge_num = np.zeros((arr_length,1))
    for n in range(1, arr_length):
        merge_num[n] = evaluateRecurrence(mergecost, nvec[n])
    
    #mergesort - analytical
    merge_analytic = np.zeros((arr_length,1))
    for n in range(1, arr_length):
        merge_analytic[n] = n*math.log(n)*1.5
        
    #mergesort plot
    plt.figure()
    plt.title("Merge Sort Plot")
    plt.plot(nvec, merge_num, label = "Merge Sort Numerical")
    plt.plot(nvec,merge_analytic, label = "Merge Sort Analytical")
    plt.legend()
    

    #Tower of Hanoi - numerical
    Hanoi_num = np.zeros((arr_length,1))
    for n in range(1, arr_length):
        Hanoi_num[n] = evaluateRecurrence(Hanoicost, nvec[n])
    
    #Tower of Hanoi - analytical
    Hanoi_analytic = np.zeros((arr_length,1))
    for n in range(1, arr_length):
        Hanoi_analytic[n] = (2**n) * 1.2
    
    #Tower of Hanoi plot
    plt.figure()
    plt.title("Tower of Hanoi")
    plt.plot(nvec, Hanoi_num, label = "Tower of Hanoi Numerical")
    plt.plot(nvec,Hanoi_analytic, label = "Tower of Hanoi Analytical")
    plt.legend()
    
        
    #T3 - numerical
    T3_num = np.zeros((arr_length,1))
    for n in range(1, arr_length):
        T3_num[n] = evaluateRecurrence(T3cost, nvec[n])
    
    #T3  - analytical
    T3_analytic = np.zeros((arr_length,1))
    for n in range(1, arr_length):
        T3_analytic[n] = (n**1.46497)*1.2
    
    #T3 plot
    plt.figure()
    plt.title("Problem T3(n)")
    plt.plot(nvec, T3_num, label = "T3(n) Numerical")
    plt.plot(nvec,T3_analytic, label = "T3(n) Analytical")
    plt.legend()
    
    
    #factorial - numerical
    fac_num = np.zeros((arr_length,1))
    for n in range(1, arr_length):
        fac_num[n] = evaluateRecurrence(factorialcost, nvec[n])
    
    #factorial  - analytical
    fac_analytic = np.zeros((arr_length,1))
    for n in range(1, arr_length):
        fac_analytic[n] = math.factorial(n) * 1.2
    
    #factorial plot
    plt.figure()
    plt.title("Factorial")
    plt.plot(nvec, fac_num, label = "Factorial Numerical")
    plt.plot(nvec,fac_analytic, label = "Factorial Analytical")
    plt.legend()
    
    plt.show()
main()
        
