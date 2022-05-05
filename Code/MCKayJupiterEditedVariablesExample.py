import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
fig,ax=plt.subplots()

##### Function to plot graph with standard axes ect ########

def Plot(T,P,name,_colour):
    ax.set_yscale('log')
    plt.ylim(1,0.001)
    plt.xlim(100,200)
    plt.title("Jupiter's Temperatre Pressure Profile Using McKay Model")
    plt.xlabel("Temperature (K)")
    plt.ylabel("Pressure (bar)")
    ax.tick_params(bottom=True, top=True, left=True, right=True)
    ax.tick_params(which="both", axis="both", direction="in")
    ax.xaxis.set_minor_locator(MultipleLocator(10))
    plt.plot(T,P,label=name,color=_colour)
    plt.legend()


####### Extract data from model data file #######

f=open("JupiterModel.txt","r")
lines=f.readlines()
f.close()
T=[]
P=[]
for line in lines:
    a=line.split(",")
    T.append(float(a[0]))
    P.append(float(a[1]))


##### Plot original model ######

Plot(T,P,'Orginal Model','black')


###### Variables used in new model ###
# edit variable of interest and label plot with difference

Fg=5.4
F1=1.3 
F2=7
g=F1/(F2+F1)

F0=50.26  
A=0.343
Fs=((1-A)*F0)/4

P=np.logspace(-3,0,1000)
Tau0=6
P0=1.1 + 1 # edited variable
n=2
Tau=Tau0*((P/P0)**(n))
k=100
s=5.67E-8


####### Find new T values #####

T2=((((Fg+((1-g)*Fs)*((1/2)+((3/4)*Tau)))+(g*Fs*((1/2)+(3/(4*k))+(((k/4)
    -(3/(4*k)))*np.exp(-k*Tau)))))
    /s)**(1/4))


######## Plot model with edited variable ######

Plot(T2,P,'Model with $P_0+1$','green')


###### Variables used in new model ###
# edit variable of interest and label plot with difference

Fg=5.4
F1=1.3
F2=7
g=F1/(F2+F1)

F0=50.26
A=0.343
Fs=((1-A)*F0)/4

P=np.logspace(-3,0,1000)
Tau0=6
P0=1.1 

n=2 + 1 # edited variable
Tau=Tau0*((P/P0)**(n))
k=100
s=5.67E-8


####### Find new T values #####

T3=((((Fg+((1-g)*Fs)*((1/2)+((3/4)*Tau)))+(g*Fs*((1/2)+(3/(4*k))+(((k/4)
    -(3/(4*k)))*np.exp(-k*Tau)))))
    /s)**(1/4))


######## Plot model with edited variable ######

Plot(T3,P,'Model with $n+1$','pink')


### Find largest difference between original and edited models ###

PinkDiff=abs(T-T3)
#print(max(PinkDiff)) ## index 579

GreenDiff=abs(T-T2)
#print(max(GreenDiff))    #### index 999

#Cut data to find max diff in specified region
GreenDiff=GreenDiff[0:700]
#print(max(GreenDiff))    #### index 584


####### Plot points of largest difference #####

T2Scatter=T2[584], T2[999]
PScatter=P[584], P[999]
plt.scatter(T2Scatter,PScatter,label='Largest Difference $p_0+1$')
plt.scatter(T3[579],P[579],label='Largest Difference $n+1$')
plt.legend()
