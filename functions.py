import numpy as np
from math import *

def DivNCon(S):
    if (len(S)==3):
        print("3 nih")
        print(S)
        d2 = DivNCon(S[1:3])
        dm1 = EuclideanDistance(S[0], S[1])
        dm2 = EuclideanDistance(S[0], S[2])
        if d2[0] <=  dm1[0] and d2[0] <= dm2[0]:
            return d2
        elif dm1[0] <= dm2[0] and dm1[0] <= d2[0]:
            return dm1
        else:
            return dm2
        # return min(d2, EuclideanDistance(S[0], S[1]), EuclideanDistance(S[0], S[2]))
        
    elif(len(S) == 2):
        print("2 nih")
        print(S)
        return EuclideanDistance(S[0],S[1])
    else:
        print("masuk sini")
        #Bagi rata
        print("nnn " + str(S[:floor(len(S)/2)]))
        print("nnn " + str(S[floor(len(S)/2):(len(S))]))
        # print(floor(len(S)/2))
        # print(floor(len(S)/2)+1)
        # print(S[floor(len(S)/2)][0])
        # print(S[floor(len(S)/2)+1][0])
        if (S[floor(len(S)/2)-1][0] != S[floor(len(S)/2)][0]):
            # print("yg bedaaaaaaa")
            L = (S[floor(len(S)/2) - 1][0] + S[floor(len(S)/2)][0])/2
            d1 = DivNCon(S[:floor(len(S)/2)])
            d2 = DivNCon(S[floor(len(S)/2):(len(S))])
        else:
            # print("yg samaaaaaaa")
            return DivNCon(S[floor(len(S)/2)-1:floor(len(S)/2)+1])
            # L = S[floor(len(S)/2)][0]
            # d1 = DivNCon(S[:floor(len(S)/2)+1])
            # d2 = DivNCon(S[floor(len(S)/2)+1:(len(S))])
            
        
        
        #solve middle
        if (d1[0] <= d2[0]):
            d3 = d1
        else:
            d3 = d2
        # d3 = min(d1,d2)
        # point1 = 
        SL = []
        SR = []
        # SMiddle = []
        # L  = S[floor(len(S)/2)][0]
        print("L nih " +str(L))
        rDistLeft = L - d3[0]
        rDistRight = L + d3[0]
        for i in range(len(S)):
            if S[i][0] >= rDistLeft and S[i][0] <= rDistRight:
                if S[i][0] > L:
                    SR.append(S[i])
                else:
                    SL.append(S[i])
        # print(SL)
        # print(SR)
        
        # for i in range(len(S[:floor(len(S)/2)])-1, -1, -1):
        #     if S[i][0] < L-d3[0]:
        #         break
        #     SL.append(S[i])
        # for i in range(0, len(S[floor(len(S)/2):-1])):
        #     if S[i][0] > L+d3[0]:
        #         break
        #     SR.append(S[i])
                
        for i in range(len(SL)):
            for j in range(len(SR)):
                if EuclideanDistance(SL[i], SR[j])[0] <= d3[0]:
                    d3 = EuclideanDistance(SL[i], SR[j])
                    print("Distance " + str(d3[0]))
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


def BruteForce(S):
    d = EuclideanDistance(S[0], S[1])
    for i in range(len(S)):
        for j in range(i+1, len(S)):
            if EuclideanDistance(S[i], S[j])[0] < d[0]:
                d = EuclideanDistance(S[i], S[j])
    return d