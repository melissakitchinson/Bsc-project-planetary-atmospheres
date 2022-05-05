import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
fig,ax=plt.subplots()

######## Plot function to set up plot axis ect ########

def Plot(T,P,name):
    ax.set_yscale('log')
    plt.ylim(1,0.001)
    plt.xlim(100,200)
    plt.title("Jupiter's Temperatre Pressure Profile Using McKay Model")
    plt.xlabel("Temperature (K)")
    plt.ylabel("Pressure (bar)")
    ax.tick_params(bottom=True, top=True, left=True, right=True)
    ax.tick_params(which="both", axis="both", direction="in")
    ax.xaxis.set_minor_locator(MultipleLocator(10))
    plt.plot(T,P,label=name,color='black')

############### Variable ##################

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
n=2
Tau=Tau0*((P/P0)**(n))
k=100
s=5.67E-8

############## Model Equation ###########

T=((((Fg+((1-g)*Fs)*((1/2)+((3/4)*Tau)))+(g*Fs*((1/2)+(3/(4*k))+(((k/4)
    -(3/(4*k)))*np.exp(-k*Tau)))))
    /s)**(1/4))

############ Plot model with Plot function ##########

Plot(T,P,'McKay Model Jupiter')


######### Add model data to file ##############

#Commented so it doesn't keep making the file
# =============================================================================
# f = open('JupiterModel.txt', 'w')
# writer = csv.writer(f)
# for x in range(len(T)):
#     a=T[x],P[x]
#     writer.writerow(a)
# f.close()
# =============================================================================

























































