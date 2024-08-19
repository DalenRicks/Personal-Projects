# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
import math as m

#List of supported settings
approved_functions = ["the center frequency", "center frequency", "fc", "f", "the inductance", "inductance", "l"]
approved_packages = ["TSSOP", "QFN"]
approved_VCO = ["RF1", "RF2", "IF"]
limit_RF1 = [947, 1720]
limit_RF2 = [789, 1429]
limit_IF = [526, 952]

#TSSOP package variables
Lrf1T = 2.0
Lrf2T = 2.3
LifT = 2.1
Crf1T = 4.3
Crf2T = 4.8
CifT = 6.5

#QFN package variables
Lrf1Q = 1.5
Lrf2Q = 1.5
LifQ = 1.6
Crf1Q = 4.3
Crf2Q = 4.8
CifQ = 6.5

print("Welcome to the PCB trace inductor calculator!\n")

#Recording the height of the deilectric between the PCB layers
height = int(input("Enter the height of the PCB deilectric in um\n"))

#Recording what package is being used
package = str(input("Are you using the TSSOP or QFN package?\n"))

#If the package is not in the approved list, it will re-ask
while package.upper() not in approved_packages:
    package = str(input("Option not supported, please enter either TSSOP or QFN.\n"))

#Recording what VCO you are using
profile = str(input("Which VCO are you using? RF1, RF2 or IF?\n"))

#If the VCO is not in the approved list, it will re-ask
while profile.upper() not in approved_VCO:
    profile = str(input("Option not supported, please enter either RF1, RF2 or IF?.\n"))

#Recording the calculator function
function = str(input("Would you like to calculate the inductor length given the center frequency (fc) or the inductance (L)?\n"))

#If the function is not in the approved list, it will re-ask
while function.lower() not in approved_functions:
    function = str(input("Option not supported, please enter either the center frequency (fc) or the inductance (L)\n"))

#Case for calculating the length given the center frequency
if function.lower() in approved_functions[:4]:

    #Asking for the center frequency for the selected VCO
    if(profile.upper() == "RF1"):
        fc = float(input("Enter the center frequency in MHz between " + str(limit_RF1[0]) + " and " + str(limit_RF1[1]) +"\n"))
        
        #If the selected center frequency is not in bounds, it will re-ask
        while limit_RF1[0] <= fc and fc >= limit_RF1[1]:
            fc = float(input("Option not supported, please center frequency in MHz between " + str(limit_RF1[0]) + " and " + str(limit_RF1[1]) +"\n"))
    
    #Asking for the center frequency for the selected VCO        
    elif(profile.upper() == "RF2"):
        fc = float(input("Enter the center frequency in MHz between " + str(limit_RF2[0]) + " and " + str(limit_RF2[1]) +"\n"))
        
        #If the selected center frequency is not in bounds, it will re-ask
        while limit_RF2[0] <= fc and fc >= limit_RF2[1]:
            fc = float(input("Option not supported, please center frequency in MHz between " + str(limit_RF2[0]) + " and " + str(limit_RF2[1]) +"\n"))
    
    #Asking for the center frequency for the selected VCO
    else:
        fc = float(input("Enter the center frequency in MHz between " + str(limit_IF[0]) + " and " + str(limit_IF[1]) +"\n"))
        
        #If the selected center frequency is not in bounds, it will re-ask
        while limit_IF[0] <= fc and fc >= limit_IF[1]:
            fc = float(input("Option not supported, please center frequency in MHz between " + str(limit_IF[0]) + " and " + str(limit_IF[1]) +"\n"))

    #TSSOP Package
    if(package.upper() == "TSSOP"):
        
        #Formula for RF1
        if(profile.upper() == "RF1"):
            X = 0.7 * (1 - 0.857 * m.exp(-(height/140)))
            L = ((1/(((2 * m.pi * fc * 10**6) ** 2) * (Crf1T * 10**-12))) - (Lrf1T * 10**-9)) * 10**9
            D = L/X
            print("The length of D is " + str(D) + "mm\n")
            print("The inductance of the trace is " + str(D * X) + "nH\n")
            
        #Formula for RF2
        elif(profile.upper() == "RF2"):
            X = 0.7 * (1 - 0.857 * m.exp(-(height/140)))
            L = ((1/(((2 * m.pi * fc * 10**6) ** 2) * (Crf2T * 10**-12))) - (Lrf2T * 10**-9)) * 10**9
            D = L/X
            print("The length of D is " + str(D) + "mm\n")
            print("The inductance of the trace is " + str(D * X) + "nH\n")
            
        #Formula for IF
        elif(profile.upper() == "IF"):
            X = 0.7 * (1 - 0.857 * m.exp(-(height/140)))
            L = ((1/(((2 * m.pi * fc * 10**6) ** 2) * (CifT * 10**-12))) - (LifT * 10**-9)) * 10**9
            D = L/X
            print("The length of D is " + str(D) + "mm\n")
            print("The inductance of the trace is " + str(D * X) + "nH\n")
        else:
            print("Option not supported. Please check spelling.")
            
    #QFN Package
    elif(package.upper() == "QFN"):
        
        #Formula for RF1
        if(profile.upper() == "RF1"):
            X = 0.62 * (1 - 0.823 * m.exp(-(height/130)))
            L = ((1/(((2 * m.pi * fc * 10**6) ** 2) * (Crf1Q * 10**-12))) - (Lrf1Q * 10**-9)) * 10**9
            D = L/X
            print("The length of D is " + str(D) + "mm\n")
            print("The inductance of the trace is " + str(D * X) + "nH\n")
            
        #Formula for RF2
        elif(profile.upper() == "RF2"):
            X = 0.62 * (1 - 0.823 * m.exp(-(height/130)))
            L = ((1/(((2 * m.pi * fc * 10**6) ** 2) * (Crf2Q * 10**-12))) - (Lrf2Q * 10**-9)) * 10**9
            D = L/X
            print("The length of D is " + str(D) + "mm\n")
            print("The inductance of the trace is " + str(D * X) + "nH\n")
        
        #Formula for IF
        elif(profile.upper() == "IF"):
            X = 0.62 * (1 - 0.823 * m.exp(-(height/130)))
            L = ((1/(((2 * m.pi * fc * 10**6) ** 2) * (CifQ * 10**-12))) - (LifQ * 10**-9)) * 10**9
            D = L/X
            print("The length of D is " + str(D) + "mm\n")
            print("The inductance of the trace is " + str(D * X) + "nH\n")
        else:
            print("Option not supported. Please check spelling.")
    else:
        print("Option not supported. Please check spelling.")

