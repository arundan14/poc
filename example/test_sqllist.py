#!/usr/bin/python
 
import sqlite3
from sqlite3 import Error
 
 
def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
 
    return None

def execute_query(conn, user):
    cur = conn.cursor()
    cur.execute("SELECT user_id FROM mvp_users WHERE user_id=?", (user,))
#    cur = execute(query, args)
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    return rows
 
 
def select_all_tasks(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM mvp_trans")
 
    rows = cur.fetchall()
 
    for row in rows:
        print(row)
 
 
def select_task_by_priority(conn, priority):
    """
    Query tasks by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM mvp_trans WHERE user_id=?", (priority,))
 
    rows = cur.fetchall()
 
    for row in rows:
        print(row)

    list = [dict(trans_id=row[0], hash=row[1], user_id=row[2], desc=row[3]) for row in rows] 
    for items in list:
	print items['trans_id']

def main():
    database = "/var/www/html/example/mvp.db"
 
    # create a database connection
    conn = create_connection(database)
    with conn:
        print("1. Query task by priority:")
        select_task_by_priority(conn,"arundan14")
 
        print("2. Query all tasks")
        select_all_tasks(conn)

        print("3. Query all with new proc")
        name = execute_query(conn,"arundan14")
	if name:
		print name[0]
	else:	
		print 'nothing'

 
if __name__ == '__main__':
    main()
