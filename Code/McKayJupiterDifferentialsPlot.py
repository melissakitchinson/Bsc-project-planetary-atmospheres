import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
fig,ax=plt.subplots()

##### Function to plot graph with standard axes ect ########

def Plot(T,P,name,colour,Style,size):
    Name=str(name)
    ax.set_xscale('log')
    #plt.xlim(0.001,1)
    #plt.ylim(-0.1,0.1)
    plt.title("Differentials of McKay Model")
    plt.ylabel("Sensitivity of T")
    plt.xlabel("Pressure at which change will occur (bar)")
    ax.tick_params(bottom=True, top=True, left=True, right=True)
    ax.tick_params(which="both", axis="both", direction="in")
    ax.xaxis.set_minor_locator(MultipleLocator(10))
    plt.plot(T,P,label=Name,linestyle=Style,color=colour,linewidth=size)
    plt.legend(loc='upper left',fontsize='medium',ncol=2,markerscale=1.0,markerfirst=False)


######### Define variables ##############

Fg=5.4
F1=1.3
F2=7
g=F1/(F2+F1)

F0=50.26
A=0.343
Fs=((1-A)*F0)/4

p=np.logspace(-3,0,1000)
Tau0=6
p0=1.1
n=2
Tau=Tau0*((p/p0)**(n))
k=100
s=5.67E-8


### Calculate the value of the differntail equations for the pressure range ##

dT_dFg=0.25*(((1/4)*F0*F1*(1 - A)*(((1/4)*k - 3/4/k)*np.exp(-Tau0*k*(p/p0)**n) 
    + 0.5 + (3/4)/k)/(F1 + F2) + (1/4)*F0*(1 - A)*(-F1/(F1 + F2) + 1)*
    (0.75*Tau0*(p/p0)**n + 0.5) + Fg)/s)**0.25/((1/4)*F0*F1*(1 - A)*
    (((1/4)*k - 3/4/k)*np.exp(-Tau0*k*(p/p0)**n) + 0.5 + (3/4)/k)/(F1 + F2) 
    + (1/4)*F0*(1 - A)*(-F1/(F1 + F2) + 1)*(0.75*Tau0*(p/p0)**n + 0.5) + Fg)

dT_dF1=0.25*(((1/4)*F0*F1*(1 - A)*(((1/4)*k - 3/4/k)*np.exp(-Tau0*k*(p/p0)**n)
    + 0.5 + (3/4)/k)/(F1 + F2) + (1/4)*F0*(1 - A)*(-F1/(F1 + F2) + 1)*
    (0.75*Tau0*(p/p0)**n + 0.5) + Fg)/s)**0.25*(-1/4*F0*F1*(1 - A)*
    (((1/4)*k - 3/4/k)*np.exp(-Tau0*k*(p/p0)**n) + 0.5 + (3/4)/k)/(F1 + F2)**2
    + (1/4)*F0*(1 - A)*(F1/(F1 + F2)**2 - 1/(F1 + F2))*
    (0.75*Tau0*(p/p0)**n + 0.5) + (1/4)*F0*(1 - A)*(((1/4)*k - 3/4/k)
    *np.exp(-Tau0*k*(p/p0)**n) + 0.5 + (3/4)/k)/(F1 + F2))/((1/4)*F0*F1*(1 - A)
    *(((1/4)*k - 3/4/k)*np.exp(-Tau0*k*(p/p0)**n) + 0.5 + (3/4)/k)/(F1 + F2) + 
    (1/4)*F0*(1 - A)*(-F1/(F1 + F2) + 1)*(0.75*Tau0*(p/p0)**n + 0.5) + Fg)


