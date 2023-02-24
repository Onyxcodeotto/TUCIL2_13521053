import numpy as np
from math import *

def DivNCon(S):
    if len(S)==3:
        d2 = DivNCon(S[1:3])
        return min(d2, EuclideanDistance(S[0], S[1]), EuclideanDistance(S[0], S[2]))
        
    elif(len(S) == 2):
        return EuclideanDistance(S[0],S[1])
    else:
        #Bagi rata
        d1 = DivNCon(S[:floor(len(S)/2)])
        d2 = DivNCon(S[floor(len(S)/2):(len(S))])
        
        #solve middle
        
        d3 = min(d1,d2)
        SL = []
        SR = []
        L  = S[floor(len(S)/2)][0] 
        
        for i in range(len(S)):
            if abs(S[i][0] - L) < d3:
                if S[i][0] < L:
                    SL.append(S[i])
                else:
                    SR.append(S[i])
        
        for i in range(len(SL)):
            for j in range(len(SR)):
                if EuclideanDistance(SL[i], SR[j]) < d3: 
                    d3 = EuclideanDistance(SL[i], SR[j])
        #output
        return d3
            

def EuclideanDistance(a, b):
    # return np.sqrt(np.sum((a - b)**2))
    # print(a, b)
    # print(np.linalg.norm(a-b))
    return np.linalg.norm(a-b)


def sortList(S):
    return S[S[:,0].argsort()]
