# Classes provide a means of bundling data and functionality together. 
# Creating a new class creates a new type of object, allowing new instances of that type to be made.

class Student:
    """Common base class for all students"""
    student_count = 0

    def __init__(self, name, id):
        self.name = name
        self.id = id
        Student.student_count += 1

    def PrintStudentData(self):
        print("Name: ", self.name, "ID: ", self.id)


std1 = Student("Juma", 102)
std1.PrintStudentData()

# creating instance object
std2 = Student('wicked', '2020')
std2.PrintStudentData()

std3 = Student("Lyomu", 2580)
std4 = Student("Lydia", 8964)
std3.PrintStudentData()
std4.PrintStudentData()

# Accessing attributes
print("am accessing the attributes. the total students are: ", Student.student_count)

# # functions used to access attributes
# print("checking if std1 has the id attribute:", hasattr(std1, 'id'), "\n"
#                                                                      "returning the value of std1 attribute:",
#       getattr(std1, 'id'), "\n"
#                            "setting the id attribute of std1 to 8001:", setattr(std1, 'id', 8001), "\n"
#                                                                                                    "deleting the id of std1:",
#       delattr(std1, 'id'), "\n", "\n"
#       )

# built in attributes
# print("Student.__doc__ : ", Student.__doc__)
# print("Student.__name__: ", Student.__name__)
# print("Student.__dict__): ", Student.__dict__)
# print("Student.__module__: ", Student.__module__)
# print("Student.__bases__: ", Student.__bases__)
