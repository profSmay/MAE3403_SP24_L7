#region class definitions
class ScrewThread():
    #constructor
    def __init__(self, system, handed,diam,pitch,lead):
        #fields/properties of the class
        #can be accesses publicly
        self.sys=system
        self.hand=handed
        self.dia=diam
        self.pitch=pitch
        self.lead=lead

    #method 1
    def PrintProps(self):
        print('System=',self.sys)
        print('Handedness=',self.hand)
        print('Diameter=',self.dia)
        print('Pitch=',self.pitch)
        print('Lead=', self.lead)
#endregion

#region function definitions
def main():
    # create an object of this class
    s1=ScrewThread('SAE', 'Right',0.25,28,0)
    s1.PrintProps()
#endregion

#region function calls
if __name__=='__main__':
    main()
#endregion