#region imports
import distributed.utils_test
import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
import random as rnd
import mplcursors as mplc
#endregion

# region class definitions
class errBarInfo():
    # region constructor
    def __init__(self, ff=0, ffMean=0, ffStDev=0):
        """
        Constructor for errBarInfo
        :param ff: 
        :param ffMean:
        :param ffStDev:
        """
        # region instance variables
        self.ff=ff
        self.ffMean=ffMean
        self.ffStDev=ffStDev
        # endregion
    # endregion

class PointOnMoodyChart():
    # region constructor
    """
    This is a class for storing a ff, Re pair
    """
    def __init__(self, Re=3000, ff=0.02, ebi=errBarInfo()):
        """
        Constructor for the PointOnMoodyChart class.
        :param Re: the Reynolds Number
        :param ff: the frection factor
        :param ebi:  the error bar info
        """
        # region instance variables (fields)
        self.Re=Re
        self.ff=ff
        self.ebi=ebi
        # endregion
    # endregion

class MoodyChart():
    # region constructor
    def __init__(self):
        """
        Constructor for MoodyChart class
        """
        # region instance variables (fields)
        self.ReValsCB=[]
        self.ReValsL=[]
        self.ReValsTrans=[]
        self.rrVals=[]
        self.ffLam=[]
        self.ffTrans=[]
        self.ffCB=[]
        self.ffCBTrans=[]
        self.makeData()
        self.ffRePoints=[]
        # endregion
    # endregion

    # region methods
    def ff(self, Re, rr, CBEQN=False):
        """
        This function calculates the friction factor for a pipe based on the
        notion of laminar, turbulent and transitional flow.
        :param Re: the Reynolds number under question.
        :param rr: the relative pipe roughness (expect between 0 and 0.05)
        :param CBEQN:  boolean to indicate if I should use Colebrook (True) or laminar equation
        :return: the (Darcy) friction factor
        """
        if(CBEQN):
            # note:  in numpy log is for natural log.  log10 is log base 10.
            cb=lambda f: 1/(f**0.5)+2.0*np.log10(rr/3.7+2.51/(Re*f**0.5))
            result= fsolve(cb,(0.001))
            #  val=cb(result[0])
            return result[0]
        else:
            return 64/Re

    def makeData(self):
        # Step 1:  create logspace arrays for ranges of Re
        self.ReValsCB = np.logspace(np.log10(4000.0), 8, 100)  # for use with Colebrook equation
        self.ReValsL = np.logspace(np.log10(600.0), np.log10(2000.0), 20)  # for use with Laminar flow
        self.ReValsTrans = np.logspace(np.log10(2000), np.log10(4000), 20)  # for use with Transition flow
        # Step 2:  create array for range of rr
        self.rrVals = np.array(
            [0, 1E-6, 5E-6, 1E-5, 5E-5, 1E-4, 2E-4, 4E-4, 6E-4, 8E-4, 1E-3, 2E-3, 4E-3, 6E-3, 8E-8, 1.5E-2, 2E-2, 3E-2,
             4E-2, 5E-2])

        # Step 2:  calculate the friction factor in the laminar range
        self.ffLam = np.array([self.ff(re, 0, False) for re in self.ReValsL])
        self.ffTrans = np.array([self.ff(re, 0, False) for re in self.ReValsTrans])

        # Step 3:  calculate friction factor values for each rr at each Re for turbulent range.
        self.ffCB = np.array([[self.ff(re, relRough, True) for re in self.ReValsCB] for relRough in self.rrVals])
        self.ffCBTrans=np.array([[self.ff(re, relRough, True) for re in self.ReValsTrans] for relRough in self.rrVals])

    def plotMoody(self, plotPoint=False, P=PointOnMoodyChart()):
        """
        This function produces the Moody diagram for a Re range from 1 to 10^8 and
        for relative roughness from 0 to 0.05 (20 steps).  The laminar region is described
        by the simple relationship of f=64/Re whereas the turbulent region is described by
        the Colebrook equation.
        :param plotPoint:  boolean to indicate if I should plot a particular point
        :param ebInfo:  a tuple with (Re, ReMean, ReStDev) for plotting error bars in transisition region
        :return: just shows the plot, nothing returned
        """

        #Step 4:  construct the plot
        plt.loglog(self.ReValsL, self.ffLam[:], color='k')
        plt.loglog(self.ReValsTrans, self.ffTrans[:], linestyle='dashed', color='k')
        ax = plt.gca()
        for nRelR in range(len(self.ffCB)):
            plt.loglog(self.ReValsCB, self.ffCB[nRelR], color='k', label=nRelR)
            plt.loglog(self.ReValsTrans, self.ffCBTrans[nRelR], color='k', label=nRelR, linestyle='dashed')
            plt.annotate(xy=(1E8,self.ffCB[nRelR][-1]),text=self.rrVals[nRelR])

        plt.xlim(600,1E8)
        plt.ylim(0.008, 0.10)
        plt.xlabel(r"Reynolds number $Re = \frac{Vd}{\nu}$", fontsize=16)
        plt.ylabel(r"Friction factor $f=\frac{h}{\left(\frac{L}{d}\cdot \frac{V^2}{2g}\right)}$", fontsize=16)
        plt.text(2.5E8,0.02,r"Relative roughness $\frac{\epsilon}{d}$",rotation=90, fontsize=16)
        ax = plt.gca()
        ax.tick_params(axis='both', which='both', direction='in', top=True, right=True, labelsize=12)  # format tick marks
        ax.tick_params(axis='both', grid_linewidth=1, grid_linestyle='solid', grid_alpha=0.5)
        ax.tick_params(axis='y', which='minor')
        ax.yaxis.set_minor_formatter(FormatStrFormatter("%.3f"))
        plt.grid(which='both')
        if(plotPoint):
            self.ffRePoints.append(P)
            for P in self.ffRePoints:
                if (P.Re<2000 or P.Re>4000):
                    plt.plot(P.Re, P.ff , marker='o', markersize=12, markeredgecolor='red', markerfacecolor='none')
                else:
                    plt.errorbar(P.Re, P.ebi.ffMean, yerr=P.ebi.ffStDev, capsize=8, ecolor='black')
                    plt.plot(P.Re, P.ebi.ffMean, marker="_", markersize=12, markeredgecolor='black', markerfacecolor='none')
                    plt.plot(P.Re, P.ff, marker='^', markersize=12, markeredgecolor='red', markerfacecolor='none')
        mplc.cursor(ax)
        plt.show()
        pass
    # endregion

