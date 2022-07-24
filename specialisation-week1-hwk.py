"""

TASK 1

Write a class to represent a Cash Register.
You class should keep the state of price total and purchased items

Below is a starter code:
------------------------
1. you can add new variables and function if you want to
2. you will NEED to add accepted method parameters where required.
For example, method add_item probably accepts some kind of an item?..
3. You will need to write some examples of how your code works.

"""
from functools import reduce
from datetime import datetime


class CashRegister:
    # init method is called when we create object for a class
    def __init__(self, discount=0):
        # we want to make total_items into a dictionary, dict() function is called to create a dictionary
        self.total_items = dict()  # {'item': 'price'}
        self.total_price = 0
        # passing discount as a parameter
        self.discount = discount
        self.itemCount = 0
        self.change = 0
        self.quantity = dict()

    # discount
    def update_discount(self, new_discount):
        self.discount = new_discount

    def add_item(self, item, price, quantity):
        # passing the item and price parameters as we need to know the info
        self.total_items[item] = price
        #  update new key item with price

        self.quantity[item] = quantity
        # update quantity dict, item: number of quantity

    def remove_item(self, item):
        # remove an item from the dict of total_items
        self.total_items.pop(item)

    def apply_discount(self):
        """
        Apply a discount to the total price of this purchase. For example,
        %10 discount on a total pric of £50

        EXAMPLE:
        new price = 50 - (50 / 10) = 45
        :return: updated total_price
        """
        try:
            price = self.total_price - (self.total_price / self.discount)
        except ZeroDivisionError:
            print("No discount available")
        else:
            self.total_price = price

    def get_total(self):
        # calculate the new prices for each item depending on the quantity
        self.total_price = sum(
            self.total_items[key] * self.quantity[key] for key in self.total_items)
        self.apply_discount()

    def show_items(self):
        msg = """
        {}
        =========================
        Items purchased
        ---------------
        {}    
        TOTAL: {}
        
        -------Thank you!--------
        =========================
        """
        width = 25  # length of the receipt / char
        records = []

        for k, v in self.total_items.items():
            # length of the key and len of the value (k,v)
            txt = len(k)
            digits = len(str(v))
            # adding thq quantity to the receipt
            qty = "..x {}".format(str(self.quantity[k]))
            char = width - txt - digits - len(qty)
            r = "{}{}{}{}".format(k, '.' * char, v, qty)
            records.append(r)
        # joined up the records
        all_records = '\n        '.join(records)
        # adding a time stamp
        time = datetime.now()

        final_msg = msg.format(time, all_records, self.total_price)
        #  return the final message
        print(final_msg)

    def reset_register(self):
        # reset all variables to zero
        self.total_price = 0
        self.total_items.clear()
        self.discount = 0

    # calculating the 20% tax rate of the order
    def calc_tax(self):
        tax = self.total_price * 0.2
        return tax

    # counting total items
    def count_items(self):
        self.itemCount = len(self.total_items.keys())
        return self.itemCount

    # calc change
    def calc_change(self, cash):
        self.change = cash - self.total_price
        return self.change


# EXAMPLE code run:

register = CashRegister(discount=10)
register.add_item('beans', 1.99, 4)
register.add_item('carrots', 0.55, 2)
register.total_items
register.get_total()
register.total_price
register.show_items()
register.calc_tax()
# register.reset_register()


"""

TASK 2

Write a base class to represent a student. Below is a starter code. 
Feel free to add any more new features to your class. 
As a minimum a student has a name and age and a unique ID.

Create a new subclass from student to represent a concrete student doing a specialization, for example:
Software Student and Data Science student. 

"""


# class Student:

#     def __init__(self, name, age, id):
#         self.name = name
#         self.age = age
#         self.id = id
#         self.subjects = dict()


# class CFGStudent(<should inherit from Student>)
#     create new methods that manage student's subects (add/remove new subject and its graade to the dict)
#     create a method to view all subjects taken by a student
#     create a method  (and a new variable) to get student's overall mark (use average)


class Student:

    def __init__(self, name, age, _id):
        self.name = name
        self.age = age
        self.id = _id
        self.subjects = dict()  # subject_name: mark
        self.attendance = dict()
        # adding attendance as a dict,with value of a list that contains each lesson's attendance, so either 0 or 100
        # student_name: []

    def add_subjects(self, list_of_subjects):
        # passing a list of subjects
        for subj in list_of_subjects:
            # subjects equals to none as marks are unknown,therefore null, subj: None
            self.subjects[subj] = None


class CFGStudent(Student):
    # inherited from Student by passing in Student. The variables in student is made available.

    def __init__(self, stream, *args, **kwargs):
        # args and kwargs allows you to add arguments
        super().__init__(*args, **kwargs)
        self.specialization = stream
        self.overall_mark = None

    # managing subjects
    def add_subject(self, subject):
        self.subjects[subject] = None

    def remove_subject(self, subject):
        self.subjects.pop(subject)

    # view all subjects by calling the keys in a list by calling a list constructor
    def view_subjects(self):
        return list(self.subjects.keys())

    def update_grade(self, subject, grade):
        self.subjects[subject] = grade

    #
    def get_overall_mark(self):
        # dict comprehension, going through all the subjects and if value is none, this is going to be left out from the total
        current = dict(
            {(k, v) for k, v in self.subjects.items() if v is not None})
        return sum(current.values()) / len(current.values())
        # filtered values / length of the values

    def add_attendance(self, name, attendance):
        self.attendance[name] = attendance

    def view_attendance(self):
        return self.attendance.items()

    # calculating students attendance
    def calculate_overall_attendance(self):
        list_of_attendances = self.attendance.values()
        for e in list_of_attendances:
            for i in e:
                pass
        return reduce(lambda a, b: a + b, e) / len(e)


s = CFGStudent(name="y", age=25, _id=17912, stream='software')
s.add_subject(subject="foundation")
s.update_grade(subject="foundation", grade=90)
s.add_subject(subject="specialization")
s.update_grade(subject="specialization", grade=100)
s.get_overall_mark()
s.add_attendance(name='y', attendance=[100, 0, 100, 100])
