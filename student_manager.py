students = []
def add_student(name):
 students.append(name)
def display_students():
 for s in students:
 print(s)
add_student("John")
add_student("Emma")
add_student("Ethan")
display_students()
