from tabulate import tabulate      # tabulate package is used for Display data in a table format.
# this program is for calculating percentage of btech
def credit_validate():
    # this function is to take input from user and validate
    sem_value = 'wrong'
    valid_input = False
    while sem_value.isdigit() == False or valid_input == False:  # validating with while loop checking the input format
        sem_value = input("enter the credits:")

        if not sem_value.isdigit():
            print("Sorry that is not a digit!")

        if sem_value.isdigit():
            if int(sem_value) in range(1, 9):

                valid_input = True
            else:
                valid_input = False
                print("enter in range(1-8)")

    return int(sem_value)  # returns semesters value

def input_validate():
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


def display_table(records, total_credit_points, total_credits):
    # this function is to display the subject name,credit points and grade points.

    print("{:>30}".format("Table of semester"))
    print(tabulate(records, headers=["subject", "Grade", "Credit", "Credit points"]))  # printing data in form of table
    print("{:28}{:>17}".format(total_credits, total_credit_points))   # printing the total credits and credits points
    sgpa=total_credit_points/total_credits                            # sgpa formula
    print("SGPA is:{}".format(sgpa))
    per=(sgpa-0.5)*10                                                 # percentage of sgpa
    print("Percentage of current semester:{}".format(per))


def grade_cal(score, credit):
    grades = {"O": 10, "A+": 9, "A": 8, "B+": 7, "B": 6, "c": 5, "F": 0}  # matching the grade to grade points
    points = []

    for i in grades:
        if i == score:

            points = grades[i]*credit                                       # calculating the credit points

    return points                                                         # returns credit points to represent() function



def represent():
    # this function takes the input of semesters and pass data to display_table function
    records = []
    total_credit_points = 0
    total_credits = 0
    # for i in range(1, subject count + 1):
    subjects_count = int(input("enter the subjects for semester "))
    for j in range(1, subjects_count + 1):
        subject = input("enter the subject name {}:".format(j))
        score = input_validate()
        credit = credit_validate()
        total_credits = total_credits+credit
        credit_points = grade_cal(score, credit)
        total_credit_points = total_credit_points + credit_points
        records.append([subject, score, credit, credit_points])      # appending the data to records list

    display_table(records, total_credit_points, total_credits)

wel="welcome to Percentage Calculator"
print("{:>60}".format(wel))
represent()                                         # calling represent function



