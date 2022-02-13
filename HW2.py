# HW2
# Due Date: 09/24/2021, 11:59PM
# REMINDER: The work in this assignment must be your own original work and must be completed alone.

import random


#Stores id, name and number of credits for a course.
class Course:
    '''
        >>> c1 = Course('CMPSC132', 'Programming in Python II', 3)
        >>> c2 = Course('CMPSC360', 'Discrete Mathematics', 3)
        >>> c1 == c2
        False
        >>> c3 = Course('CMPSC132', 'Programming in Python II', 3)
        >>> c1 == c3
        True
        >>> c1
        CMPSC132(3): Programming in Python II
        >>> c2
        CMPSC360(3): Discrete Mathematics
        >>> c3
        CMPSC132(3): Programming in Python II
        >>> c1 == None
        False
        >>> print(c1)
        CMPSC132(3): Programming in Python II
    '''

    #Initializes the values of Course
    def __init__(self, cid, cname, credits):
        self.cid = cid
        self.cname = cname
        self.credits = credits


    #Returns string in cid(credits): cname format
    def __str__(self):
        return f'{self.cid}({self.credits}): {self.cname}'



    __repr__ = __str__

    #Checks if two courses are equal based on course id
    def __eq__(self, other):
        if not isinstance(other, Course):
            return False
        return self.cid == other.cid

#Stores collection of course objects and their capacity in an accessible, modifiable dictionary
class Catalog:
    ''' 
        >>> C = Catalog()
        >>> C.addCourse('CMPSC132', 'Programming in Python II', 3, 400)
        'Course added successfully'
        >>> C.addCourse('CMPSC360', 'Discrete Mathematics', 3, 200)
        'Course added successfully'
        >>> C.courseOfferings
        {'CMPSC132': (CMPSC132(3): Programming in Python II, 400), 'CMPSC360': (CMPSC360(3): Discrete Mathematics, 200)}
        >>> C.removeCourse('CMPSC360')
        'Course removed successfully'
        >>> C.courseOfferings
        {'CMPSC132': (CMPSC132(3): Programming in Python II, 400)}
        >>> isinstance(C.courseOfferings['CMPSC132'][0], Course)
        True
    '''

    #Sets Catalog to be empty at start
    def __init__(self):
        self.courseOfferings = {}


    #Adds a course to the catalog
    #Returns a string on whether a course has been added or not
    def addCourse(self, cid, cname, credits, capacity):
        if cid in self.courseOfferings.keys():
            return "Course already added"
        self.courseOfferings[cid] = (Course(cid, cname, credits), capacity)
        return "Course added successfully"


    #Removes a course from the catalog
    #Returns a string on whether a course was successfully removed or not
    def removeCourse(self, cid):
        if not (cid in self.courseOfferings.keys()):
            return "Course not found"
        del self.courseOfferings[cid]
        return "Course removed successfully"

