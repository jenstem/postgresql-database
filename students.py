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
    name = input("Enter name: ")
    address = input("Enter address: ")
    age = input("Enter age: ")
    number = input("Enter phone number: ")
    conn = psycopg2.connect(dbname='studentdb', user='postgres', password='Coopercooper12', host='localhost', port='5432')
    cur = conn.cursor()
    cur.execute("update students set name=%s , address=%s , age=%s , number=%s where student_id=%s", (name, address, age, number, student_id))
    conn.commit()
    conn.close()

# insert_data()
update_data()