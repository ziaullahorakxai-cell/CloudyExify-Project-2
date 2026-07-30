import csv
import os


FILE_NAME = "students.csv"

students = []


# ============================
# LOAD DATA FROM CSV
# ============================

def load_data():

    try:

        if os.path.exists(FILE_NAME):

            with open(FILE_NAME, "r") as file:

                reader = csv.DictReader(file)

                for row in reader:

                    row["marks"] = list(
                        map(int, row["marks"].split(","))
                    )

                    row["average"] = float(row["average"])

                    students.append(row)


            print("Data loaded successfully")

        else:

            print("CSV file not found. Creating new file...")


    except Exception as e:

        print("Error loading data:", e)



# ============================
# SAVE DATA TO CSV
# ============================


def save_data():

    try:

        with open(
            FILE_NAME,
            "w",
            newline=""
        ) as file:


            columns = [
                "id",
                "name",
                "age",
                "department",
                "marks",
                "average",
                "grade"
            ]


            writer = csv.DictWriter(
                file,
                fieldnames=columns
            )


            writer.writeheader()


            for s in students:

                writer.writerow({

                    "id":s["id"],

                    "name":s["name"],

                    "age":s["age"],

                    "department":s["department"],

                    "marks":",".join(
                        map(str,s["marks"])
                    ),

                    "average":s["average"],

                    "grade":s["grade"]

                })


        print("Data saved successfully")


    except Exception as e:

        print(
            "Saving Error:",
            e
        )




# ============================
# CALCULATE AVERAGE
# ============================


def calculate_average(marks):

    return round(
        sum(marks)/len(marks),
        2
    )




# ============================
# ASSIGN GRADE
# ============================


def assign_grade(avg):


    if avg >= 90:
        return "A+"


    elif avg >= 80:
        return "A"


    elif avg >= 70:
        return "B"


    elif avg >= 60:
        return "C"


    elif avg >= 50:
        return "D"

    else:

        return "F"




# ============================
# ADD STUDENT
# ============================


def add_student():

    try:

        sid=input(
            "Student ID: "
        )


        for s in students:

            if s["id"] == sid:

                print(
                    "Student ID already exists"
                )

                return



        name=input(
            "Name: "
        )


        age=input(
            "Age: "
        )


        department=input(
            "Department: "
        )


        marks=[]


        for subject in [
            "Math",
            "English",
            "Computer"
        ]:

            mark=int(
                input(
                    subject+" Marks: "
                )
            )


            marks.append(mark)



        avg=calculate_average(marks)

        grade=assign_grade(avg)



        student={

            "id":sid,

            "name":name,

            "age":age,

            "department":department,

            "marks":marks,

            "average":avg,

            "grade":grade

        }


        students.append(student)


        save_data()


        print(
            "Student Added Successfully"
        )


    except ValueError:

        print(
            "Marks must be numbers"
        )





# ============================
# VIEW STUDENTS
# ============================


def view_students():

    if len(students)==0:

        print(
            "No records found"
        )

        return



    for s in students:

        print("\n----------------")

        print(
            "ID:",
            s["id"]
        )

        print(
            "Name:",
            s["name"]
        )

        print(
            "Department:",
            s["department"]
        )

        print(
            "Marks:",
            s["marks"]
        )

        print(
            "Average:",
            s["average"]
        )

        print(
            "Grade:",
            s["grade"]
        )





# ============================
# SEARCH STUDENT
# ============================


def search_student():

    sid=input(
        "Enter ID: "
    )


    for s in students:

        if s["id"]==sid:

            print(s)

            return


    print(
        "Student not found"
    )





# ============================
# EDIT GRADES
# ============================


def edit_grades():

    sid=input(
        "Enter ID: "
    )


    for s in students:


        if s["id"]==sid:


            marks=[]


            try:

                for sub in [
                    "Math",
                    "English",
                    "Computer"
                ]:

                    marks.append(
                        int(
                            input(
                                sub+": "
                            )
                        )
                    )


                s["marks"]=marks


                s["average"]=calculate_average(
                    marks
                )


                s["grade"]=assign_grade(
                    s["average"]
                )


                save_data()


                print(
                    "Updated Successfully"
                )


                return


            except:

                print(
                    "Invalid marks"
                )


                return



    print(
        "Student not found"
    )





# ============================
# RANK STUDENTS
# ============================


def rank_students():

    ranked=sorted(
        students,
        key=lambda x:x["average"],
        reverse=True
    )


    position=1


    for s in ranked:


        print(
            position,
            s["name"],
            s["average"],
            s["grade"]
        )


        position+=1





# ============================
# DELETE STUDENT
# ============================


def delete_student():

    sid=input(
        "Enter ID: "
    )


    for s in students:


        if s["id"]==sid:


            students.remove(s)


            save_data()


            print(
                "Deleted Successfully"
            )


            return



    print(
        "Student not found"
    )





# ============================
# MENU
# ============================


def menu():

    while True:


        print("""
=============================
Student Management System
=============================

1. Add Student
2. View Students
3. Calculate Average
4. Assign Grades
5. Rank Students
6. Search Student
7. Edit Grades
8. Delete Student
9. Exit

""")


        choice=input(
            "Choose option: "
        )


        if choice=="1":

            add_student()


        elif choice=="2":

            view_students()


        elif choice=="3":

            view_students()


        elif choice=="4":

            view_students()


        elif choice=="5":

            rank_students()


        elif choice=="6":

            search_student()


        elif choice=="7":

            edit_grades()


        elif choice=="8":

            delete_student()


        elif choice=="9":

            save_data()

            print(
                "Program Closed"
            )

            break


        else:

            print(
                "Invalid option"
            )





# START PROGRAM

load_data()

menu()