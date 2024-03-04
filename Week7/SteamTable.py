#region imports
import numpy as np
from scipy.interpolate import griddata
#import pyXSteam.XSteam as xsteam
#endregion

#region functions
def main():
    """
    This function illustrates the reading and parsing of data by numpy loadtxt and interpolation using griddata.
    We are reading in data for superheated water, which is tabulated for various T at several different isobars.
    We know that for pure substances in a single phase region, we need two independent thermodynamic variables
    to calculate ALL other intensive thermodynamic properties.
    Notes:
    1.  I need to know the structure of the .txt file to make this work properly.  Don't assume.
    2.  The first row can be skipped if it contains heading information or can be read for labels
    :return: nothing to return
    """
    tcol, hcol,scol,pcol=np.loadtxt('superheated_water_table.txt', skiprows=1, unpack=True)

    pval=90 #kpa
    tval=250 #C

    # Note, all of these are double interpolations.  In ENSC thermodynamics, we used (double) linear interpolation, but
    # griddata can use Lagrange polynomials for interpolation, or splines.  We can use it as a black box without
    # specifying the method OR can specify the method.
    h=float(griddata((tcol,pcol),hcol,(tval,pval),'linear'))  # interpolate tcol, pcol to find h given tval, pval
    s=float(griddata((tcol,pcol),scol,(tval,pval),'linear'))
    t=float(griddata((hcol,pcol),tcol,(h+500,pval),'linear'))

    # steamtable=xsteam.XSteam(xsteam.XSteam.UNIT_SYSTEM_MKS)
    # ppval=pval/101.5  # must work in bar
    # hh=steamtable.h_pt(ppval, tval)
    # ss=steamtable.s_pt(ppval,tval)
    # tt=steamtable.t_ph(ppval, hh+500)
    print(h,s,t)
#endregion

#region function calls
if __name__=="__main__":
    main()
#endregion