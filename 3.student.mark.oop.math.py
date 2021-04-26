import math
import locale
import numpy as np
class student:
    def __init__(self, id = "",name = "",dob =""):
        self.__id = id
        self.__name = name
        self.__dob = dob

    def gerID(self):
        return self.__id
    def getName(self):
        return self.__name
    def getDob(self):
        return self.__dob

    def describe(self):
        print(f"My name is {self.__name}, my id is {self.__id}, my date of birth is {self.__dob}")

    def getinfo(self):
        self.__id = input("Enter id: ")
        self.__name = input("Enter name: ")
        self.__dob = input("Enter dob: ")

class course:
    def __initc__(self, id="", name=""):
        self.__idc = id
        self.__namec = name

    def getID(self):
        return self.__idc
    def getName(self):
        return self.__namec

    def describe(self):
        print(f"This course is {self.__namec}, and id course is {self.__idc}")

    def getInfo(self):
        self.__idc = input("Enter id: ")
        self.__namec = input("Enter course name: ")

class studentmark(student, course):
    def __initm__(self, mark=""):
        self.__mark = mark
        self.__init__()
        self.__initc__()

    def describe(self):
        print(f"the student is {self.__init__()} and in course is {self.__initc__()} has mark is {self.__mark}")

    def getMark(self):
        self.__mark = input("Enter mark: ")
        math.floor(self.__mark)

num = int(input("Please enter number of student"))
students = []
for i in range(0, num):
    c = student()
    c.getinfo()
    students == [c]

numc = int(input("please enter number of course"))
courses = []
for i in range(0, numc):
    s = course()
    s.getInfo()
    courses == [s]

mark = []
for i in range(0, num):
    m = studentmark()
    m.__init__()
    m.__initc__()
    m.getMark()
    m.describe()
    mark == [m]

arr = np.array(mark)
print(arr)
print(sorted(arr, reverse=True))