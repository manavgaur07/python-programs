import json
FILE = "students.json"
def load_students():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return []
def save_students(students):
    with open(FILE, "w") as f:
        json.dump(students, f, indent=4)

def select_course():
        print(" 1.Bca\n 2.Mca\n 3.BscIT\n 4.Mba\n")
        choose= int(input("Choose your course:"))
        match choose:
            case 1 : return "Bca"
            case 2 : return "Mca"
            case 3 : return "BscIT"
            case 4 : return "Mba"
            case _: 
              print("Invalid")
              return None
def register():
    students= load_students()
    print("\n=== Registration Form===")
    while True:
     name = input("Enter Your Name:").strip()
     if name != "":
      break
     print("try again")
    while True:
     mobile = input("Enter mobile number: ")
     if len(mobile) == 10 and mobile.isdigit():
        break
     print("Invalid Mobile! Enter 10 digits")

    while True:
     email = input("Enter your email id:")
     if "@" in email or "." in email:
        break
     print("Invalid email!")
    course = select_course()
    if course is None:
       print("try again")

    new_student = {
        "name":name,
        "mobile":mobile,
        "email":email,
        "course": course
    }
    students.append(new_student)
    save_students(students)
    print("registration succesfull!")
    print("\n--- Student Details ---")
    print("name     :", new_student["name"])
    print("mobile     :", new_student["mobile"])
    print("email     :", new_student["email"])
    print("course     :", new_student["course"])
def update(): 
   students = load_students()

   mobile = (input("Enter Your Mobile Number:"))
   for student in students:
      if student["mobile"] == mobile:
         print("--- Student Found! ---")
         print("name :", student["name"])
         print("email :", student["email"])
         print("course :", student["course"])
         print("What do you want to change:")
         print("\n1. Name \n2.Email \n3.Course")
         choice= int(input(""))
         match choice:
            case 1: 
               while True:
                  new_name = input("Enter new name:").strip()
                  if new_name != "":
                     student["name"] = new_name
                     break
                  print("Error!")
            case 2: 
               while True:
                  new_email = input("Enter new email")
                  if "@" in new_email and "." in new_email:
                     student["email"] = new_email
                     break
                  print("Error!")
            case 3: 
                  student["course"] = select_course()   
            case _:
               print("invalid")
      save_students(students)
      print("Successfully updated")
      return 

def delete(): 
   students = load_students()

   mobile = input("Enter MobileNumber you want to delete:")

   for student in students:
      if student["mobile"] == mobile:
         print("student found!")
         print("name:", student["name"])
         print("email:", student["email"])
         print("course:", student["course"])
         a = input("do you want to really delete it? y or n:")
         if a.lower() == "y":
           students.remove(student)
           save_students(students)
           print("Removed Sucessfully")
      else:
         print("return cancelled!")
         return
   print("student not found!")

while True:
   print("\n1. Student registration \n2. Update Details \n3. Delete Student \n4.Exit")
   choice = int(input("Choose:"))
   match choice:
        case 1: 
           register()
        case 2:
           update()
        case 3:
           delete()
        case _:
           break





