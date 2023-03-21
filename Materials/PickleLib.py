import pickle

class Student:
    def __init__(self, name, age, class_name):
        self.name = name
        self.age = age
        self.class_name = class_name

def write():
    # Create an empty list to store the student objects
    students = []

    # Take input for 10 students
    for i in range(1):
        name = input("Enter name of student: ")
        age = int(input("Enter age of student: "))
        class_name = input("Enter class name of student: ")

        # Create a new student object with the input data
        student = Student(name, age, class_name)

        # Add the student object to the list
        students.append(student)

    # Save the student objects to a binary file using pickle
    with open("students.bin", "wb") as file:
        pickle.dump(students, file)

def read():
    with open("students.bin", 'rb') as file:
        students = pickle.load(file)

    for student in students:
        print(f"Name: {student.name} | Age: {student.age} | Class: {student.class_name}")

if __name__ == '__main__':
    write()
    read()
