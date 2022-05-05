import numpy as np

def RMSD (X,Y,T,P,NumberofPoints):
    
    ComparisonTModel=[]
    ComparisonTData=[]
    ComparisonPModel=[]
    ComparisonPData=[]
    Points=np.logspace(-3,0,NumberofPoints) # chosen pressure points
    
    #find data points closest to chosen pressure points
    for p in Points:
        differencesdata=[]
        for d in Y:
            differencesdata.append(abs(p-d))
        Minimum=min(differencesdata)
        Index=differencesdata.index(Minimum)
        ComparisonPData.append(Y[Index])
        ComparisonTData.append(X[Index])
        
    #find model points closest to the data points
    for p in ComparisonPData:
        differencesdata=[]
        for d in P:
            differencesdata.append(abs(p-d))
        Minimum=min(differencesdata)
        Index=differencesdata.index(Minimum)
        ComparisonPModel.append(P[Index])
        ComparisonTModel.append(T[Index])
    
    
    ######## RMSD #######################
    Tdiff=[]
    for Index in range(len(ComparisonTData)):
        TD=ComparisonTData[Index]
        TM=ComparisonTModel[Index]
        Tdiff.append(TD-TM)
    Tdiff=np.array(Tdiff)
    RMSD=((sum((Tdiff)**2)/(len(ComparisonTData))))**(1/2)
    
    return(RMSD)


######### Extract data from files #######

# change file names for different models and planets
f=open("JupiterModel.txt","r")
lines=f.readlines()
f.close()
T=[]
P=[]
for line in lines:
    a=line.split(",")
    T.append(float(a[0]))
    P.append(float(a[1]))

f=open("JupiterData.txt","r")
lines=f.readlines()
f.close()
X=[]
Y=[]
for line in lines:
    a=line.split(",")
    X.append(float(a[0]))
    Y.append(float(a[1]))
    
RMSDJupiter=RMSD(X,Y,T,P,50) # Use RMSD function for chosen data
# Choose number of points to take along the line (50)
print(RMSDJupiter)