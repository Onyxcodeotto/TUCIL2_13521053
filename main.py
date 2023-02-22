import numpy as np
from functions import *
print("Hello")

# print(euclideanDistance(np.array([3,0,0]), np.array([0,4,1])))
#Result = 1.41421
S = np.array([[2,3],[12,30],[40,50],[5,1],[12,10],[3,4]])
S2 = np.array([[1,3,0,1],[12,30,0,1],[40,50,0,1],[5,1,0,0],[12,10,0,0],[3,4,0,1]])

print("Masukan banyak titik ")
n = int(input("n = "))
List_Points = np.empty((0,4), int)
print()
for i in range(n):
    print("Masukan titik ke-", i+1, ": ")
    x1 = int(input())
    x2 = int(input())
    x3 = int(input())
    print()
    List_Points = np.append(List_Points, np.array([[x1,x2,x3]]), axis=0)
    # List_Points = np.append(List_Points, np.random.randint(0, 5, (1, 3), int), axis=0)
print(S2)
# List_Points = np.append(List_Points, np.array([[7, 8, 9]]), axis=0)

print()
print()
print(List_Points)
    
# print(DivNCon(sortList(List_Points)))
