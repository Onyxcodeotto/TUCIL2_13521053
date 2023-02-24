import numpy as np
from math import *

def DivNCon(S):
    if len(S)==3:
        d2 = DivNCon(S[1:3])
        if d2[0] <= EuclideanDistance(S[0], S[1])[0] and d2[0] <= EuclideanDistance(S[0], S[2])[0]:
            return d2
        elif d2[0] <= EuclideanDistance(S[0], S[1])[0]:
            return EuclideanDistance(S[0], S[1])
        else:
            return EuclideanDistance(S[0], S[2])
        # return min(d2, EuclideanDistance(S[0], S[1]), EuclideanDistance(S[0], S[2]))
        
    elif(len(S) == 2):
        return EuclideanDistance(S[0],S[1])
    else:
        #Bagi rata
        d1 = DivNCon(S[:floor(len(S)/2)])
        d2 = DivNCon(S[floor(len(S)/2):(len(S))])
        
        #solve middle
        if (d1[0] <= d2[0]):
            d3 = d1
        else:
            d3 = d2
        # d3 = min(d1,d2)
        # point1 = 
        SL = []
        SR = []
        L  = S[floor(len(S)/2)][0] 
        
        for i in range(len(S)):
            if abs(S[i][0] - L) < d3[0]:
                if S[i][0] < L:
                    SL.append(S[i])
                else:
                    SR.append(S[i])
        
        for i in range(len(SL)):
            for j in range(len(SR)):
                if EuclideanDistance(SL[i], SR[j])[0] < d3[0]: 
                    d3 = EuclideanDistance(SL[i], SR[j])
                    # point1 = EuclideanDistance(SL[j], SR[i])[1]
                    # point2 = EuclideanDistance(SL[j], SR[i])[2]
        #output
        return d3
            

def EuclideanDistance(a, b):
    # return np.sqrt(np.sum((a - b)**2))
    # print(a, b)
    # print(np.linalg.norm(a-b))
    return np.linalg.norm(a-b), a, b


def sortList(S):
    return S[S[:,0].argsort()]
