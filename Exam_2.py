"""

Q1 – Q1
A thread is a flow of execution and each thread is responsible of a separate flow of control. Multithreading is running different programs at the same time.
Q1 – Q2
concurrency is when multiple threads are running at the same time.
Q1 – Q3
It is a memory management strategy where unused objects are deleted to free up memory, the method tracks and identifies each object that can be deleted in the program.
Q1 – Q4
Transactions are one or more statements that can be executed and the database data has been changed as a result of it
Q1 – Q 5
The endpoint of the API is the sources of the API which is on the server side. Examples of the API methods are GET, POST and DELETE.
Q1 – Q6
Data normalization – a process that allows us to design a database to ask better questions
Primary Key Constraint – a table only has one primary key assigned to the column where it contains unique values.
Foreign key constraint – this is the column/s that refers to the primary key in another table, creating a link between the two tables.
Having primary and foreign key constraints, relational databases can be created to ensure the data integrity.

Q2
Exception Handling
Exceptions are raised when there is an error in a function/program and it needs to be handled. Python has inbuilt keywords such as try and except to handle the exceptions that may occur.
Try is used to include statements that we may expect an exception. If there is indeed an exception, except will handle the exception by raising an error message. If there is no error, else keyword allows execution of the code when no exceptions are found. Finally keyword can be used to execute a block of code by skipping the results of the try/except statements.
Python debugging
assertation statement is used by testing a condition, whether it returns false or true. If false, we’ll receive an assertion error (can include an error message). This allows the developer to find debug faster.


"""

# Task 3
def square(list):
    list.sort()
    if len(list) > 0:
        return[i ** 2 for i in list]
    if len(list) == 0:
        return False

# result = square([6,5,4])
# print(result)

#Task 4
"""
Three unit tests to test 1) the function does not taker non-empty arrays as it returns False when the list is empty.
2) to test if the square function returns the squared numbers we expect.
3) to test the order of the list returned as a result of the function, which it should be ascending.
Unit test is used as its good to test individual functions/components 
"""
from unittest import TestCase, main
from Exam_2 import square

class MyTestCase(TestCase):

    def test_empty_list(self):
        expected = False
        result = square(list=[])
        self.assertEqual(result,expected)

    def test_square_calc(self):
        expected = [4,25]
        result = square(list=[2,5])
        self.assertEqual(result,expected)

    def test_order(self):
        expected = [9,16,36]
        result = square(list=[3,6,4])
        self.assertEqual(result,expected)

if __name__ == '__main__':
    main()


"""
Q 5
1.	Scrum master – they are usually heading and scrum team and is held accountable for the teams effectiveness. Scrum masters are responsible of holding daily scrum meetings and helping developers to understand/refine the backlog items by also collaborating with product owners, discussing what is prioritised for the sprint. 
2.	Product owner – they maximise the value of the product that the developers are working on. They are responsible of the backlog management, i.e. bring in new features and make sure the tickets are written concisely for developers to work on. They also set the ordering of the product backlog items and this is communicated to the scrum master. 

Q6 
TDD
Advantages: 
1.	Since TDD allows a developer to write simple code to get the test to pass, it prevents developers to write code that is not required. Keeping the codebase simple. 
2.	Flexible, it is easier to refactor as every piece of code is tested so changes do not cause easy breakages
3.	Codebase will be easy to test as codes were written to get the tests to pass, and it suggests high test coverage as every feature has tests to cover it
Disadvantages: 
1.	All members of team are required to implement TDD, this leads to inconsistency 
2.	Maintenance required when code is refactored / requirements change 
3.	Slow – long planning 

Q7
Python DB cursor allows us to fetch data from the database. We would  have to initialise the cursor object as below:
mycursor = db.cursor()

db should be connected to a database, i.e. with host/user/password included to enable the access to SQL.
The cursor object includes an execution method to execute a query, i.e. to create a new database. 
mycursor.execute("CREATE DATABASE myfabdatabase")

alternatively, it could execute to select the data.
mycursor.execute("SELECT * FROM EMPLOYEE")

Then the cursor can be closed be calling, mycursor.close()
Q8 

SELECT max(purch_amt), customer_id
FROM ordersinfo.orders
GROUP BY customer_id
HAVING customer_id between 3002 AND 3007 AND max(purch_amt) > 1000

"""
#Task 9

nums = [ 3, 5, -4, 8, 11, 1, -1, 6]
t_sum = 9
def num_sum (nums, t_sum):
    for i in range(0, len(nums)):
        for x in range(i + 1, len(nums)):
            total = nums[i] + nums[x]
            if (total == t_sum):
               return (nums[i], nums[x])
    return -1
result = num_sum (nums, t_sum)
print(list(result))

