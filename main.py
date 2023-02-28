from functions import *

S = np.array([[2,3],[12,30],[40,50],[5,1],[12,10],[3,4]])
S2 = np.array([[1,3,0,1],[12,30,0,1],[40,50,0,1],[5,1,0,0],[12,10,0,0],[3,4,0,1]])
#Result = 1.41421

lower_bound = 0
upper_bound = 1000
dimension = 3

# Stest = np.array([[1,1,0],[3,0,1],[7,8,9]])
Stest = np.array([[4,3,1],[3,1,0],[3,3,4],[4,3,0]])
Stest2 = np.array([[78, 75],[80, 85],[78, 20],[57, 47], [4, 80]])
Stest3 = np.array([[79,40],
 [56, 21],
 [87 ,96],
 [67 ,73],
 [71 ,58]])
Stest4 = np.array([[51, 32],[51, 32],[78, 20],[57, 47], [4, 80]])
Stest5 = np.array([[51, 32],[51, 32],[78, 20], [4, 80]])
Stest6 = np.array([[42, 91],
 [95, 17],
 [17, 96],
 [87, 37],
 [74,  8],
 [15, 41],
 [22,  9],
 [96, 25],
 [ 1, 48],
 [36, 25],
 [29, 49],
 [60, 69],
 [ 9,  4],
 [16, 93],
 [82, 57],
 [ 0, 25],
 [55, 73],
 [80,  1],
 [ 6, 50],
 [20, 60],
 [49, 19],
 [ 9, 45],
 [40, 54],
 [98, 32],
 [48, 44],
 [93, 95],
 [25, 30],
 [59, 38],
 [ 2, 44],
 [38, 23],
 [49, 76],
 [24, 91],
 [36, 47],
 [31, 77],
 [49,  4],
 [67, 74],
 [61,  7],
 [ 7,  8],
 [78, 50],
 [52, 26],
 [92, 58],
 [58, 94],
 [75, 81],
 [55,  4],
 [29, 66],
 [97, 98],
 [57, 69],
 [37, 83],
 [21, 69],
 [10, 65],
 [63, 50],
 [69, 73],
 [29,  5],
 [84, 43],
 [40, 14],
 [55, 22],
 [12, 56],
 [89, 73],
 [68,  3],
 [54, 26],
 [13, 15],
 [ 3, 88],
 [83, 82],
 [82, 83],
 [20, 94],
 [71, 90],
 [ 0, 70],
 [41, 95],
 [13, 51],
 [ 9, 55],
 [98, 38],
 [58,  8],
 [25, 75],
 [29, 65],
 [26,  2],
 [95, 22],
 [30, 41],
 [66, 79],
 [25, 91],
 [97, 52],
 [69,  7],
 [48, 97],
 [95,  3],
 [49, 96],
 [85, 74],
 [64, 76],
 [13, 63],
 [ 0, 68],
 [60, 17],
 [23, 35]])
# Stest = np.array([[1,0,0],[2,0,1],[2,0,2]])
# print(EuclideanDistance(Stest[0], Stest[1]))

print("Masukan banyak titik")
n = int(input("n = "))
List_Points = np.empty((0,dimension), int)
print()
for i in range(n):
    # print("Masukan titik ke-", i+1, ": ")
    # x1 = int(input())
    # x2 = int(input())
    # x3 = int(input())
    # print()
    # List_Points = np.append(List_Points, np.array([[x1,x2,x3]]), axis=0)
    List_Points = np.append(List_Points, np.random.randint(lower_bound, upper_bound, size=(1, dimension)), axis=0)

# List_Points = np.append(List_Points, np.array([[7, 8, 9]]), axis=0)
# print(Stest)
print(List_Points)
# print(DivNCon(sortList(Stest)))

List_PointsBruteForce = List_Points.copy()
# hasil = DivNCon(sortList(List_Points))
# hasilB = BruteForce(sortList(List_PointsBruteForce))
id = np.arange(len(List_Points))[:, np.newaxis]
print(id)
#print(np.concatenate((id,List_Points), axis = 1))
hasilD = DivNConBigD(sortListAxis(np.concatenate((id, List_Points), axis = 1),0), dimension, 0)
hasil = DivNCon(sortList(List_Points), dimension)
hasilB, brute = BruteForce(sortList(List_Points))  
print("titik 1 D= ", List_Points[hasilD[1]])
print("titik 2 D= ", List_Points[hasilD[2]])
print(hasilD[0])
print("titik 1 = ", hasil[1])
print("titik 2 = ", hasil[2])
print(hasil[0])

print()
print("titik 1 Brute = ", hasilB[1])
print("titik 2 Brute = ", hasilB[2])
print(hasilB[0])
# from viz import *

print()
if (hasil[0] == hasilB[0]):
    print("Hasil sama")
else:
    print("SALAHH")

    
print(getDivcon())
print(getDivcon2())
print(brute)