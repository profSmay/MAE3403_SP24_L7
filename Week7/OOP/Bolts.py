# region class definitions
#a ScrewThread class
class ScrewThread():
    # region constructor
    def __init__(self, system='SAE', handed='right',diam='1/4',pitch='1/20',lead='1/20'):
        """
        :param str system:
        :param str handed:
        :param str diam:
        :param str pitch:
        :param str lead:
        """
        # region class variables (fields)
        self.sys=system
        self.hand=handed
        self.dia=diam
        self.pitch=pitch
        self.lead=lead
        # endregion
    # endregion

    # region class functions (methods)
    def PrintProps(self):
        """
        Prints the properties of the object
        :return:
        """
        print('System=',self.sys)
        print('Handedness=',self.hand)
        print('Diameter=',self.dia)
        print('Pitch=',self.pitch)
        print('Lead=', self.lead)
    # endregion

#a Bolt class
class Bolt():
    # region constructor
    def __init__(self, thread, grade, headtype, length):
        """
        Constructor for Bolt
        :param ScrewThread thread: a ScrewThread object
        :param int grade: a grade for hardness of bolt
        :param str headtype: type of head for the bolt
        :param float length: length of the bolt
        """
        self.thread=thread
        self.grade=grade
        self.headtype=headtype
        self.length=length
    # endregion

    # region class functions (methods)
    def PrintProps(self):
        print('Bolt properties:')
        print('Grade=',self.grade)
        print('Head Type=',self.headtype)
        print('Length=',self.length)
        print('Thread properties:')
        self.thread.PrintProps()
    # endregion
# endregion

# region function definitions
def main():
    st = ScrewThread()
    pitch = st.pitch
    st2 = ScrewThread('metric','right', '6', '1','1')
    system=st2.sys
    mybolt=Bolt(ScrewThread('SAE','right','0.25 in', '1/20 in', '1/20 in'), 5, 'socket', 1.0)
    mybolt.PrintProps()
# endregion

# region function calls
if __name__ == "__main__":
    main()
# endregion