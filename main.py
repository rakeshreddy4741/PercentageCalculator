from tabulate import tabulate      # tabulate package is used for Display data in a table format.
# this program is for calculating percentage of btech
def input_int_validate(value):
    # this function is to take input from user and validate
    sem_value = 'wrong'
    valid_input = False
    while sem_value.isdigit() == False or valid_input == False:  # validating with while loop checking the input format
        sem_value = input(f"enter {value}")

        if sem_value.isdigit() == False:
            print("Sorry that is not a digit!")

        if sem_value.isdigit() == True:
            if int(sem_value) in range(1, 30):
                valid_input = True
            else:
                valid_input = False
                print("enter in range")

    return int(sem_value)  # returns semesters value





def input_str_validate():
    # this function is to take input from user and validate
    input_value = "322"
    valid_input = False
    accept_range = ['A', 'A+', 'O', 'B', 'B+', 'C', 'F']
    while input_value.isdigit() == True or valid_input == False:  # validating with while loop checking the input format
        input_value = input("enter the grade:")
        if input_value.isdigit():
            print("sorry You entered a wrong input")
        if input_value in accept_range:
            valid_input = True
        else:
            valid_input = False
    return input_value


def sgpa_display_table(records, total_credit_points, total_credits):
    # this function is to display the subject name,credit points and grade points.

    print("{:>30}".format("Table of semester"))
    print(tabulate(records, headers=["subject", "Grade", "Credit", "Credit points"]))  # printing data in form of table
    print("{:28}{:>17}".format(total_credits, total_credit_points))   # printing the total credits and credits points
    sgpa=total_credit_points/total_credits                            # sgpa formula
    print("SGPA is:{:.2f}".format(sgpa))
    per=(sgpa-0.5)*10                                                 # percentage of sgpa
    print("Percentage of current semester:{:.2f}".format(per))


def grade_cal(score, credit):
    grades = {"O": 10, "A+": 9, "A": 8, "B+": 7, "B": 6, "c": 5, "F": 0}  # matching the grade to grade points
    points = []

    for i in grades:
        if i == score:

            points = grades[i]*credit                                       # calculating the credit points

    return points                                                         # returns credit points to represent() function



def semester_calculator():
    # this function takes the input of semesters and pass data to display_table function
    records = []
    total_credit_points = 0
    total_credits = 0
    # for i in range(1, subject count + 1):
    subjects_count = input_int_validate("subjects:")
    for j in range(1, subjects_count + 1):
        subject = input("enter the subject name {}:".format(j))
        score = input_str_validate()
        credit = input_int_validate("credits:")
        total_credits = total_credits+credit
        credit_points = grade_cal(score, credit)
        total_credit_points = total_credit_points + credit_points
        records.append([subject, score, credit, credit_points])      # appending the data to records list

    sgpa_display_table(records, total_credit_points, total_credits)

def calculator_selction():
    valid_input = False
    select = "wrong"
    while select.isdigit() == False or valid_input == False:
        select = input("select from following:\n1.semester(SGPA) percentage calculater\n2.CGPA calculator\n:")

        if not select.isdigit():
            print("wrong option")

        if select.isdigit():
            if int(select) == 1:
                semester_calculator()
                valid_input = True

            elif int(select) == 2:
                cgpa_calculator()
                valid_input = True
            else:
                print("wrong option")
                valid_input = False
def cgpa_display_table(records, total_sem_credits, total_credit_points):
    print("{:>30}".format("Table of semesters "))
    print(tabulate(records, headers=["SGPA", "credits", "credit_points"]))  # printing data in form of table
    print("{:>17}{:>17}".format(total_sem_credits, total_credit_points))   # printing the total credits and credits points
    cgpa = total_credit_points / total_sem_credits
    per = (cgpa - 0.5)*10                       # percentage of cgpa
    print("CGPA of all semesters is:{:.2f}".format(cgpa))
    print("Percentage of current semester:{:.2f}".format(per))

def cgpa_calculator():  #  this function calculates the CGPA
    total_sems=input_int_validate("total semesters:")
    total_sem_credits=0
    total_credit_points=0
    records = []
    for i in range(1, total_sems+1):
        sgpa=float(input("SGPA value {}:".format(i)))

        credits=input_int_validate("Total credites of semester:")
        total_sem_credits=total_sem_credits+credits
        credit_points = sgpa * credits
        total_credit_points=total_credit_points+credit_points
        records.append([sgpa,credits,credit_points])

    cgpa_display_table(records,total_sem_credits,total_credit_points)


wel="welcome to Percentage Calculator"
print("{:>60}".format(wel))
calculator_selction()








