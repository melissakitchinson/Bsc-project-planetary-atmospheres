import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
fig,ax=plt.subplots()

####### Plot function #################

def Plot(T,P,name,colour,Style,size):
    Name=str(name)
    ax.set_xscale('log')
    #plt.xlim(0.4,100)
    #plt.ylim(-0.1,0.1)
    plt.title("Differentials of R+C Model")
    plt.ylabel("Sensitivity of T")
    plt.xlabel("Pressure at which change will occur (bar)")
    ax.tick_params(bottom=True, top=True, left=True, right=True)
    ax.tick_params(which="both", axis="both", direction="in")
    ax.xaxis.set_minor_locator(MultipleLocator(10))
    plt.plot(T,P,label=Name,linestyle=Style,color=colour,linewidth=size)
    plt.legend(fontsize='medium',ncol=2,markerscale=1.0,markerfirst=False)

   
##############Variables##################

P=np.logspace(-2,2,1000)
Fnet= 160 
Fi=0
P0= 92 
T0= 730 
n= 1 
Tau0=400
TauRC=1
D=5/3
S=5.67E-8
a=0.8
g=1.3
adjust=80

################## R+C Model Data #############

#Extract data from data file
f=open("VenusModel1.txt","r")
lines=f.readlines()
f.close()
T=[]
P=[]
for line in lines:
    a=line.split(",")
    T.append(float(a[0]))
    P.append(float(a[1]))


######## Split pressures into rad and con regions #######
PRad=P[:341]
PCon=P[341:]


###### T RAD differental equations ###########

dT_dFnet=0.210224103813429*((Fi + Fnet)*(D*Tau0*(PRad/P0)**n + 1)/S)**0.25/(Fi + Fnet)


dT_dFi=0.210224103813429*((Fi + Fnet)*(D*Tau0*(PRad/P0)**n + 1)/S)**0.25/(Fi + Fnet)


dT_dD=0.210224103813429*Tau0*(PRad/P0)**n*((Fi + Fnet)*(D*Tau0*(PRad/P0)**n + 1)/S)**0.25/(D*Tau0*(PRad/P0)**n + 1)


dT_dTau0=0.210224103813429*D*(PRad/P0)**n*((Fi + Fnet)*(D*Tau0*(PRad/P0)**n + 1)/S)**0.25/(D*Tau0*(PRad/P0)**n + 1)


dT_dP0=-0.210224103813429*D*n*Tau0*(PRad/P0)**n*((Fi + Fnet)*(D*Tau0*(PRad/P0)**n + 1)/S)**0.25/(P0*(D*Tau0*(PRad/P0)**n + 1))


dT_dn=0.210224103813429*D*Tau0*(PRad/P0)**n*((Fi + Fnet)*(D*Tau0*(PRad/P0)**n + 1)/S)**0.25*np.log(PRad/P0)/(D*Tau0*(PRad/P0)**n + 1)


####### T CON differentail equations ############

dT_dT0=(PCon/P0)**(a*(g - 1)/g)

dT_dP0C=-T0*a*(PCon/P0)**(a*(g - 1)/g)*(g - 1)/(P0*g)

dT_da=T0*(PCon/P0)**(a*(g - 1)/g)*(g - 1)*np.log(PCon/P0)/g

dT_dg=T0*a*(PCon/P0)**(a*(g - 1)/g)*np.log(PCon/P0)/g**2


########### Plot pressures and differentials ############

#Choose which to plot together, might need to change axis limits in Plot function

Plot(PRad,(dT_dFnet/250),'$\dfrac{\partial T}{\partial F_{net}}$','cornflowerblue','-',2)
Plot(PRad,(dT_dFi/250),'$\dfrac{\partial T}{\partial F_i}$','blue','--',2)
Plot(PRad,(dT_dP0/250),'$\dfrac{\partial T}{\partial P_0}$','green','-',2)
Plot(PRad,(dT_dTau0/250),'$\dfrac{\partial T}{\partial Tau_0}$','grey','-',2)
Plot(PRad,(dT_dD/250),'$\dfrac{\partial T}{\partial D}$','orange','-',2)
Plot(PRad,(dT_dn/250),'$\dfrac{\partial T}{\partial n}$','pink','-',2)
#plt.show()

Plot(PCon,(dT_dT0/700),'$\dfrac{\partial T}{\partial T_0}$','black','-',2)
Plot(PCon,(dT_dP0C/700),'$\dfrac{\partial T}{\partial P_0}$','r','-',2)
Plot(PCon,(dT_da/700),'$\dfrac{\partial T}{\partial alpha}$','yellow','-',2)
Plot(PCon,(dT_dg/700),'$\dfrac{\partial T}{\partial gamma}$','purple','-',2)
plt.show()



