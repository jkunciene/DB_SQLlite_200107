import sqlite3

def open_connection():
    connection = sqlite3.connect("exercise.db")
    cursor = connection.cursor()
    return connection, cursor


def close_connection(connection, cursor):
    cursor.close()
    connection.close()


def query_database(query, params = None):
    try:
        connection, cursor = open_connection()
        if params:
            cursor.execute(query)
            connection.commit()
        else:
            for row in cursor.execute(query):
                print(row)
    except sqlite3.DatabaseError as error:
        print(error)
    finally:
        close_connection(connection, cursor)


# task 1
def get_employees_task1():
    query = """SELECT first_name, last_name, salary, job_id  FROM employees 
    WHERE salary < 10000 or salary < 15000 """
    query_database(query)

# task 2
def get_employees_task2():
    query = """SELECT first_name, last_name, department_id  FROM employees
    WHERE department_id = 30 or department_id = 100
    ORDER BY department_id ASC """
    query_database(query)

# task 3
def get_employees_task3():
    query = """SELECT first_name, last_name, department_id, salary  FROM employees
    WHERE (department_id = 30 or department_id = 100) AND (salary <10000 or salary > 15000)   """
    query_database(query)

# task 4
def get_employees_task4():
    query = """SELECT first_name  FROM employees
    WHERE (first_name LIKE "%b%") AND (first_name LIKE "%c%")  """
    query_database(query)

# task 5
def get_employees_task5():
    query = """SELECT last_name, job_id, salary  FROM employees
    WHERE (job_id = "IT_PROG" OR job_id = "SH_CLERK" ) AND (NOT salary =  4500 or 10000 or 15000)  """
    query_database(query)

# task 6
def get_employees_task6():
    query = """SELECT last_name FROM employees
    WHERE LENGTH(last_name) = 6  """
    query_database(query)

# task 7
def get_employees_task7():
    query = """SELECT last_name FROM employees
    WHERE last_name LIKE "___e%"  """
    query_database(query)


# get_employees_task1()
# get_employees_task2()
# get_employees_task3()
# get_employees_task4()
# get_employees_task5()
# get_employees_task6()
# get_employees_task7()

# 2nd part tasks

# 2nd part task 1
def get_employees_2nd_task1():
    query = """SELECT DISTINCT job_id FROM employees
    ORDER BY job_id ASC  """
    query_database(query)

# 2nd part task 2
def get_employees_2nd_task2():
    query = """SELECT SUM(salary) AS total_salary FROM employees"""
    query_database(query)

# 2nd part task 3
def get_employees_2nd_task3():
    query = """SELECT MIN(salary) AS min_salary FROM employees"""
    query_database(query)

# 2nd part task 4
def get_employees_2nd_task4():
    query = """SELECT MAX(salary) AS max_salary FROM employees"""
    query_database(query)

# 2nd part task 5
def get_employees_2nd_task5():
    query = """SELECT AVG(salary), COUNT(employee_id), department_id FROM employees
    WHERE department_id = 90"""
    query_database(query)

# 2nd part task 6
def get_employees_2nd_task6():
    query = """SELECT MIN(salary), MAX(salary), AVG(salary), SUM(salary) FROM employees"""
    query_database(query)

# 2nd part task 7
def get_employees_2nd_task7():
    query = """SELECT job_id, count(*) as samejob FROM employees GROUP BY job_id"""
    query_database(query)

# 2nd part task 8
def get_employees_2nd_task8():
    query = """SELECT MAX(salary) - MIN(salary) as difference FROM employees"""
    query_database(query)

# 2nd part task 9
def get_employees_2nd_task9():
    query = """SELECT department_id, SUM(salary) FROM employees
    GROUP BY department_id """
    query_database(query)

# 2nd part task 10
def get_employees_2nd_task10():
    query = """SELECT job_id, AVG(salary) FROM employees
    WHERE job_id NOT IN (SELECT job_id FROM employees WHERE job_id ="IT_PROG")
    GROUP BY job_id """
    query_database(query)

# 2nd part task 11
def get_employees_2nd_task11():
    query = """SELECT manager_id, employee_id, MIN(salary) FROM employees
    GROUP BY manager_id"""
    query_database(query)


# get_employees_2nd_task1()
# get_employees_2nd_task2()
# get_employees_2nd_task3()
# get_employees_2nd_task4()
# get_employees_2nd_task5()
# get_employees_2nd_task6()
# get_employees_2nd_task7()
# get_employees_2nd_task8()
# get_employees_2nd_task9()
# get_employees_2nd_task10()
# get_employees_2nd_task11()

def create_names_view():
    query = """ CREATE VIEW IF NOT EXISTS names
                AS SELECT
                first_name,
                last_name
                FROM employees"""

    query_database(query)
    query_database("SELECT * FROM names")

# create_names_view()

# 3nd part tasks

# 3nd part task 1
def get_employees_3nd_task1():
    query = """ SELECT first_name, last_name, salary
                FROM employees
                WHERE salary > (SELECT salary FROM employees WHERE last_name = 'Bull')"""

    query_database(query)

# get_employees_3nd_task1()


# 3nd part task 2
def get_employees_3nd_task2():
    query = """ SELECT first_name, last_name, employee_id, manager_id, job_id
            FROM employees
            WHERE (employee_id IN (SELECT manager_id FROM employees))"""

    query_database(query)

# get_employees_3nd_task2()

# 3nd part task 3
def get_employees_3nd_task3():
    query = """ SELECT first_name, last_name, salary
                FROM employees                
                WHERE salary > (SELECT AVG(salary) FROM employees)"""

    query_database(query)

# get_employees_3nd_task3()

def get_employees_3nd_task4():
    query = """ SELECT first_name, last_name, salary
                FROM employees
                WHERE salary = (SELECT min_salary FROM jobs WHERE employees.job_id = jobs.job_id)"""

    query_database(query)

#get_employees_3nd_task4()

def get_employees_3nd_task5():
    query = """ SELECT first_name, last_name, salary
                FROM employees
                WHERE department_id IN (SELECT department_id FROM departments 
                WHERE depart_name LIKE 'IT%' AND 
               salary > (SELECT AVG(salary) FROM employees))"""

    query_database(query)

get_employees_3nd_task5()

def get_employees_3nd_task6():
    query = """ SELECT first_name, last_name, salary FROM employees
                WHERE salary IN (SELECT salary FROM employees ORDER BY salary desc LIMIT 3)"""

    query_database(query)

# get_employees_3nd_task6()

# 3nd part task 7
def get_employees_3nd_task7():
    query = """ SELECT first_name, last_name FROM employees
                WHERE manager_id IN (SELECT employee_id FROM employees
                WHERE department_id IN (SELECT department_id FROM departments
                WHERE location_id IN (SELECT location_id FROM locations WHERE country_id = 'US')))"""

    query_database(query)

#get_employees_3nd_task7()