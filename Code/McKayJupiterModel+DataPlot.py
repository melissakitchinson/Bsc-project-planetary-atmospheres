import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
fig,ax=plt.subplots()

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


######### Extract data from digitalised data file #####

f=open("DigitalisedDataJupiter.txt","r")
lines=f.readlines()
f.close()
X=[]
Y=[]
for line in lines:
    a=line.split(",")
    X.append(float(a[0]))
    Y.append(float(a[1]))
    
    
############ Plot function ##################

def Plot(T,P,name,colour,Style):
    ax.set_yscale('log')
    plt.ylim(1,0.001)
    plt.xlim(100,200)
    plt.title("Jupiter's Temperatre Pressure Profile using McKay Model and Data")
    plt.xlabel("Temperature (K)")
    plt.ylabel("Pressure (bar)")
    ax.tick_params(bottom=True, top=True, left=True, right=True)
    ax.tick_params(which="both", axis="both", direction="in")
    ax.xaxis.set_minor_locator(MultipleLocator(10))
    plt.plot(T,P,label=name,linestyle=Style,color=colour)
    plt.legend(loc='lower right')

############ Use Plot function to plot data and model ######

Plot(X,Y,'Data','red','-')
Plot(T,P,'McKay Model','black','-')
