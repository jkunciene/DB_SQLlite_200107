import sqlite3


def open_connection():
    connection = sqlite3.connect("exercise.db")
    cursor = connection.cursor()
    return connection, cursor


def close_connection(connection, cursor):
    cursor.close()
    connection.close()


def query_database(query, params=None):
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


def get_employes_filter4_1():
    query = """SELECT depart_name, COUNT(employee_id)  
    FROM employees 
    INNER JOIN departments on employees.department_id=departments.department_id
    GROUP BY depart_name"""
    query_database(query)


get_employes_filter4_1()

def get_employes_filter4_2():
    query = """SELECT departments.Department_ID, departments.depart_name, employees.manager_id, employees.first_name
    FROM departments
    INNER JOIN employees
    ON employees.employee_id=departments.Manager_ID"""
    query_database(query)

get_employes_filter4_2()

def get_employes_filter4_3():
    query = """SELECT departments.depart_name, employees.first_name, locations.city
    FROM employees
    INNER JOIN departments
    ON employees.employee_id=departments.Manager_ID
    INNER JOIN locations
    ON departments.Location_ID=locations.location_id"""
    query_database(query)

get_employes_filter4_3()

def get_employes_filter4_4():
    query = """SELECT job_history.*
    FROM job_history
    INNER JOIN employees
    ON employees.employee_id=job_history.employee_id
    WHERE employees.salary > 10000"""
    query_database(query)

get_employes_filter4_4()