#Stores collection of course objects for a student (based on each semester)
class Semester:
    '''
        >>> cmpsc131 = Course('CMPSC131', 'Programming in Python I', 3)
        >>> cmpsc132 = Course('CMPSC132', 'Programming in Python II', 3)
        >>> math230 = Course("MATH 230", 'Calculus', 4)
        >>> phys213 = Course("PHYS 213", 'General Physics', 2)
        >>> econ102 = Course("ECON 102", 'Intro to Economics', 3)
        >>> phil119 = Course("PHIL 119", 'Ethical Leadership', 3)
        >>> semester = Semester(1)
        >>> semester
        No courses
        >>> semester.addCourse(cmpsc132)
        >>> isinstance(semester.courses['CMPSC132'], Course)
        True
        >>> semester.addCourse(math230)
        >>> semester
        CMPSC132, MATH 230
        >>> semester.isFullTime
        False
        >>> semester.totalCredits
        7
        >>> semester.addCourse(phys213)
        >>> semester.addCourse(econ102)
        >>> semester.addCourse(econ102)
        'Course already added'
        >>> semester.addCourse(phil119)
        >>> semester.isFullTime
        True
        >>> semester.dropCourse(phil119)
        >>> semester.addCourse(Course("JAPNS 001", 'Japanese I', 4))
        >>> semester.totalCredits
        16
        >>> semester.dropCourse(cmpsc131)
        'No such course'
        >>> semester.courses
        {'CMPSC132': CMPSC132(3): Programming in Python II, 'MATH 230': MATH 230(4): Calculus, 'PHYS 213': PHYS 213(2): General Physics, 'ECON 102': ECON 102(3): Intro to Economics, 'JAPNS 001': JAPNS 001(4): Japanese I}
    '''
    
    #Initializes courses to be empty and semester number is assigned
    def __init__(self, sem_num):
        self.sem_num = sem_num
        self.courses = {}

    #Returns all the courses in this semester in cid, cid, ... cid format
    def __str__(self):
        if len(self.courses) == 0:
            return "No courses"
        message = ""
        for key in self.courses:
            message = message + f'{self.courses[key].cid}, '
        return message[:-2]


    __repr__ = __str__

    #Adds a course to current semester
    #Returns a string if course is already added
    def addCourse(self, course):
        if (course.cid in self.courses.keys()):
            return "Course already added"
        self.courses[course.cid] = course


    #Removes a course from the current semester
    #Returns a string if no such course is there
    def dropCourse(self, course):
        if not (course.cid in self.courses.keys()):
            return "No such course"
        del self.courses[course.cid]


    #Returns the total number of credits (cumulative sum) taken this semester
    @property
    def totalCredits(self):
        total = 0
        for key in self.courses:
            total += self.courses[key].credits
        return total

    #Returns a boolean depending on whether this is a full time schedule or not
    @property
    def isFullTime(self):
        return self.totalCredits >= 12
    

#Simple class to represent amount of money taken out by a loan with a unique id
class Loan:
    '''
        >>> import random
        >>> random.seed(2)  # Setting seed to a fixed value, so you can predict what numbers the random module will generate
        >>> first_loan = Loan(4000)
        >>> first_loan
        Balance: $4000
        >>> first_loan.loan_id
        17412
        >>> second_loan = Loan(6000)
        >>> second_loan.amount
        6000
        >>> second_loan.loan_id
        22004
        >>> third_loan = Loan(1000)
        >>> third_loan.loan_id
        21124
    '''
    
    #Creates a new loan with an amount and unique id
    def __init__(self, amount):
        self.loan_id = self.__getloanID 
        self.amount = amount

    #Returns the balance on the loan
    def __str__(self):
        return f'Balance: ${self.amount}'


    __repr__ = __str__

    
    #Creates a unique id using a pseudorandom number generator
    @property
    def __getloanID(self):
        return random.randint(10000, 99999)


#Stores the name and social security of a person
class Person:
    '''
        >>> p1 = Person('Jason Lee', '204-99-2890')
        >>> p2 = Person('Karen Lee', '247-01-2670')
        >>> p1
        Person(Jason Lee, ***-**-2890)
        >>> p2
        Person(Karen Lee, ***-**-2670)
        >>> p3 = Person('Karen Smith', '247-01-2670')
        >>> p3
        Person(Karen Smith, ***-**-2670)
        >>> p2 == p3
        True
        >>> p1 == p2
        False
    '''
    
    #Creates a person object with a public name attribute and private ssn attribute
    def __init__(self, name, ssn):
        self.name = name
        self.__ssn = ssn

    #Returns a string in the format Person(name, ***-**-1234)
    def __str__(self):
        return f'Person({self.name}, ***-**-{self.__ssn[-4:]})'

    __repr__ = __str__

    #Getter function for social security number
    def get_ssn(self):
        return self.__ssn

    #Determine if two person objects are the same if their social security numbers are the same
    def __eq__(self, other):
        return isinstance(other, Person) and (self.get_ssn()  == other.get_ssn())

