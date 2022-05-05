import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
fig,ax=plt.subplots()

# log of pressure = 0.01 to 100
P=np.logspace(-2,2,1000)
Fnet= 160 #W m^-2 
Fi=0
P0= 92 #bar
T0= 730 #K
n1= 1 
n2= 2
Tau01=400 #n=1 
Tau02=2E5 #n=2
TauRC1=1 #n=1
TauRC2=0.1 #n=2
D=5/3
S=5.67E-8 #sigma W m^-2 K^-4
a=0.8 #alpha
g=1.3 #gamma
adjust=80



###############Radiative#################

def Radiative(Tau0,P,P0,n,Fnet,Fi,D,TauRC,S):
    Tau=Tau0*((P/P0)**(n))  #calculate tau from pressure, 0.04 - 434.78
    c=0
    for x in Tau:
        if x<=TauRC:
            c+=1
        else:
            continue
    TauRad=Tau[0:c]           #find taus in rad region
    TRad=(((Fnet+Fi)*(1+(D*TauRad)))/(2*S))**(1/4)  #find T for each Tau
    #PRad=P0*((TauRad/Tau0)**(1/n)) #optional - recalculate P or cut original array
    PRad=P[0:c]
    return TRad,PRad,c,Tau


######################### Convective ########################

def Convective(Tau,c,P0,Tau0,n,T0,a,g,adjust):
    #TauCon=Tau[c+adjust:] #needed if recalculating P
    #PCon=P0*((TauCon/Tau0)**(1/n)) #optional - recalculate P or cut original array
    PCon=P[c+adjust:]
    TCon=T0*((PCon/P0)**((a*(g-1))/g))
    return TCon,PCon

#################Join arrays###############

def JoinArrays(TRad,Tcon,PRad,PCon):
    T=np.concatenate((TRad, TCon),axis=0)
    P=np.concatenate((PRad,PCon),axis=0)
    return T,P

###################plot################################

def Plot(T,P,name):
    Name="n="+str(name)
    if name==1:
        Style='dotted'
    elif name==2:
        Style='dashed'
    ax.set_yscale('log')
    plt.ylim(100,0.01)
    plt.title("Venus' Temperatre Pressure Profile Using R+C Model")
    plt.xlabel("Temperature (K)")
    plt.ylabel("Pressure (bar)")
    ax.tick_params(bottom=True, top=True, left=True, right=True)
    ax.tick_params(which="both", axis="both", direction="in")
    ax.xaxis.set_minor_locator(MultipleLocator(10))
    plt.plot(T,P,label=Name,linestyle=Style,color='black')
    plt.legend()


######## Caclulate T and P for n=1 and plot ####

TRad,PRad,c,Tau=Radiative(Tau01,P,P0,n1,Fnet,Fi,D,TauRC1,S)
TCon,PCon=Convective(Tau,c,P0,Tau01,n1,T0,a,g,adjust)
T1,P1=JoinArrays(TRad,TCon,PRad,PCon)
Plot(T1,P1,1)


######## Caclulate T and P for n=2 and plot ####

TRad,PRad,c,Tau=Radiative(Tau02,P,P0,n2,Fnet,Fi,D,TauRC2,S)
TCon,PCon=Convective(Tau,c,P0,Tau02,n2,T0,a,g,adjust)
T2,P2=JoinArrays(TRad,TCon,PRad,PCon)
Plot(T2,P2,2)

plt.show()

########### Add Data to file #############

#Commented so it doesn't remake the file every time
# =============================================================================
# import csv
# f = open('VenusModel1.txt', 'w')
# writer = csv.writer(f)
# for x in range(len(T)):
#     a=T1[x],P2[x]
#     writer.writerow(a)
# f.close()
# 
# f = open('VenusModel2.txt', 'w')
# writer = csv.writer(f)
# for x in range(len(T)):
#     a=T1[x],P2[x]
#     writer.writerow(a)
# f.close()
# =============================================================================
