name_list = []
age_list = []

def add_student(name):
 name_list.append(name)

def add_age(age):
 age_list.append(age)
 
def display_students():
 for name_dis in name_list:
  for age_dis in age_list:
   if age_dis <= 17:
    print(f"{name_dis} is still a teenager")

   else:
    age_dis >= 18
    print(f"{name_dis} is now an adult.")

add_student(input("Enter your name: "))
add_age(int(input("Enter your age: ")))

display_students()