#Staff inherits from Person, adds new functions that manage student objects
class Staff(Person):
    '''
        >>> C = Catalog()
        >>> C.addCourse('CMPSC132', 'Programming in Python II', 3, 400)
        'Course added successfully'
        >>> C.addCourse('CMPSC360', 'Discrete Mathematics', 3, 200)
        'Course added successfully'
        >>> s1 = Staff('Jane Doe', '214-49-2890')
        >>> s1.getSupervisor
        >>> s2 = Staff('John Doe', '614-49-6590', s1)
        >>> s2.getSupervisor
        Staff(Jane Doe, 905jd2890)
        >>> s1 == s2
        False
        >>> s2.id
        '905jd6590'
        >>> p = Person('Jason Smith', '221-11-2629')
        >>> st1 = s1.createStudent(p)
        >>> isinstance(st1, Student)
        True
        >>> s2.applyHold(st1)
        'Completed!'
        >>> st1.registerSemester()
        'Unsuccessful operation'
        >>> s2.removeHold(st1)
        'Completed!'
        >>> st1.registerSemester()
        >>> st1.enrollCourse('CMPSC132', C,1)
        'Course added successfully'
        >>> st1.semesters
        {1: CMPSC132}
        >>> s1.applyHold(st1)
        'Completed!'
        >>> st1.enrollCourse('CMPSC360', C, 1)
        'Unsuccessful operation'
        >>> st1.semesters
        {1: CMPSC132}
    '''

    #Creates a new person and adds staff.__supervisor attribute
    def __init__(self, name, ssn, supervisor=None):
        super().__init__(name,ssn)
        self.__supervisor = supervisor

    #Returns a string in the format Staff(name, id)
    def __str__(self): 
        return f'Staff({self.name}, {self.id})'

    __repr__ = __str__


    #Returns staff id in the format 905abc1234, where abc is the initals 
    #and 1234 are the last four digits of their SSN
    @property
    def id(self):
        #names include first, middle, last names
        names = self.name.split()
        idStr = "905"
        for name in names:
            idStr = idStr + name[0]
        idStr = idStr + self.get_ssn()[-4:]
        return idStr.lower()

    #Returns the supervisor of the current instance
    @property   
    def getSupervisor(self):
        return self.__supervisor

    
    #Sets a supervisor value for current instance
    def setSupervisor(self, new_supervisor):
        if isinstance(new_supervisor, Staff):
           self.__supervisor = new_supervisor
           return "Completed!"

    #Sets hold value to true for a student instance
    def applyHold(self, student):
        if isinstance(student, Student):
            student.hold = True
            return "Completed!"

    #Sets hold value to false for a student instance
    def removeHold(self, student):
        if isinstance(student, Student):
            student.hold = False
            return "Completed!"

    #Sets active value to false for a student instance
    def unenrollStudent(self, student):
        if isinstance(student, Student):
            student.active = False
            return "Completed!"

    #Creates a new student instance based off of a person instance
    def createStudent(self, person):
        if isinstance(person, Person):
            return Student(person.name, person.get_ssn(), "Freshman")


