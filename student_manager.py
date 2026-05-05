name_list = []
age_list = []

def add_student(name):
 name_list.append(name)

def add_age(age):
 age_list.append(age)
 
def display_students():
 for name_dis in name_list:
  print(name_dis)

 for age_dis in age_list:
  print(age_dis)

add_student("John")
add_age(21)
add_student("Emma")
add_age(19)

display_students()
