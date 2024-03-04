#region imports
import datetime as dt
#endregion

#region class definitions
#a class for a person
class Person():
    #region constructor
    def __init__(self, name, YearOfBirth):
        '''
        Default constructor for a Person.
        :param name: property of person
        :param YearOfBirth: property of person
        '''
        self.name=name
        self.BirthYear=YearOfBirth
    #endregion
    #region methods
    def GetYearsOld(self):
        return dt.datetime.now().year-self.BirthYear
    #endregion

#demonstration of class inheritance
class Employee(Person):
    #region constructor
    def __init__(self,name, YearOfBirth,PhoneNum,Company):
        '''
        This is the default constructor for class Employee which inherits from Person
        We don't employee non-persons
        :param name: property of parent
        :param YearOfBirth: property of parent
        :param PhoneNum: property of employee
        :param Company: property of employee
        '''
        #call constructor of parent class
        super().__init__( name, YearOfBirth)
        self.Phone=PhoneNum
        self.Company=Company

    @classmethod
    def makeEmployee(cls, person, PhoneNum, Company):
        return cls(person.name,person.BirthYear,PhoneNum, Company)
    #endregion
    #region methods
    def PrintPhoneNumber(self):
        print(self.Phone)
    #endregion
class Company():
    #region constructor
    def __init__(self, Employees):
        '''
        This is the default constructor for the Company class
        Note: Employees argument is not an instance variable.  I need to copy the objects from Employees
        to an instance variable if I want to remember them after the constructor
        :param Employees: an array of Employee objects
        '''
        self.Employees=[]
        for e in Employees:
            self.Employees.append(e)
    #endregion
    #region methods
    def PrintPhoneBook(self):
        for e in self.Employees:
            print(e.name, ":", e.Phone)
    #endregion

#endregion

#region function definitions
def main():
    """
    This main function creates three Employee objects and then a Company object and prints the phonebook of the company.
    :return:
    """
    Joe=Employee('Joe Biden', '1943', '555-203-7839','Democratic Politician')
    theBern=Person('Bernie Sanders', '1942')
    Bernie=Employee(theBern.name,theBern.BirthYear, '555-786-5309','Socialist Politician')
    Liz=Person('Elizabeth Warren','1950')
    Elizabeth=Employee.makeEmployee(Liz, '555-836-2211','Democratic Politician')

    DNC=Company([Joe, Bernie, Elizabeth])
    DNC.PrintPhoneBook()
#endregion

#region function calls
if __name__=='__main__':
    main()
#endregion