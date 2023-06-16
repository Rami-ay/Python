"""Imports:"""
import math
import random
"""
Student Name : Rami Ayoub
Login Name : ramiay
Student ID : 315478966
"""

"""1st Question Overview:
classes for different shapes, and a collection class to manage a list of these shapes.
 It also includes methods to calculate properties of these shapes such as area, perimeter,
and < operand to compare and sort the shapes based on their area.
"""


"""2ndd Question Overview:
defining three classes: Person, Bank_account and it's subclass Student_account.
Person holds information about a person,Bank_account stores a person's account number, balance, and personal information
from the Person class.
In addition, two functions to create and manage accounts.
the create_bank_account function takes from user his information and creates account for him.
manage_bank_account function asks the user for the desired operations and keep an account history file.

"""
# ================= 1st Question =================
"""General class of shapes:"""

class Shape:

    """function that returns the area
                        of the shape:"""
    def area(self):
        pass
    """function that returns the perimeter 
                        of the shape:"""
    def perimeter(self):
        pass

    """Less operand that compares two 
                        shapes according to their area"""
    def __lt__(self, other):
        return self.area() < other.area()


"""Circle that inherits from the Shape class"""


class Circle(Shape):
    """Constructor that takes radius as input
                        and store it as private member"""
    def __init__(self, radius):
        """if radius <= 0 , save the radius as 1:"""
        if radius <= 0:
            self.__radius = 1
        else:
            self.__radius = radius

    """function that sets a new value 
                            of the radius"""
    def set_radius(self, new_val):
        if new_val > 0:
            self.__radius = new_val

    """function that returns the radius value:"""
    def get_radius(self):
        return self.__radius

    """presenting the object:"""
    def __str__(self):
        return "Circle: radius = " + str(self.__radius)

    """overwriting the area function from shape:"""
    def area(self):
        return math.pi*self.__radius**2

    """overwriting the perimeter function"""
    def perimeter(self):
        return 2 * math.pi * self.__radius


"""Rectangle that inherits from the Shape class"""


class Rectangle(Shape):
    """Constructor that takes width and height as input
                        and store them as private members"""
    def __init__(self, width, height):
        if width <= 0:
            self.__width = 1
        else:
            self.__width = width

        if height <= 0:
            self.__height = 1
        else:
            self.__height = height

    """function that returns the width"""
    def get_width(self):
        return self.__width

    """function that returns the height"""
    def get_height(self):
        return self.__height

    """function that sets the width"""
    def set_width(self, new_val):
        if new_val > 0:
            self.__width = new_val

    """function that sets the height"""
    def set_height(self, new_val):
        if new_val > 0:
            self.__height = new_val

    """presenting the object:"""
    def __str__(self):
        return f"Rectangle: width = {self.__width}, height = {self.__height}"

    """function that returns the area of rectangle"""
    def area(self):
        return self.__width * self.__height

    """function that returns the perimeter of rectangle"""
    def perimeter(self):
        return 2 * (self.__width + self.__height)


"""Square that inherits from the Rectangle class"""


class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)

    """presenting the object:"""
    def __str__(self):
        return "Square: length = {}".format(self.get_width())


"""ShapesCollection Class:"""


class ShapesCollection:

    def __init__(self):
        self.__shapes = []

    """return the length of the list:"""
    def __len__(self):
        return len(self.__shapes)

    """getting the item index from the list:"""
    def __getitem__(self, index):
        return self.__shapes[index]
    """set the item index in the list:"""
    def __setitem__(self, index, value):
        self.__shapes[index] = value

    """inserting shape to the list according to the size:"""
    def insert(self, new_shape):
        # check that the input is a Shape:
        if not isinstance(new_shape, Shape):
            raise ValueError("Input must be a Shape object")

        # find the placement for the new shape:
        index = len(self.__shapes)
        for i, shape in enumerate(self.__shapes):
            if new_shape < shape:
                index = i
                break

        # insert the shape at the calculated index
        self.__shapes.insert(index, new_shape)

    """presenting the object:"""
    def __str__(self):
        shapes_str = "Shapes in collection:\n"
        for shape in self.__shapes:
            shapes_str += str(shape) + "\n"
        return shapes_str

    def biggest_perimeter_diff(self):
        """
        Returns the biggest difference in perimeters of any two shapes in the list
        """
        # check that the list has at least two shapes
        if len(self.__shapes) < 2:
            return None

        max_diff = 0
        # iterate over all pairs of shapes and calculate the difference in their perimeters
        for i in range(len(self.__shapes)):
            for j in range(i + 1, len(self.__shapes)):
                diff = abs(self.__shapes[i].perimeter() - self.__shapes[j].perimeter())
                if diff > max_diff:
                    max_diff = diff

        return max_diff

    def same_area_as(self, s):
        """
        Returns a list that contains all the shapes from the list that have an area equal to the area of s
        """
        same_area_shapes = []
        for shape in self.__shapes:
            if shape.area() == s.area():
                same_area_shapes.append(shape)
        return same_area_shapes

    def how_many_quadrilaterals(self):
        """
        Returns the number of rectangles and squares in the list
        """
        num_quadrilaterals = 0
        for shape in self.__shapes:
            if isinstance(shape, Rectangle) or isinstance(shape, Square):
                num_quadrilaterals += 1
        return num_quadrilaterals


