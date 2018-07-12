import csv
import sqlite3

conn = sqlite3.connect('poc_userfiles.db')
cur = conn.cursor()
cur.execute("""DROP TABLE IF EXISTS user_files""")
cur.execute("""CREATE TABLE user_files
            (ac_no integer, trans_date text, description text, user text, filename text)""")

with open('/var/www/html/example/static/user_files.csv', 'r') as f:
    reader = csv.reader(f.readlines()[1:])  # exclude header line
    cur.executemany("""INSERT INTO indiv_transactions VALUES (?,?,?,?,?)""",
                    (row for row in reader))
#    for row in reader:
#     print len(row) 
conn.commit()
conn.close()
