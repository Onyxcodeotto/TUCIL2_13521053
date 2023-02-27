import numpy as np
from math import *

divcon = 0
def getDivcon():
    global divcon
    return divcon
def DivNConBigD(S,D, start):
    global divcon
    # S: Set of points
    # D: Dimension
    # start: start loop
    # O(n)=n (log(n))^(d-1)
    if (len(S)==3):
        d2 = DivNConBigD(S[1:3], D, start)
        dm1 = DivNConEuclideanDistance(S[0], S[1])
        dm2 = DivNConEuclideanDistance(S[0], S[2])
        divcon +=2
        if d2[0] <=  dm1[0] and d2[0] <= dm2[0]:
            return d2
        elif dm1[0] <= dm2[0] and dm1[0] <= d2[0]:
            return dm1
        else:
            return dm2
        
    elif(len(S) == 2):
        divcon +=1
        return DivNConEuclideanDistance(S[0],S[1])
    elif (len(S)==0):
        while(True):
            n=0
    else:
        if(D>2):
            d1 = DivNConBigD(S[:floor(len(S)/2)], D, start)
            d2 = DivNConBigD(S[floor(len(S)/2):], D, start)
            ### Get median and Sparse###
            
            if (d1[0] <= d2[0]):
                d3 = d1
            else:
                d3 = d2
            SL = np.empty((0,D+start+1), int)
            if(len(S) %2 == 0):
                L= (S[floor(len(S)/2)][start + 1] + S[floor(len(S)/2)-1][start + 1])/2
            else:
                L  = S[floor(len(S)/2)][start + 1]
            for i in range(len(S)):
                if S[i][start+1] > L+d3[0]:
                    break
                if(S[i][start +1] <=L + d3[0] and (S[i][start + 1] >=L - d3[0])):
                    SL = np.append(SL,[S[i]], axis = 0)         
            
            if(len(SL)<2):
                return d3
            else:
                d4 = DivNConBigD(sortListAxis(SL, start+1), D-1, start+1)    
                if d4[0]<d3[0]:
                    return d4
                else:
                    return d3

        else:
            d1 = DivNConBigD(S[:floor(len(S)/2)], D, start)
            d2 = DivNConBigD(S[floor(len(S)/2):], D, start)
            ### Get median and Sparse###
            if (d1[0] <= d2[0]):
                d3 = d1
            else:
                d3 = d2    
            ### Proses cari tengah ###
            ## Method 1: SL SR method ##
          
            ## Method 2 ##
            # Kelihatan O(n^2), tapi sebenarnya O(n) berdasarkan suatu pembuktian#
            #  #
            SL = np.empty((0,D+start+1), int)
            if(len(S) %2 == 0):
                L= (S[floor(len(S)/2)][start+1] + S[floor(len(S)/2)-1][start+1])/2
            else:
                L  = S[floor(len(S)/2)][start + 1]
            for i in range(len(S)):
                if S[i][start + 1] > L+d3[0]:
                    break
                if(S[i][start + 1] <=L + d3[0] and (S[i][start + 1] >=L - d3[0])):
                    SL = np.append(SL,[S[i]], axis = 0)     
            SL = sortListAxis(SL, start+1)#Sort first by y 
            d = d3 # d bisa saja nggak dibutuhkan
            if(len(SL)<2):
                return d3
            for i in range(len(SL)):
                for j in range(i+1, len(SL)):
                    if SL[i][start + 2] - SL[j][start + 2] > d[0]:
                        break
                    else:
                        divcon+=1
                        if(DivNConEuclideanDistance(SL[i], SL[j])[0] < d3[0]):
                            d3 = DivNConEuclideanDistance(SL[i], SL[j]) 
                            divcon += 1
            if d[0] > d3[0]:
                return d3
            else:
                return d            
                    
        
        


def DivNCon(S):
    if (len(S)==3):
        print("3 nih")
        print(S)
        d2 = DivNCon(S[1:3])
        dm1 = EuclideanDistanceBF(S[0], S[1])
        dm2 = EuclideanDistanceBF(S[0], S[2])
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
        return EuclideanDistanceBF(S[0],S[1])
    else:
        print("masuk sini")
        #Bagi rata
        print("nnn " + str(S[:floor(len(S)/2)]))
        print("nnn " + str(S[floor(len(S)/2):]))
        # print(floor(len(S)/2))
        # print(floor(len(S)/2)+1)
        # print(S[floor(len(S)/2)][0])
        # print(S[floor(len(S)/2)+1][0])
        """
        if (S[floor(len(S)/2)-1][0] != S[floor(len(S)/2)][0]):
            # print("yg bedaaaaaaa")
            L = (S[floor(len(S)/2) - 1][0] + S[floor(len(S)/2)][0])/2
            d1 = DivNCon(S[:floor(len(S)/2)])
            d2 = DivNCon(S[floor(len(S)/2):(len(S))])
        else:
            # print("yg samaaaaaaa")
            return DivNCon(S[floor(len(S)/2)-1:floor(len(S)/2)+1])
            # L = S[floor(len(S)/2)][0]
            """
        d1 = DivNCon(S[:floor(len(S)/2)])
        d2 = DivNCon(S[floor(len(S)/2):])
            
        
        
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
        if(len(S) %2 == 0):
            L= (S[floor(len(S)/2)][0] + floor(len(S)/2)-1)/2
        else:
            L  = S[floor(len(S)/2)][0]
        
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
                if EuclideanDistanceBF(SL[i], SR[j])[0] <= d3[0]:
                    d3 = EuclideanDistanceBF(SL[i], SR[j])
                    print("Distance " + str(d3[0]))
                    # point1 = EuclideanDistance(SL[j], SR[i])[1]
                    # point2 = EuclideanDistance(SL[j], SR[i])[2]
        #output
        return d3
    
         

def EuclideanDistanceBF(a, b):
    # return np.sqrt(np.sum((a - b)**2))
    # print(a, b)
    # print(np.linalg.norm(a-b))
    return np.linalg.norm(a-b), a, b

def DivNConEuclideanDistance(a,b):
    return np.linalg.norm(a[1:]-b[1:]), a[0], b[0]

def sortList(S):# Pake buat brute force saja
    return S[S[:,0].argsort()]
def sortListY(S):
    return S[S[:,2].argsort()]
def sortListAxis(S, axis):
    return S[S[:,axis+1].argsort()]
def BruteForce(S):
    brute = 0
    d = EuclideanDistanceBF(S[0], S[1])
    brute +=1
    for i in range(len(S)):
        for j in range(i+1, len(S)):
            brute+=1
            if EuclideanDistanceBF(S[i], S[j])[0] < d[0]:
                d = EuclideanDistanceBF(S[i], S[j])
                brute += 1
    return d, brute