dT_dF2=0.25*(((1/4)*F0*F1*(1 - A)*(((1/4)*k - 3/4/k)*np.exp(-Tau0*k*(p/p0)**n) 
    + 0.5 + (3/4)/k)/(F1 + F2) + (1/4)*F0*(1 - A)*(-F1/(F1 + F2) + 1)*
    (0.75*Tau0*(p/p0)**n + 0.5) + Fg)/s)**0.25*((1/4)*F0*F1*(1 - A)*
    (0.75*Tau0*(p/p0)**n + 0.5)/(F1 + F2)**2 - 1/4*F0*F1*(1 - A)*
    (((1/4)*k - 3/4/k)*np.exp(-Tau0*k*(p/p0)**n) + 0.5 + 
    (3/4)/k)/(F1 + F2)**2)/((1/4)*F0*F1*(1 - A)*(((1/4)*k - 3/4/k)*
    np.exp(-Tau0*k*(p/p0)**n) + 0.5 + (3/4)/k)/(F1 + F2) + 
    (1/4)*F0*(1 - A)*(-F1/(F1 + F2) + 1)*(0.75*Tau0*(p/p0)**n + 0.5) + Fg)


dT_dF0=0.25*(((1/4)*F0*F1*(1 - A)*(((1/4)*k - 3/4/k)*
    np.exp(-Tau0*k*(p/p0)**n) + 0.5 + (3/4)/k)/(F1 + F2) + (1/4)*F0*(1 - A)*
    (-F1/(F1 + F2) + 1)*(0.75*Tau0*(p/p0)**n + 0.5) + Fg)/s)**0.25*((1/4)*F1*
    (1 - A)*(((1/4)*k - 3/4/k)*np.exp(-Tau0*k*(p/p0)**n) + 0.5 + 
    (3/4)/k)/(F1 + F2) + (1/4 - 1/4*A)*(-F1/(F1 + F2) + 1)*(0.75*Tau0*
    (p/p0)**n + 0.5))/((1/4)*F0*F1*(1 - A)*(((1/4)*k - 3/4/k)*
    np.exp(-Tau0*k*(p/p0)**n) + 0.5 + (3/4)/k)/(F1 + F2) + 
    (1/4)*F0*(1 - A)*(-F1/(F1 + F2) + 1)*(0.75*Tau0*(p/p0)**n + 0.5) + Fg)


dT_dA=0.25*(((1/4)*F0*F1*(1 - A)*(((1/4)*k - 3/4/k)*np.exp(-Tau0*k*(p/p0)**n) 
    + 0.5 + (3/4)/k)/(F1 + F2) + (1/4)*F0*(1 - A)*(-F1/(F1 + F2) + 1)*
    (0.75*Tau0*(p/p0)**n + 0.5) + Fg)/s)**0.25*(-1/4*F0*F1*(((1/4)*k - 3/4/k)*
    np.exp(-Tau0*k*(p/p0)**n) + 0.5 + (3/4)/k)/(F1 + F2) - 1/4*F0*
    (-F1/(F1 + F2) + 1)*(0.75*Tau0*(p/p0)**n + 0.5))/((1/4)*F0*F1*(1 - A)*
    (((1/4)*k - 3/4/k)*np.exp(-Tau0*k*(p/p0)**n) + 0.5 + (3/4)/k)/(F1 + F2) 
    + (1/4)*F0*(1 - A)*(-F1/(F1 + F2) + 1)*(0.75*Tau0*(p/p0)**n + 0.5) + Fg)


dT_dTau0=0.25*(((1/4)*F0*F1*(1 - A)*(((1/4)*k - 3/4/k)*
    np.exp(-Tau0*k*(p/p0)**n) + 0.5 + (3/4)/k)/(F1 + F2) + (1/4)*F0*(1 - A)*
    (-F1/(F1 + F2) + 1)*(0.75*Tau0*(p/p0)**n + 0.5) + 
    Fg)/s)**0.25*(-1/4*F0*F1*k*(p/p0)**n*(1 - A)*((1/4)*k - 3/4/k)*
    np.exp(-Tau0*k*(p/p0)**n)/(F1 + F2) + 0.1875*F0*(p/p0)**n*(1 - A)*
    (-F1/(F1 + F2) + 1))/((1/4)*F0*F1*(1 - A)*(((1/4)*k - 3/4/k)*
    np.exp(-Tau0*k*(p/p0)**n) + 0.5 + (3/4)/k)/(F1 + F2) + (1/4)*F0*(1 - A)*
    (-F1/(F1 + F2) + 1)*(0.75*Tau0*(p/p0)**n + 0.5) + Fg)


