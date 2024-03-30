import psycopg2


def create_table():
    conn = psycopg2.connect(dbname='studentdb', user='postgres', password='Coopercooper12', host='localhost', port='5432')
    cur = conn.cursor()
    cur.execute("create table students(student_id serial primary key, name text, address text, age int, number text);")
    conn.commit()
    conn.close()


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

# insert_data()
update_data()