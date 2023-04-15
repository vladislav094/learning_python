# 1

# class Block:
#     # Good Luck!
#     def __init__(self, arr):
#         self.arr = list(arr)
#
#     def get_width(self):
#         return self.arr[0]
#
#     def get_length(self):
#         return self.arr[1]
#
#     def get_height(self):
#         return self.arr[2]
#
#     def get_volume(self):
#         return self.arr[0] * self.arr[1] * self.arr[2]
#
#     def get_surface_area(self):
#         return 2 * (self.arr[1] * self.arr[0] + self.arr[1] * self.arr[2] + self.arr[0] * self.arr[2])
#
#
# b = Block([2, 4, 6])
# print(b)
#
# print(b.get_width())
# print(b.get_length())
# print(b.get_height())
# print(b.get_volume())
# print(b.get_surface_area())

# 2

# class Class:
#     value = 1
#     @staticmethod
#     def get_number():
#         result = Class.value
#         Class.value *= 2
#         return result
#
#
# print(Class.get_number())
# print(Class.get_number())
# print(Class.get_number())
# print(Class.get_number())

# 3
# class Quark:
#     def __init__(self, color, up):
#         self.color = color
#         self.up = up
#         self.baryon = 1
#
#     @property
#     def baryon_number(self):
#         return self.baryon / 3
#
#     def interact(self, second_self):
#         self.color, second_self.color = second_self.color, self.color
#
#
# q1 = Quark('red', 'up')
# print(q1.color)
# print(q1.baryon_number)
# q2 = Quark('blue', 'strange')
# print(q2.color)
# print(q2.baryon_number)
# q1.interact(q2)
# print(q1.color)
# print(q2.color)

# 4
# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def greet(self, your_name):
#         return f"Hello {your_name}, my name is {self.name}"
#
# jack = Person("Jack")
# jill = Person("Jill")
#
# print(jack.greet('Jill'))

# 5
# def make_class(*args):
#     class MyClass:
#         def __init__(self, *vals):
#             self.__dict__ = {x:y for x,y in zip(args, vals)}
#     return MyClass
#
# Animel = make_class("name", "species", "age", "health", "weight", "color")


# 6
class Student:

    def __init__(self, first_name, last_name, grades=[]):
        self.first_name = first_name
        self.last_name = last_name
        self.grades = grades[:]

    def add_grade(self, grade):
        self.grades.append(grade)

    def get_average(self):
        return sum(self.grades) / len(self.grades)

matthewConnorGrades = [44, 53, 27, 60]
chloeMadisonGrades = [79, 58, 30, 66]
studentGrades = matthewConnorGrades, chloeMadisonGrades
matthewConnor = Student('Matthew', 'Connor', matthewConnorGrades)
chloeMadison = Student('Chloe', 'Madison', chloeMadisonGrades)
students = matthewConnor, chloeMadison
print(matthewConnor.grades)
print(chloeMadison.grades)


johnDoe = Student('John', 'Doe')
janeDoe = Student('Jane', 'Doe')
jamesSmith = Student('James', 'Smith')
jennaSmith = Student('Jenna', 'Smith')
students = johnDoe, janeDoe, jamesSmith, jennaSmith
firstAssessmentGrades = [63, 92, 82, 75]
#
for i, student in enumerate(students):
    student.add_grade(firstAssessmentGrades[i])

print(johnDoe.grades)
print(janeDoe.grades)
print(jamesSmith.grades)
print(jennaSmith.grades)
