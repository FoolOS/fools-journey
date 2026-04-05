"GPAinator 5000"
#This app will test your GPA
#to see if you've made the Dean's List 
#or the Honor Roll.

while True:
    #Check for last name against a break condition.
    last_name = input("Please enter your last name: ")
    if last_name == "ZZZ":
        break

    #Step right up and enter your first name, any name at all!
    first_name = input("Please enter your first name: ")

    #Enter the student's smart score and determine if they are WORTHY!
    gpa = float(input("Please enter student's GPA: "))
    if gpa >= 3.5:
        print(f"{first_name} {last_name} is on the Dean's List.")
        break
    elif gpa >= 3.25:
        print(f"{first_name} {last_name} is on the Honor Roll.")
        break
    else:
        print(f"{first_name} {last_name} is not worthy.")
    break