#Student is inherited from Person, has ability to manage courses and finances
class Student(Person):
    '''
        >>> C = Catalog()
        >>> C.addCourse('CMPSC132', 'Programming in Python II', 3, 400)
        'Course added successfully'
        >>> C.addCourse('CMPSC360', 'Discrete Mathematics', 3, 200)
        'Course added successfully'
        >>> s1 = Student('Jason Lee', '204-99-2890', 'Freshman')
        >>> s1
        Student(Jason Lee, jl2890, Freshman)
        >>> s2 = Student('Karen Lee', '247-01-2670', 'Freshman')
        >>> s2
        Student(Karen Lee, kl2670, Freshman)
        >>> s1 == s2
        False
        >>> s1.id
        'jl2890'
        >>> s2.id
        'kl2670'
        >>> s1.registerSemester()
        >>> s1.enrollCourse('CMPSC132', C,1)
        'Course added successfully'
        >>> s1.semesters
        {1: CMPSC132}
        >>> s1.enrollCourse('CMPSC360', C, 1)
        'Course added successfully'
        >>> s1.enrollCourse('CMPSC311', C, 1)
        'Course not found'
        >>> s1.semesters
        {1: CMPSC132, CMPSC360}
        >>> s2.semesters
        {}
        >>> s1.enrollCourse('CMPSC132', C, 1)
        'Course already enrolled'
        >>> s1.dropCourse('CMPSC360')
        'Course dropped successfully'
        >>> s1.dropCourse('CMPSC360')
        'Course not found'
        >>> s1.semesters
        {1: CMPSC132}
        >>> s1.registerSemester()
        >>> s1.semesters
        {1: CMPSC132, 2: No courses}
        >>> s1.enrollCourse('CMPSC360', C, 2)
        'Course added successfully'
        >>> s1.semesters
        {1: CMPSC132, 2: CMPSC360}
        >>> s1.registerSemester()
        >>> s1.semesters
        {1: CMPSC132, 2: CMPSC360, 3: No courses}
        >>> s1
        Student(Jason Lee, jl2890, Sophomore)

    >>> jane_doe = Staff('Jane Doe', '214-49-2890')
    >>> p = Person('Jason Smith', '221-11-2629')
    >>> s = jane_doe.createStudent(p)
    >>> s
    Student(Jason Smith, js2629, Freshman)
    >>> s.year, s.semesters
    'Freshman',{}
    >>> s.account
    Name: Jason Smith
    ID: js2629
    Balance: $0
    >>> C = Catalog()
    >>> C.addCourse('CMPSC132', 'Programming in Python II', 3, 400)
    'Course added successfully'
    >>> C.addCourse('CMPSC360', 'Discrete Mathematics', 3, 200)
    'Course added successfully'
    >>> C.removeCourse('CMPSC360')
    'Course removed successfully'
    >>> C.addCourse('MATH 230', 'Calculus', 4, 700)
    'Course added successfully'
    >>> C.addCourse('PHYS 213', 'General Physics', 2, 500)
    'Course added successfully'
    >>> C.courseOfferings
    {'CMPSC132': (CMPSC132(3): Programming in Python II, 400), 'MATH 230': (MATH 230(4): Calculus, 700), 'PHYS 213': (PHYS 213(2): General Physics, 500)}
    >>> s.registerSemester()
    >>> s.enrollCourse('CMPSC132', C,1)
    'Course added successfully'
    >>> s.semesters
    {1: CMPSC132}
    '''
    #Creates a new student based off of person
    #By default:
    #Semesters is empty
    #hold is False
    #active is True
    def __init__(self, name, ssn, year):
        random.seed(1)
        super().__init__(name, ssn)
        self.year = year
        #Private variable sem_num represents which semester they are.
        #Defaults to these values based on year based on how many semesters they should have
        #already completed.
        semesterMap = {"Freshman":0, "Sophomore":2,"Junior":4,"Senior":6}
        self.__sem_num = semesterMap[year]
        self.semesters = {}
        self.hold = False
        self.active = True
        self.account = self.__createStudentAccount()
        

    #Returns a string in the format: Student(name, id, yera)
    def __str__(self):
        return f'Student({self.name}, {self.id}, {self.year})'

    __repr__ = __str__

    #If the student is active, a new student account will be made
    def __createStudentAccount(self):
        if self.active:
            return StudentAccount(self)

    #Creates an id in the format of abc1234 where abc is the student's initials
    #and 1234 are the last four digits of their SSN
    @property
    def id(self):
        #names include first, middle, last names
        names = self.name.split()
        idStr = ""
        for name in names:
            idStr = idStr + name[0]
        idStr = idStr + str(self.get_ssn())[-4:]
        return idStr.lower()

    #Registers for a semester
    #Updates semester number and year standing
    #Returns a string if there is a hold or inactivity
    def registerSemester(self):
        if ((not self.active) or (self.hold)):
            return "Unsuccessful operation"
        self.__sem_num += 1
        self.semesters[self.__sem_num] = Semester(self.__sem_num)
        if self.__sem_num > 6:
            self.year = "Senior"
        else:
            semesterMap = {1:"Freshman",2:"Freshman",3:"Sophomore",4:"Sophomore",5:"Junior",6:"Junior"}
            self.year = semesterMap[self.__sem_num]

    #Adds a course to a student's semester schedule 
    #and adds a charge to their student account
    #Returns a string based on how the task was completed
    def enrollCourse(self, cid, catalog, semester):
        if not self.active or self.hold or not semester in self.semesters.keys():
            return "Unsuccessful operation"
        if not (cid in catalog.courseOfferings.keys()):
            return "Course not found"
        returnValue = self.semesters[semester].addCourse(catalog.courseOfferings[cid][0])
        if not returnValue:
            cost = catalog.courseOfferings[cid][0].credits * StudentAccount.CREDIT_PRICE
            self.account.chargeAccount(cost)
            return "Course added successfully"
        return "Course already enrolled"

    #Removes a course from a student's current semester schedule
    #and adds a refund to their student account
    #Returns a string based on how the task was completed
    def dropCourse(self, cid):
        if not self.active or self.hold: 
            return "Unsuccessful operation"
        if cid in self.semesters[self.__sem_num].courses.keys():
            refund = 0.5 * self.semesters[self.__sem_num].courses[cid].credits * StudentAccount.CREDIT_PRICE
            del self.semesters[self.__sem_num].courses[cid]
            self.account.makePayment(refund)
            return "Course dropped successfully"

        return "Course not found"
    
    #Adds a loan to the student's student account
    #Uses loan money to make a payment to student account balance
    #Returns a string if task was unsuccessful
    def getLoan(self, amount):
        if not self.active:
            return "Unsuccessful operation"
        if self.semesters[self.__sem_num].isFullTime:
            newLoan = Loan(amount)
            self.account.loans[newLoan.loan_id] = newLoan
            self.account.makePayment(amount)
            return None
        return "Not full-time"


