```
#database initialization,users and attendance tables created using MySQL workbench
import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='****',
    port='3306',
    database='college'
)
command_handler=mydb.cursor(buffered=True)


def student_session(username):
    while 1:
        print("")
        print("1. View Register")
        print("2. Logout")


        user_option = input(str("Option :"))

        if user_option=='1':
            username = (str(username),)
            command_handler.execute("SELECT date,username,status FROM attendance WHERE username =%s",username)
            records = command_handler.fetchall()
            for record in records:
                print(record)

        elif user_option =='2':
            break
        else:
            print("Invalid option selected.")

def teacher_session():
    while 1:
        print("")
        print("Teacher's menu:")
        print("1.Mark student's register")
        print("2.View register")
        print("3.View all student's usernames")
        print("4.Logout")
        print("")
        user_option = input(str("Option:"))
        if user_option == "1":
            print("")
            print("Mark student register")
            command_handler.execute("SELECT username FROM users WHERE privilege='student'")
            records= command_handler.fetchall()
            date = input(str("Date : DD/MM/YYYY : "))
            for record in records:
                record = str(record).replace("'","")
                record = str(record).replace(",", "")
                record = str(record).replace("(", "")
                record = str(record).replace(")", "")
                #Present|Absent|Late
                status=input(str("Status for "+str(record) + " P/A/L : "))
                query_vals=(str(record),date,status)
                command_handler.execute("INSERT INTO attendance (username,date,status) VALUES (%s,%s,%s)",query_vals)
                mydb.commit()
                print(record + "Marked as " + status)
        elif user_option == "2":
            print("")
            print("Viewing all student Register")
            print("")
            command_handler.execute("SELECT username,date,status FROM attendance")
            records = command_handler.fetchall()
            print("Displaying all registers:")
            print("")
            for record in records:
                print(record)
        elif user_option == "3":
            print("")
            print("Viewing all student Usernames")
            print("")
            command_handler.execute("SELECT username FROM users WHERE privilege = 'student' ")
            records = command_handler.fetchall()
            # print("Displaying all registers:")
            # print("")
            for record in records:
                record = str(record).replace("'", "")
                record = str(record).replace(",", "")
                record = str(record).replace("(", "")
                record = str(record).replace(")", "")
                print(record)
        elif user_option == "4":
            print("Logged out of Teacher account.")
            break
        else:
            print("Invalid option selected.")


def admin_session():
    while 1:
        print("")
        print("Admin menu:")
        print("1.Register new student")
        print("2.Register new teacher")
        print("3.Delete existing student")
        print("4.Delete existing teacher")
        print("5.View All Accounts")
        print("6.Logout")
        print("")

        user_option=input(str("Option:"))
        if user_option =="1":
            print("")
            username=input(str("Student username :"))
            password = input(str("Student password :"))

            query_vals=(username,password)
            command_handler.execute("INSERT INTO users(username,password,privilege) VALUES( %s,%s,'student')",query_vals)
            mydb.commit()
            print(username+" has been registered as a student.")
        elif user_option=="2":
            print("")
            username = input(str("Teacher username :"))
            password = input(str("Teacher password :"))

            query_vals = (username, password)
            command_handler.execute("INSERT INTO users(username,password,privilege) VALUES( %s,%s,'teacher')",
                                    query_vals)
            mydb.commit()
            print(username + " has been registered as a teacher.")
        elif user_option == "3":
            print("")
            print("Delete existing student account.")
            print("")
            username=input(str("Student Username: "))
            query_vals=(username,"student")
            command_handler.execute("DELETE FROM users WHERE username=%s AND privilege=%s",query_vals)
            mydb.commit()
            if command_handler.rowcount <1:
                print("Username not found")
            else:
                print(username + " has been deleted successfully")
        elif user_option == "4":
            print("")
            print("Delete existing teacher account.")
            print("")
            username=input(str("Teacher username: "))
            query_vals=(username,"teacher")
            command_handler.execute("DELETE FROM users WHERE username=%s AND privilege=%s",query_vals)
            mydb.commit()
            if command_handler.rowcount <1:
                print("Username not found")
            else:
                print(username + " has been deleted successfully")
        elif user_option == "5":
            print("")
            print("Viewing all Accounts present.")
            print("")
            command_handler.execute("SELECT * FROM users")
            mydb.commit()
            if command_handler.rowcount < 1:
                print("No accounts registered")
            else:
                records = command_handler.fetchall()
                for record in records:
                    print(record)



        elif user_option =="6":
            print('Logged out')
            break
        else:
            print("Invalid option selected")
def auth_student():
    while 1:
        print("")
        print("Student's login")
        print("")
        username = input(str("Username:"))
        password = input(str("Password:"))
        query_vals=(username,password)
        command_handler.execute("SELECT * FROM users WHERE username=%s AND password=%s AND privilege='student'",query_vals)
        mydb.commit()
        if command_handler.rowcount <= 0:
            print("Invalid login credentials.")
        else:
            student_session(username)
            break
def auth_teacher():
    while 1:
        print("")
        print("Teacher menu:")
        print("")
        username=input(str("Username:"))
        password = input(str("Password:"))
        query_vals=(username,password)
        command_handler.execute("SELECT * FROM users WHERE username=%s AND password=%s AND privilege='teacher'",query_vals)
        mydb.commit()
        if command_handler.rowcount <=0:
            print("Login credentials invalid")
        else:
            teacher_session()
            break

def auth_admin():
    while 1:
        print("")
        print("Admin login")
        print("")
        username = input(str("Username:"))
        password = input(str("Password:"))
        if username =="admin":
            if password =="password":
                admin_session()
                break
            else:
                print("password is incorrect")
        else:
            print("username is invalid")

def main():
    while 1:
        print("")
        print ("Welcome to the college system")
        print("")
        print("1.Login as student")
        print("2.Login as teacher")
        print("3.Login as admin")
        print("4.Exit")
        print("")

        user_option = input(str("Option :"))

        if user_option=="1":
            auth_student()
        elif user_option=="2":
            auth_teacher()
        elif user_option=="3":
            auth_admin()
        elif user_option=="4":
            print("Program Ended.")
            exit()
        else:
            print("Invalid option selected.")

main()

```
