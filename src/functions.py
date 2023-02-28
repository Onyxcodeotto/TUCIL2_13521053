import numpy as np
from math import *
from sort import *

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
    else:
        if(D>2):
            d1 = DivNConBigD(S[:floor(len(S)/2)], D, start)
            d2 = DivNConBigD(S[floor(len(S)/2):], D, start)
            ### Get median and Sparse###
            
            if (d1[0] <= d2[0]):
                d3 = d1
            else:
                d3 = d2
            SL = np.empty((0,D+start+1), float)
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
            SL = np.empty((0,D+start+1), float)
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
                    
        

def DivNCon(S, D, count):
    # S: Set of points
    # D: Dimension
    # count: Frekuensi pemanggilan fungsi EuclideanDistanceBF
    #Brute Force untuk len(S)<=3#
    if (len(S)==3):
        d2, count = DivNCon(S[1:3], D, count)
        dm1 = EuclideanDistanceBF(S[0], S[1])
        dm2 = EuclideanDistanceBF(S[0], S[2])
        count +=2
        if d2[0] <=  dm1[0] and d2[0] <= dm2[0]:
            return d2, count
        elif dm1[0] <= dm2[0] and dm1[0] <= d2[0]:
            return dm1,count 
        else:
            return dm2, count
        
    elif(len(S) == 2):
        count+=1
        return EuclideanDistanceBF(S[0],S[1]), count
    
    
    else:
        d1, count = DivNCon(S[:floor(len(S)/2)], D,count)
        d2,count = DivNCon(S[floor(len(S)/2):], D,count)
        if (d1[0] <= d2[0]):
            d3 = d1
        else:
            d3 = d2
        SL = np.empty((0,D), float)
        if(len(S) %2 == 0):
            L= (S[floor(len(S)/2)][0] + S[floor(len(S)/2)-1][0])/2
        else:
            L  = S[floor(len(S)/2)][0]
        
        rDistLeft = L - d3[0]
        rDistRight = L + d3[0]
        for i in range(len(S)):
            if rDistRight>= S[i][0] >= rDistLeft and S[i][0] <= rDistRight:
                SL = np.append(SL,[S[i]], axis = 0)  

        
        if (D != 1):
            sortListY(SL)
            for i in range(len(SL)):
                j= i+1
                while(j<len(SL) and SL[j][1] - SL[i][1]<d3[0]):
                    count +=1
                    temp = EuclideanDistanceBF(SL[i], SL[j])
                    if temp[0] <= d3[0]:
                        d3 = temp
                    j+=1
        else:
            for i in range(len(SL)):
                j = i+1
                while j<len(S) and SL[j][0] - SL[i][0]<d3[0]:
                    temp = EuclideanDistanceBF(SL[i], SL[j])
                    count+=1
                    if (temp[0] <= d3[0]):
                        d3 = temp
        return d3, count
        
                

def EuclideanDistanceBF(a, b):
    # return np.sqrt(np.sum((a - b)**2))
    # print(a, b)
    # print(np.linalg.norm(a-b))
    return np.linalg.norm(a-b), a, b

def DivNConEuclideanDistance(a,b):
    return np.linalg.norm(a[1:]-b[1:]), a[0], b[0]
    
def BruteForce(S):
    brute = 0
    d = EuclideanDistanceBF(S[0], S[1])
    brute +=1
    for i in range(len(S)):
        for j in range(i+1, len(S)):
            brute+=1
            temp = EuclideanDistanceBF(S[i], S[j])
            if temp[0] < d[0]:
                d = temp
    return d, brute
