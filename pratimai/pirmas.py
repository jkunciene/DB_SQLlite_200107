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
        # klaidu gaudymas, vykdyk, jei nera klaidos, jei yra parodyk kokia
        if params:
            cursor.execute(query, params)
            connection.commit()
        else:
            for row in cursor.execute(query):
                print(row)

    except sqlite3.DataError as error:
        print(error)
    finally:
        connection.close()


def exercise1():
    query = "SELECT * FROM employees"
    query_database(query)


# exercise1()


def exercise2():
    query = """SELECT first_name, last_name, salary FROM employees
                    WHERE salary < 10000 OR salary > 15000"""
    query_database(query)


# exercise2()


def exercise3():
    query = """SELECT first_name, last_name, department_id FROM employees
                    WHERE department_id=30 OR department_id=100 
                    ORDER BY department_id ASC"""
    query_database(query)


# exercise3()

def exercise4():
    query = """SELECT first_name, last_name, salary FROM employees
                    WHERE (salary < 10000 OR salary > 15000) AND ( department_id=30 OR department_id=100)"""
    query_database(query)


# exercise4()

def exercise5():
    query = """SELECT first_name FROM employees
                    WHERE (first_name LIKE '%b%') AND (first_name LIKE '%c%')"""
    query_database(query)


# exercise5()

def exercise6():
    query = """SELECT last_name, job_id, salary FROM employees
                    WHERE (( job_id='IT_PROG') OR ( job_id='SH_CLERK')) AND ((salary <> 4500) OR (salary <>10000) OR (salary <> 15000)) """
    query_database(query)


# exercise6()

def exercise7():
    query = """SELECT last_name, first_name FROM employees
                    WHERE LENGTH(first_name) = 6"""
    query_database(query)


# exercise7()

def exercise8():
    query = """SELECT last_name FROM employees
                    WHERE last_name LIKE '__e%'"""
    query_database(query)


exercise8()