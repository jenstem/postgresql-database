import psycopg2


# Create Table
def create_table():
    conn = psycopg2.connect(dbname='studentdb', user='postgres', password='Coopercooper12', host='localhost', port='5432')
    cur = conn.cursor()
    cur.execute("create table students(student_id serial primary key, name text, address text, age int, number text);")
    conn.commit()
    conn.close()


# Add Data
def insert_data():
    name = input("Enter name: ")
    address = input("Enter address: ")
    age = input("Enter age: ")
    number = input("Enter phone number: ")
    conn = psycopg2.connect(dbname='studentdb', user='postgres', password='Coopercooper12', host='localhost', port='5432')
    cur = conn.cursor()
    cur.execute("insert into students(name, address, age, number) values (%s, %s, %s, %s)", (name, address, age, number))
    print("Data added successfully")
    conn.commit()
    conn.close()


# Delete Data
def delete_data():
    student_id = input("Enter student id to be deleted: ")
    conn = psycopg2.connect(dbname='studentdb', user='postgres', password='Coopercooper12', host='localhost', port='5432')
    cur = conn.cursor()
    cur.execute("select * from students where student_id=%s", (student_id,))
    student = cur.fetchone()
    if student:
        print(f"Student to be delete: ID: {student[0]}, Name: {student[1]}, Address: {student[2]}, Age: {student[3]}, Number: {student[4]}")
        choice = input("Are you sure you want to delete this student? (y/n): ")
        if choice.lower() == "y":
            cur.execute("delete from students where student_id=%s", (student_id,))
            print("Student deleted successfully")
        else:
            print("Student not deleted")
    else:
        print("Student not found")
    conn.commit()
    conn.close()


# Revise Data
def update_data():
    student_id = input("Enter student id to be updated: ")
    conn = psycopg2.connect(dbname='studentdb', user='postgres', password='Coopercooper12', host='localhost', port='5432')
    cur = conn.cursor()
    fields = {
        "1": ("name", "Enter new name: "),
        "2": ("address", "Enter new address: "),
        "3": ("age", "Enter new age: "),
        "4": ("number", "Enter new phone number: "),
    }
    print("Select field to update: ")
    for key in fields:
        print(f"{key}:{fields[key][0]}")
    field_choice = input("Enter field number to be updated: ")

    if field_choice in fields:
        field_name, prompt = fields[field_choice]
        new_value = input(prompt)
        sql = f"update students set {field_name}=%s where student_id=%s"
        cur.execute(sql, (new_value, student_id))
        print(f"{field_name} updated successfully")
    else:
        print("Invalid choice, please try again")

    conn.commit()
    conn.close()


# Read Data
def read_data():
    conn = psycopg2.connect(dbname='studentdb', user='postgres', password='Coopercooper12', host='localhost', port='5432')
    cur = conn.cursor()
    cur.execute("select * from students;")
    students = cur.fetchall()
    for student in students:
        print(f"ID: {student[0]}, Name: {student[1]}, Address: {student[2]}, Age: {student[3]}, Number: {student[4]}")
    conn.close()


# Menu Options
while True:
    print("\n Welcome to the student database management system")
    print("1. Create table")
    print("2. Insert Data")
    print("3. Read Data")
    print("4. Update Data")
    print("5. Delete Data")
    print("6. Exit")
    choice = input("Enter your choice: (1 - 6): ")
    if choice == '1':
        create_table()
    elif choice == '2':
        insert_data()
    elif choice == '3':
        read_data()
    elif choice == '4':
        update_data()
    elif choice == '5':
        delete_data()
    elif choice == '6':
        break
    else:
        print("Invalid choice, please try again")