# ================= 2nd Question =================


class Person:
    def __init__(self, first_name, last_name, address, id_number):
        if not first_name.isalpha():
            self.__first_name = "Avi"
        else:
            self.__first_name = first_name

        if not last_name.isalpha():
            self.__last_name = "Cohen"
        else:
            self.__last_name = last_name
        if not id_number.isdigit():
            self.__id = "300010000"
        else:
            self.__id = id

        self.__address = address

    @property
    def first_name(self):
        return self.__first_name

    @property
    def id(self):
        return self.__id

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, value):
        self.__last_name = value

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, value):
        self.__address = value


class Bank_account:
    """Initializes a Bank_account object with an account number
                    , a person object, and a balance amount"""
    def __init__(self, acc_num, person, money):
        self.account_number = acc_num
        if not isinstance(person, Person):
            raise TypeError("Didn't insert Person Class")
        else:
            self.person = person
        if not isinstance(money, (int, float)):
            raise ValueError("Didn't insert money as digits value")
        else:
            self.balance = money

    """Presentation of the class"""
    def __str__(self):
        return f"Account: {self.account_number}\nName: {self.person.first_name} {self.person.last_name}\nBalance: {self.balance}"

    """Adding money to account, after substracting fee of 5"""
    def add_money(self, value):
        self.balance += (value-5)

    """Taking money from account, after substracting fee of 5"""
    def take_money(self, value):
        if self.balance - value < 0:
            return "Operation Failed\n"
        else:
            self.balance -= (value+5)
    """print the current account status"""
    def check_account(self):
        print(self.balance)




class Student_account(Bank_account):
    """Iinit student account"""
    def __init__(self, acc_num, person, money, univ):
        super().__init__(acc_num, person, money)
        self.university = univ

    """presenting the class:"""
    def __str__(self):
        return f"Student Account: {self.account_number}\nName: {self.person.first_name} {self.person.last_name}\nBalance: {self.balance}"

    """Adding money from account , after substracting fee of 3"""
    def add_money(self, value):
        self.balance += (value-3)

    """Taking money from account , after substracting fee of 3"""
    def take_money(self, value):
        if self.balance - value < 0:
            return "Operation Failed\n"
        else:
            self.balance -= (value+3)

#Operations on the Bank Account:
"""function that asks the user for his information and creates an account for him:"""
def create_bank_account():
    """Ask the user for his info and making account"""
    first_name = input("Please enter your first name: ")
    last_name = input("Please enter your last name: ")
    address = input("Please enter your address: ")
    id_num = input("Please enter your ID number: ")
    balance = input("Please enter your account balance: ")
    account_type = input("Please enter your account type (regular/student): ")
    university = ""
    if account_type.lower() == "student":
        university = input("Please enter the name of your university: ")
        account = Student_account(random.randint(0, 1000), Person(first_name, last_name, address, id_num), int(balance), university)
    else:
        account = Bank_account(random.randint(0, 1000), Person(first_name, last_name, address, id_num), int(balance))
    return account

"""function that asks the user for the desired operation and handles it,
the function runs in infinite loop until the user inserts finish"""
def manage_bank_account(account):
    """opening a file to contain the operations history:"""
    file_name = f"account_history.txt"
    with open(file_name, 'w') as file:
        file.write(f"New account, balance: {account.balance}\n")
    """in infinite loop until the user inserts finish:
                    handle the user's operations:"""
    while True:
        operation = input("Please enter an operation (withdraw/deposit/print/print history/finish): ")
        if operation.lower() == "withdraw":
            amount = int(input("Please enter the amount to withdraw: "))
            result = account.take_money(amount)
            if result == "Operation Failed\n":
                print(result)
                with open(file_name, 'a') as file:
                    file.write(f"Tried to withdraw {amount} and failed\n")
            else:
                print("Operation Successful\n")
                with open(file_name, 'a') as file:
                    file.write(f"Withdraw {amount}, balance: {account.balance}\n")
        elif operation.lower() == "deposit":
            amount = int(input("Please enter the amount to deposit: "))
            account.add_money(amount)
            print("Operation Successful")
            with open(file_name, 'a') as file:
                file.write(f"Deposit {amount}, balance: {account.balance}\n")
        elif operation.lower() == "print":
            print(account)
        elif operation.lower() == "print history":
            with open(file_name, 'r') as file:
                print(file.read())
        elif operation.lower() == "finish":
            print("Thank You\n")
            break
        else:
            print("Invalid Operation")


while(True):
    ex_num = (input("Please Enter The Exercise Number (1/2) : "))
    if (ex_num == '1'):
        print("Please Tester, Have Mercy :)")
    elif(ex_num == '2'):
        account = create_bank_account()
        manage_bank_account(account)
    else:
        print("Exercise Number is Not Valid, Try Again!")