#A class that represents a student's finances
class StudentAccount:
    '''
        >>> C = Catalog()
        >>> C.addCourse('CMPSC132', 'Programming in Python II', 3, 400)
        'Course added successfully'
        >>> C.addCourse('CMPSC360', 'Discrete Mathematics', 3, 200)
        'Course added successfully'
        >>> C.addCourse('MATH 230', 'Calculus', 4, 600)
        'Course added successfully'
        >>> C.addCourse('PHYS 213', 'General Physics', 2, 500)
        'Course added successfully'
        >>> C.addCourse('CMPEN270', 'Digital Design', 4, 300)
        'Course added successfully'
        >>> s1 = Student('Jason Lee', '204-99-2890', 'Freshman')
        >>> s1.registerSemester()
        >>> s1.enrollCourse('CMPSC132', C,1)
        'Course added successfully'
        >>> s1.account.balance
        3000
        >>> s1.enrollCourse('CMPSC360', C, 1)
        'Course added successfully'
        >>> s1.account.balance
        6000
        >>> s1.enrollCourse('MATH 230', C,1)
        'Course added successfully'
        >>> s1.enrollCourse('PHYS 213', C,1)
        'Course added successfully'
        >>> print(s1.account)
        Name: Jason Lee
        ID: jl2890
        Balance: $12000
        >>> s1.account.chargeAccount(100)
        12100
        >>> s1.account.balance
        12100
        >>> s1.account.makePayment(200)
        11900
        >>> s1.getLoan(4000)
        >>> s1.account.balance
        7900
        >>> s1.getLoan(8000)
        >>> s1.account.balance
        -100
        >>> s1.enrollCourse('CMPEN270', C,1)
        'Course added successfully'
        >>> s1.account.balance
        3900
        >>> s1.dropCourse('CMPEN270')
        'Course dropped successfully'
        >>> s1.account.balance
        1900.0
        >>> s1.account.loans
        {27611: Balance: $4000, 84606: Balance: $8000}
        >>> StudentAccount.CREDIT_PRICE = 1500
        >>> s2 = Student('Thomas Wang', '123-45-6789', 'Freshman')
        >>> s2.registerSemester()
        >>> s2.enrollCourse('CMPSC132', C,1)
        'Course added successfully'
        >>> s2.account.balance
        4500
        >>> s1.enrollCourse('CMPEN270', C,1)
        'Course added successfully'
        >>> s1.account.balance
        7900.0
    '''

    #Cost per credit
    CREDIT_PRICE = 1000
    
    #Initializes student account to have empty loans dictionary and 0 balance
    def __init__(self, student):
        self.student = student
        #The amount of money the student has to pay
        self.balance = 0
        self.loans = {}

    #Returns info about student account in the format of:
    #Name: name
    #ID: abc1234
    #Balance: $0000
    def __str__(self):
        return f'Name: {self.student.name}\nID: {self.student.id}\nBalance: ${self.balance}'

    __repr__ = __str__

    #Reduces balance by amount
    def makePayment(self, amount):
        self.balance -= amount
        return self.balance
    
    #Increases balance by amount
    def chargeAccount(self, amount):
        self.balance += amount
        return self.balance




#############################################################################################
#print(StudentAccount.cost)
if __name__=='__main__':
    import doctest
    doctest.testmod()     # Uncomment this line to run all docstrings
    doctest.run_docstring_examples(Student, globals(), name='HW2',verbose=True)   # Replace Course with the name of the class you want to run its doctest
