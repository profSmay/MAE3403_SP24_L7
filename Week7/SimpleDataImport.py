#region imports
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import griddata as grd
from scipy.interpolate import interp1d
#endregion

#region functions
def main():
    #simply read in the Data File 1.txt
    dat = np.loadtxt('Data File 1.txt', skiprows=1)  # why skiprows=1?
    x=dat[:,0] #must slice numpy array to extract columns
    y=dat[:,1] #must slice numpy array to extract columns
    plt.plot(x,y, marker='o',linestyle='none', markeredgecolor='b', markerfacecolor='w')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

    #demonstrate unpack option in loadtxt and interp1d

    #read in Data File 1.txt with unpack=true
    xvals, yvals=np.loadtxt('Data File 1.txt', skiprows=1, unpack=True)

    xpt1=(xvals[4]-xvals[3])/3+xvals[3]
    # this is instantiation of an object of class interp1d
    f=interp1d(xvals,yvals, kind='linear')
    xpts=np.linspace(xvals.min(), xvals.max(),130)
    ypts=np.array([f(xpt) for xpt in xpts])
    ypt1=f(xpt1)
    plt.plot(xvals,yvals, marker='o',linestyle='none', markeredgecolor='r', markerfacecolor='w')
    plt.plot(xpts,ypts, marker='', linestyle='dashed')
    plt.plot(xpt1,ypt1, marker='v', linestyle='none')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()

    print(dat)
#endregion

#region function calls
if __name__=='__main__':
    main()
#endregion