#Case for calculating the length given the inductance
else:
    L = float(input("Enter the inductance in nH\n"))
    
    #Note from AN31 from Silicon Labs
    if L > 2.0:
        print("Please note that PCB inductors are recommended for inductances smaller than 2nH.\n")
    
    #TSSOP Package
    if(package.upper() == "TSSOP"):
        
        #Formula for RF1
        if(profile.upper() == "RF1"):
            X = 0.7 * (1 - 0.857 * m.exp(-(height/140)))
            D = L/X
            freq = 1/(2*m.pi*m.sqrt(Crf1T * 10**-12 *(Lrf1T * 10**-9 + L* 10**-9)))* 10**-6
            print("The length of D is " + str(D) + "mm\n")
            print("The center frequency of the PLL is " + str(freq) + "MHz\n")
            
        #Formula for RF2
        elif(profile.upper() == "RF2"):
            X = 0.7 * (1 - 0.857 * m.exp(-(height/140)))
            D = L/X
            freq = 1/(2*m.pi*m.sqrt(Crf2T * 10**-12 *(Lrf2T * 10**-9 + L* 10**-9)))* 10**-6
            print("The length of D is " + str(D) + "mm\n")
            print("The center frequency of the PLL is " + str(freq) + "MHz\n")
            
        #Formula for IF
        elif(profile.upper() == "IF"):
            X = 0.7 * (1 - 0.857 * m.exp(-(height/140)))
            D = L/X
            freq = 1/(2*m.pi*m.sqrt(CifT * 10**-12 *(LifT * 10**-9 + L* 10**-9)))* 10**-6
            print("The length of D is " + str(D) + "mm\n")
            print("The center frequency of the PLL is " + str(freq) + "MHz\n")
            
        #Catch-all    
        else:
            print("Option not supported. Please check spelling.")
            
    #QFN Package
    elif(package.upper() == "QFN"):
        
        #Formula for RF1
        if(profile.upper() == "RF1"):
            X = 0.62 * (1 - 0.823 * m.exp(-(height/130)))
            D = L/X
            freq = 1/(2*m.pi*m.sqrt(Crf1Q * 10**-12 *(Lrf1Q * 10**-9 + L* 10**-9)))* 10**-6
            print("The length of D is " + str(D) + "mm\n")
            print("The center frequency of the PLL is " + str(freq) + "MHz\n")
            
        #Formula for RF2
        elif(profile.upper() == "RF2"):
            X = 0.62 * (1 - 0.823 * m.exp(-(height/130)))
            D = L/X
            freq = 1/(2*m.pi*m.sqrt(Crf2Q * 10**-12 *(Lrf2Q * 10**-9 + L* 10**-9)))* 10**-6
            print("The length of D is " + str(D) + "mm\n")
            print("The center frequency of the PLL is " + str(freq) + "MHz\n")
        
        #Formula for IF
        elif(profile.upper() == "IF"):
            X = 0.62 * (1 - 0.823 * m.exp(-(height/130)))
            D = L/X
            freq = 1/(2*m.pi*m.sqrt(CifQ * 10**-12 *(LifQ * 10**-9 + L* 10**-9))) * 10**-6
            print("The length of D is " + str(D) + "mm\n")
            print("The center frequency of the PLL is " + str(freq) + "MHz\n")
        else:
            print("Option not supported. Please check spelling.")
    
    #Catch-all        
    else:
        print("Option not supported. Please check spelling.")
