from functions import *

S = np.array([[2,3],[12,30],[40,50],[5,1],[12,10],[3,4]])
S2 = np.array([[1,3,0,1],[12,30,0,1],[40,50,0,1],[5,1,0,0],[12,10,0,0],[3,4,0,1]])
#Result = 1.41421

lower_bound = 0
upper_bound = 100
dimension = 2

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
hasil = DivNCon(sortList(List_Points))
hasilB = BruteForce(sortList(List_PointsBruteForce))
# hasil = DivNCon(sortList(Stest3))
# hasilB = BruteForce(sortList(Stest3))  
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