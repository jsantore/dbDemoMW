import random
import  sqlite3
from typing import Tuple
def open_db(filename:str)->Tuple[sqlite3.Connection, sqlite3.Cursor]:
    db_connection = sqlite3.connect(filename)#connect to existing DB or create new one
    cursor = db_connection.cursor()#get ready to read/write data
    return db_connection, cursor

def make_initial_classLists(cursor:sqlite3.Cursor):
    cursor.execute(f'''INSERT INTO CLASS_LIST (banner_id, course_prefix, course_number,  registration_date)
    VALUES(1001, 'Comp', 490, DATE('now'))
    ''')
    cursor.execute(f'''INSERT INTO CLASS_LIST (banner_id, course_prefix, course_number,  registration_date)
        VALUES(1002, 'Comp', 490, DATE('now'))
        ''')
    cursor.execute(f'''INSERT INTO CLASS_LIST (banner_id, course_prefix, course_number,  registration_date)
            VALUES(1003, 'Comp', 490, DATE('now'))
            ''')
    cursor.execute(f'''INSERT INTO CLASS_LIST (banner_id, course_prefix, course_number,  registration_date)
            VALUES(1004, 'Comp', 490, DATE('now'))
            ''')
    cursor.execute(f'''INSERT INTO CLASS_LIST (banner_id,  course_prefix, course_number, registration_date)
            VALUES(1005, 'Comp', 490, DATE('now'))
            ''')

def close_db(connection:sqlite3.Connection):
    connection.commit()#make sure any changes get saved
    connection.close()

def setup_db(cursor:sqlite3.Cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS students(
    banner_id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    gpa REAL DEFAULT 0,
    credits INTEGER DEFAULT 0
    );''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS courses(
    course_prefix TEXT NOT NULL,
    course_number INTEGER NOT NULL,
    cap INTEGER DEFAULT 20,
    description TEXT,
    PRIMARY KEY(course_prefix, course_number)
    );''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS class_list(
    registration_id INTEGER PRIMARY KEY,
    course_prefix TEXT NOT NULL,
    course_number INTEGER NOT NULL,
    banner_id INTEGER NOT NULL,
    registration_date TEXT,
    FOREIGN KEY (banner_id) REFERENCES students (banner_id)
    ON DELETE CASCADE ON UPDATE NO ACTION,
    FOREIGN KEY (course_prefix, course_number) REFERENCES courses (course_prefix, course_number)
    ON DELETE CASCADE ON UPDATE NO ACTION
    );''')

def make_intial_students(cursor:sqlite3.Cursor):
    cursor.execute(f'''INSERT INTO STUDENTS (banner_id, first_name, last_name, gpa, credits)
                   VALUES (1001, "John", "Santore", {random.uniform(0.0,4.0)}, {random.randint(0,120)})''')
    cursor.execute(f'''INSERT INTO STUDENTS(banner_id, first_name, last_name, gpa, credits) 
            VALUES(1002, "Enping", "Li", {random.uniform(0.0, 4.0)}, {random.randint(0, 120)})''')
    cursor.execute(f'''INSERT INTO STUDENTS(banner_id, first_name, last_name, gpa, credits) 
            VALUES(1003, "Margaret", "Black", {random.uniform(0.0, 4.0)}, {random.randint(0, 120)})''')
    cursor.execute(f'''INSERT INTO STUDENTS(banner_id, first_name, last_name, gpa, credits) 
            VALUES(1004, "Seikyung", "Jung", {random.uniform(0.0, 4.0)}, {random.randint(0, 120)})''')
    cursor.execute(f'''INSERT INTO STUDENTS(banner_id, first_name, last_name, gpa, credits) 
            VALUES(1005, "Haleh", "Khojasteh", {random.uniform(0.0, 4.0)}, {random.randint(0, 120)})''')


def make_initial_courses(cursor:sqlite3.Cursor):
    cursor.execute(f'''INSERT INTO COURSES (course_prefix, course_number, cap, description)
        VALUES ('COMP', 151, 24, 'This is the intro course, you will learn to program, maybe for the first time')''')
    cursor.execute(f'''INSERT INTO COURSES (course_prefix, course_number, cap, description)
        VALUES ('COMP', 490, 20, 'This is the final course. You will get a chance to apply much of what you learned throughout the undergrad degree')''')
    cursor.execute(f'''INSERT INTO COURSES (course_prefix, course_number, cap, description)
        VALUES ('MATH', 130, 20, 'This course is changing to include much more on graph theory and number bases/systems')''')


def show_simple_select(cursor:sqlite3.Cursor):
    cutoff = float(input("What should the GPA cutoff be?"))
    #question to class-what about security issues here? 	       #Discuss
    result = cursor.execute(f'SELECT * from STUDENTS WHERE 		gpa < {cutoff}')
    for row in result:
        print(f'BannerId: {row[0]}\nName: {row[1]} {row[2]}\nGPA:{row[3]}')

def main():
    conn, cursor = open_db("demo_db.sqlite")
    setup_db(cursor)
    #make_intial_students(cursor)
    #make_initial_courses(cursor)
    #make_initial_classLists(cursor)
    show_simple_select(cursor)
    close_db(conn)



if __name__ == '__main__':
    main()