# Задача 4.1.
# Домашнее задание на SQL

# В базе данных teacher создайте таблицу Students

# Структура таблицы: Student_Id - Integer, Student_Name - Text, School_Id - Integer (Primary key)

# Наполните таблицу следующими данными:

# 201, Иван, 1
# 202, Петр, 2
# 203, Анастасия, 3
# 204, Игорь, 4

# Напишите программу, с помощью которой по ID студента можно получать информацию о школе и студенте.

# Формат вывода:

# ID Студента:
# Имя студента:
# ID школы:
# Название школы:



import sqlite3
connection = sqlite3.connect('teachers.db')
cursor = connection.cursor()
sqlquery = """CREATE TABLE Students (
Students_Id INTEGER NOT NULL,
Student_Name TEXT NOT NULL,
School_Id INTEGER NOT NULL PRIMARY KEY
);"""
cursor.execute(sqlquery)
connection.commit()
connection.close()

import sqlite3
connection = sqlite3.connect('teachers.db')
cursor = connection.cursor()
sqlquery = """INSERT INTO Students (Students_Id, Student_Name, School_Id )
VALUES
('201', 'Иван', '1'),
('202', 'Петр', '2'),
('203', 'Анастасия', '3'),
('204', 'Игорь', '4');"""

cursor.execute(sqlquery)
connection.commit()
connection.close()

def get_connection():
  connection = sqlite3.connect('teachers.db')
  return connection

def close_connection(connection):
  if connection:
    connection.close()

def get_school_id(Students_Id):
  try:
    connection = get_connection()
    cursor = connection.cursor()
    select_query = "SELECT * FROM Students WHERE Students_Id = ?"
    cursor.execute(select_query,(Students_Id,))
    rec = cursor.fetchone()
    close_connection(connection)
    return rec[2]
  except (Exception, sqlite3.Error) as error:
    print ("Ошибка в получении данных: ", error)

def get_school_name(school_id):
  try:
    connection = get_connection()
    cursor = connection.cursor()
    select_query = "SELECT * FROM School WHERE School_Id = ?"
    cursor.execute(select_query,(school_id,))
    record = cursor.fetchone()
    close_connection(connection)
    return record[1]
  except (Exception, sqlite3.Error) as error:
    print ("Ошибка в получении данных: ", error)

def get_students_detail(Students_Id):
  try:
    school_id = get_school_id(Students_Id)
    school_name = get_school_name(school_id)
    connection = get_connection()
    cursor = connection.cursor()
    select_query = "SELECT * FROM Students WHERE Students_Id = ?"
    cursor.execute(select_query,(Students_Id,))
    records = cursor.fetchall()
    for row in records:
      print ("ID Студента:", row[0])
      print ("Имя студента:", row[1])
      print ("ID школы:", row[2])
      print("Название школы:", school_name)

  except (Exception, sqlite3.Error) as error:
    print ("Ошибка в получении данных: ", error)

x = int(input("Введите ID Студента: "))
get_students_detail(x)
