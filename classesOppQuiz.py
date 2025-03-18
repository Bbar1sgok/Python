# Question 1
"""
def toplama(a,b):
    print(a,b)

x = toplama(3,4)

REPLY: none because does not return

"""
# Question 2 , 3
def usselIslem (x = 5, y = 3):
    print(x**y)

# 2
usselIslem(2,4)

# REPLY: 16

# 3

usselIslem()

# REPLY : 125

# Question 4
# What will be the output of the following code?

my_loop = [3,2,1,5,3,4]

def myLoop (*args):
    for element in args:
        print(element/2)


# REPLY: [1.5, 1, 0.5, 2.5, 1.5, 2]

# Question 5
# Apply the numbers given in the array below to myFunction and create a new array.

myList = [2,3,4,5,6,7]
newMyList = []
def myFunc(num):
    return num ** 3

for num in myList:
    newMyList.append(myFunc(num))

print(newMyList)

# Question 6
# Create a new list with the barcodes containing XYZ in the following sequence

barcodeList = ["ABC231", "SA3123XYZ", "XYZA123Q", "QRE1231KS", "X112QGL"]

print(list(filter(lambda string : "XYZ" in string, barcodeList)))

# Question 7
# cat.ageMultiply() = ?

class cat():
    def __init__(self, name, age = 5):
        self.name = name
        self.age = age

    def multiplyTheAge(self):
        return self.age * 3

# REPLY:  cat.ageMultiply() = 15

# Question 8
# What will be the output of the following code?

class Student():

    def __init__(self, name, quizNote):
        self.name = name
        self.__quizNote = quizNote
    def show_Note(self):
        print(f"{self.name} Quiz Note {self.quizNote}")

# student = Student("Yusuf", 85) => REPLY: Yusuf Quiz Note 85