dT_dP0=0.25*(((1/4)*F0*F1*(1 - A)*(((1/4)*k - 3/4/k)*np.exp(-Tau0*k*(p/p0)**n)
    + 0.5 + (3/4)/k)/(F1 + F2) + (1/4)*F0*(1 - A)*(-F1/(F1 + F2) 
    + 1)*(0.75*Tau0*(p/p0)**n + 0.5) + Fg)/s)**0.25*((1/4)*F0*F1*Tau0*k*n*
    (p/p0)**n*(1 - A)*((1/4)*k - 3/4/k)*np.exp(-Tau0*k*(p/p0)**n)/(p0*(F1 + F2))
    - 0.1875*F0*Tau0*n*(p/p0)**n*(1 - A)*(-F1/(F1 + F2) + 1)/p0)/((1/4)*F0*F1*
    (1 - A)*(((1/4)*k - 3/4/k)*np.exp(-Tau0*k*(p/p0)**n) + 0.5 + 
    (3/4)/k)/(F1 + F2) + (1/4)*F0*(1 - A)*(-F1/(F1 + F2) + 1)*
    (0.75*Tau0*(p/p0)**n + 0.5) + Fg)


dT_dn=0.25*(((1/4)*F0*F1*(1 - A)*(((1/4)*k - 3/4/k)*np.exp(-Tau0*k*(p/p0)**n) 
    + 0.5 + (3/4)/k)/(F1 + F2) + (1/4)*F0*(1 - A)*(-F1/(F1 + F2) + 1)*
    (0.75*Tau0*(p/p0)**n + 0.5) + Fg)/s)**0.25*(-1/4*F0*F1*Tau0*k*(p/p0)**n*
    (1 - A)*((1/4)*k - 3/4/k)*np.exp(-Tau0*k*(p/p0)**n)*np.log(p/p0)/(F1 + F2) 
    + 0.1875*F0*Tau0*(p/p0)**n*(1 - A)*(-F1/(F1 + F2) + 1)*np.log(p/p0))/((1/4)
    *F0*F1*(1 - A)*(((1/4)*k - 3/4/k)*np.exp(-Tau0*k*(p/p0)**n) + 0.5 + 
    (3/4)/k)/(F1 + F2) + (1/4)*F0*(1 - A)*(-F1/(F1 + F2) + 1)*
    (0.75*Tau0*(p/p0)**n + 0.5) + Fg)


dT_dk=0.0625*F0*F1*(((1/4)*F0*F1*(1 - A)*(((1/4)*k - 3/4/k)*
    np.exp(-Tau0*k*(p/p0)**n) + 0.5 + (3/4)/k)/(F1 + F2) + (1/4)*F0*
    (1 - A)*(-F1/(F1 + F2) + 1)*(0.75*Tau0*(p/p0)**n + 0.5) + 
    Fg)/s)**0.25*(1 - A)*(-Tau0*(p/p0)**n*((1/4)*k - 3/4/k)*
    np.exp(-Tau0*k*(p/p0)**n) + 
    (1/4 + (3/4)/k**2)*np.exp(-Tau0*k*(p/p0)**n) - 3/4/k**2)/((F1 + F2)*
    ((1/4)*F0*F1*(1 - A)*(((1/4)*k - 3/4/k)*np.exp(-Tau0*k*(p/p0)**n) + 0.5 +
    (3/4)/k)/(F1 + F2) + (1/4)*F0*(1 - A)*(-F1/(F1 + F2) + 1)*
    (0.75*Tau0*(p/p0)**n + 0.5) + Fg))


# Plot pressure and differentials scaled to simplify plot

Plot(p,(dT_dA/70),'A','orange','-',2)
Plot(p,(dT_dF1/70),'F1','blue','-',2)
Plot(p,(dT_dP0/70),'P0','green','-',2)
Plot(p,(dT_dn/70),'n','pink','-',2)

plt.show()

Plot(p,(dT_dFg/70),'Fg','black','-',2)
Plot(p,(dT_dTau0/70),'Tau0','grey','-',2)
Plot(p,(dT_dF2/70),'F2','r','-',2)
Plot(p,(dT_dF0/70),'F0','yellow','-',2)
Plot(p,(dT_dk/70),'k','purple','-',2)

plt.show()
