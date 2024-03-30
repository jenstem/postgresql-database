import psycopg2

conn = psycopg2.connect(dbname='studentdb', user='postgres', password='Coopercooper12', host='localhost', port='5432')
cur = conn.cursor()

cur.execute("create table students(student_id serial primary key, name text, address text, age int, number text);")

conn.commit()
conn.close()