class PointedMoodyChart():
    # region constructor
    def __init__(self):
        # region class variables (fields)
        self.MP=MoodyChart()
        self.pt=PointOnMoodyChart()
        # endregion
    # endregion

    # region class functions (methods)
    def ffPoint(self, Re, rr):
        """
        This function takes Re and rr as parameters and outputs a friction factor according to the following:
        1.  if Re>4000 use Colebrook Equation
        2.  if Re<2000 use f=64/Re
        3.  else calculate a probabilistic friction factor where the distribution has a mean midway between the prediction
            of the f=64/Re and Colebrook Equations and a standard deviation of 20% of this mean
        :param Re:  the Reynolds number
        :param rr:  the relative roughness
        :return:  the friction factor
        """
        if Re >= 4000:
            self.pt=PointOnMoodyChart(Re, self.MP.ff(Re, rr, CBEQN=True))
            self.pt.ebi=errBarInfo(self.pt.ff, self.pt.ff,0)
            return
        if Re <= 2000:
            self.pt=PointOnMoodyChart(Re, self.MP.ff(Re, rr))
            self.pt.ebi=errBarInfo(self.pt.ff, self.pt.ff,0)
            return
        CBff = self.MP.ff(Re, rr, CBEQN=True)
        Lamff = self.MP.ff(Re, rr)
        mean =Lamff+(Re-2000)/(4000-2000)* (CBff - Lamff)
        sig = 0.2 * mean
        ff=rnd.normalvariate(mean, sig)
        self.pt=PointOnMoodyChart(Re, ff,errBarInfo(ff, mean, sig))
        return

    def plotPoint(self, Re, rr, keepOldPts=True):
        """
        This calls the function plotMoody from MP
        :param Re: The Reynolds number for the point
        :param rr: The relative roughness for the point
        :param keepOldPts: boolean to tell if I should keep the old points on the plot
        :return:
        """
        if not keepOldPts: self.MP.ffRePoints.clear()
        self.ffPoint(Re, rr)
        self.MP.plotMoody(plotPoint=True, P=self.pt)
    # endregion
# endregion

# region function definitions
def main():
    """
    This program creates a PointedMoodyChart object and then prompts the user for a Re and a relative roughness and
    then plots the point on a Moody diagram using pyplot.  Once the plot closes, it asks if you want to plot another
    point.
    :return:
    """
    pmp=PointedMoodyChart()
    ReLast=3000.0
    rrLast=0.0
    TF=True
    while (TF):
        Re=float(input("Enter the Reynolds number [{:.3e}]:  ".format(ReLast)) or ReLast)
        rr=float(input("Enter the relative roughness [{:.6e}]:  ".format(rrLast)) or rrLast)
        ReLast=Re
        rrLast=rr
        pmp.plotPoint(Re, rr)
        tf=input("Try another point ([Y]/N)?").lower() or 'yes'
        TF=tf in ('y', 'yes')
# endregion

# region funciton calls
if __name__=="__main__":
    main()  # entry point to start the program
# endregion