# importing mplot3d toolkits, numpy and matplotlib
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
from main import *

fig = plt.figure()
pointHasilColor = 'red'
pointHasilColorB = 'yellow'
pointsColor = 'blue'
lineHasilColor = 'green'
lineHasilColorB = 'yellow'
lineWidthConts = 2

if (dimension == 3):
    ax = plt.axes(projection =str(dimension)+'d') 
    ax.invert_yaxis()
    # defining all 3 axis
    x = List_Points[:,0]
    y = List_Points[:,1]
    z = List_Points[:,2]
    Phasil = np.concatenate(([hasil[1]], [hasil[2]]), axis=0)
    # PhasilBrute = np.concatenate(([hasilB[1]], [hasilB[2]]), axis=0)

    xhasil = Phasil[:,0]
    yhasil = Phasil[:,1]
    zhasil = Phasil[:,2]
    # xhasilB = PhasilBrute[:,0]
    # yhasilB = PhasilBrute[:,1]
    # zhasilB = PhasilBrute[:,2]

    # plotting
    ax.plot3D(xhasil, yhasil, zhasil, lineHasilColor, linewidth = lineWidthConts)
    # ax.plot3D(xhasil, yhasil, zhasil, lineHasilColorB, linewidth = lineWidthConts)
    
    # make points
    ax.scatter3D( x, y, z, color = pointsColor)
    ax.scatter3D( xhasil, yhasil, zhasil, color = pointHasilColor)
    # ax.scatter3D( xhasil, yhasil, zhasil, color = pointHasilColorB)
    ax.set_title('3D line plot')
    ax.set_xlabel('x-axis')
    ax.set_ylabel('y-axis')
    ax.set_zlabel('z-axis')
    plt.show()
    
elif(dimension == 2 ):
    # defining all 3 axis
    x = List_Points[:,0]
    y = List_Points[:,1]
    Phasil = np.concatenate(([hasil[1]], [hasil[2]]), axis=0)
    # PhasilBrute = np.concatenate(([hasilB[1]], [hasilB[2]]), axis=0)
    
    xhasil = Phasil[:,0]
    yhasil = Phasil[:,1]
    # xhasilB = PhasilBrute[:,0]
    # yhasilB = PhasilBrute[:,1]
    
    # plotting
    plt.plot(xhasil, yhasil, lineHasilColor, linewidth = lineWidthConts)
    # plt.plot(xhasilB, yhasilB, lineHasilColorB, linewidth = lineWidthConts)
    
    # make points
    plt.scatter( x, y, color = pointsColor)
    plt.scatter( xhasil, yhasil, color = pointHasilColor)
    # plt.scatter( xhasilB, yhasilB, color = pointHasilColorB)
    plt.title('2D line plot')
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    plt.show()
    
elif (dimension == 1):
    # defining all 3 axis
    x = List_Points[:,0]
    y = np.array([0]*len(List_Points))
    Phasil = np.concatenate(([hasil[1]], [hasil[2]]), axis=0)
    # PhasilBrute = np.concatenate(([hasilB[1]], [hasilB[2]]), axis=0)

    xhasil = Phasil[:,0]
    yhasil = np.array([0]*len(Phasil))
    # xhasilB = PhasilBrute[:,0]
    # yhasilB = np.array([0]*len(PhasilBrute))
    
    # plotting
    plt.plot(xhasil, yhasil,  lineHasilColor, linewidth = lineWidthConts)
    # plt.plot(xhasilB, lineHasilColorB, linewidth = lineWidthConts)
    
    # make points
    plt.ylim([-1, 1])
    plt.scatter( x, y, color = pointsColor)
    plt.scatter( xhasil, yhasil, color = pointHasilColor)
    # plt.scatter( xhasilB, yhasilB, color = pointHasilColorB)
    plt.title('1D line plot')
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    plt.show()

else :
    print('Error plotting, dimension not supported')
    