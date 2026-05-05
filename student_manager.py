students = []
def add_student(name):
 students.append(name)
def display_students():
 for s in students:
 print(s)
add_student(f"{students}) John")
add_student(f"{students}) Emma")

display_students()
