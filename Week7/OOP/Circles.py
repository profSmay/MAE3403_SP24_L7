# region imorts
import math
# endregion

# region class definitions
class Circle():
    """
    A circle class
    """
    def __init__(self, xcenter=0, ycenter=0, radius=1):
        """
        The constructor for Circle
        :param xcenter: x center of the circle
        :param ycenter: y center of the circle
        :param radius: radius of the circle
        """
        #region member variables
        self.x=xcenter
        self.y=ycenter
        self.r=radius
        #endregion

    def Area(self):
        return math.pi*self.r**2

    def Circum(self):
        return math.pi*2*self.r

    def Type(self):
        return "Circle"

class Square(Circle):
    def __init__(self, c=None, sidelength=5):
        """
        Constructor for Square, which is a derived (child) class of Circle (parent)
        :param c: optional, a Circle object
        :param sidelength: the side length of the square
        """
        if c is not None:  # do this if c is set
            super().__init__(xcenter=c.x, ycenter=c.y)  # run constructor of parent class
            self.L=c.r
        else:
            super().__init__()  # run constructor of parent class
            self.L=sidelength

    def Area(self):  # redefining function Area overrides the parent class function Area
        return self.L**2

    def Circum(self):  # redefining function Circum overrides the parent class function Circum
        return 4*self.L

    def Type(self):  # redefining function Type overrides the parent class function Type
        return "Square"
# endregion

# region function definitions
def main():
    """
    This creates three circle objects and a square object.
    :return:
    """
    c1=Circle(1,2,3)  # create first circle object (an instance of Circle class)
    c2=Circle(0,0,4)  # create second circle object (an instance of Circle class)
    c3=Circle()  # create third circle object (an instance of Circle class)
    c3.x = 0
    c3.y = 1
    c3.r = 4
    s1=Square(c1)
    print('c1 has area={:0.3f} and circum={:0.3f}'.format(c1.Area(),c1.Circum()))
    print('c2 has area={:0.3f} and circum={:0.3f}'.format(c2.Area(),c2.Circum()))
    print('c3 has area={:0.3f} and circum={:0.3f}'.format(c3.Area(),c3.Circum()))
    print('s1 has area={:0.3f} and circum={:0.3f}'.format(s1.Area(),s1.Circum()))
# endregion

# region function calls
if __name__ == "__main__":
    main()
# endregion