import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
fig,ax=plt.subplots()

##################R+C Modle Data#############

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

###################plot################################

#Plot function for data lines
def Plot(T,P,name,colour,Style,size):
    Name=str(name)
    ax.set_yscale('log')
    plt.ylim(100,0.01)
    plt.xlim(150,800)
    plt.title("Venus' Temperatre Pressure Profile Using Data and R+C Model")
    plt.xlabel("Temperature (K)")
    plt.ylabel("Pressure (bar)")
    ax.tick_params(bottom=True, top=True, left=True, right=True)
    ax.tick_params(which="both", axis="both", direction="in")
    ax.xaxis.set_minor_locator(MultipleLocator(10))
    plt.plot(T,P,label=Name,linestyle=Style,color=colour,linewidth=size)
    plt.legend(loc='upper right',fontsize='medium',ncol=2,markerscale=1.0,markerfirst=False)

#Plot function for data points
def PlotS(T,P,name,colour,Style,size):

    Name=str(name)
    ax.set_yscale('log')
    plt.ylim(100,0.01)
    plt.xlim(150,800)
    plt.title("Venus' Temperatre Pressure Profile Using Data and R+C Model")
    plt.xlabel("Temperature (K)")
    plt.ylabel("Pressure (bar)")
    ax.tick_params(bottom=True, top=True, left=True, right=True)
    ax.tick_params(which="both", axis="both", direction="in")
    ax.xaxis.set_minor_locator(MultipleLocator(10))
    plt.scatter(T,P,label=Name,linestyle=Style,color=colour,s=size)
    plt.legend(loc='upper right',fontsize='medium',ncol=2,markerscale=1.0,markerfirst=False)

############# Plot model ################
Plot(T,P,'R+C n=1','black',':',2)


################Data#########################

f=open("mgn_rtpd.dat","r")
lines=f.readlines()
f.close()

data ={}

for line in lines:
    A=line.split(',')
    N=str(A[0])+str(A[1])
    if not N in data.keys():
        data[N] = {'X':[] , 'Y':[]}
    
    data[N]['X'].append(float(A[5]))
    data[N]['Y'].append(float(A[7]))

X16=data['X3214']['X']
Y16=data['X3214']['Y']

Plot(X16,Y16,"Magellan","brown","-",2)

###################################

f=open("vg2lr.dat","r")
lines=f.readlines()
f.close()
X6=[]
Y6=[]
for line in lines:
    a=line.split(",")
    X6.append(float(a[3]))
    Y6.append(float(a[2]))

Plot(X6,Y6,'Vega Lander','seagreen','-',2)

##############################

f=open("article_data.txt","r")
lines=f.readlines()
f.close()

data ={}

for line in lines:
    A=line.split(',')
    N=str(A[0])
    if not N in data.keys():
        data[N] = {'X':[] , 'Y':[]}
    
    data[N]['X'].append(float(A[2]))
    data[N]['Y'].append(float(A[1]))
    
X35=data['35']['X']
Y35=data['35']['Y']
X55=data['55']['X']
Y55=data['55']['Y']
X70=data['70']['X']
Y70=data['70']['Y']


PlotS(X35,Y35,'Article data 35','darkorange','-',2)
PlotS(X55,Y55,'Article data 55','violet','-',2)
PlotS(X70,Y70,'Article data 70','springgreen','-',2)


############ Single Data Line #########################

#Combine Magellan and Vega Lander data into smooth line
X16=X16[::-1]
X6=X6[100:]
X=np.concatenate((X16,X6),axis=0)
X=X[36:]
Y16=Y16[::-1]
Y6=Y6[100:]
Y=np.concatenate((Y16,Y6),axis=0)
Y=Y[36:]
Plot(X,Y,'Single Data Line','blue','-',1)


######### Add Data To File ###################

#commented so it doesn't remake the file
# =============================================================================
# import csv
# f = open('VenusData.txt', 'w')
# writer = csv.writer(f)
# for x in range(len(Y)):
#     a=X[x],Y[x]
#     writer.writerow(a)
# f.close()
# =============================================================================









































