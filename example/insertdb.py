import csv
import sqlite3

conn = sqlite3.connect('indiv_transactions.db')
cur = conn.cursor()
cur.execute("""DROP TABLE IF EXISTS indiv_transactions""")
cur.execute("""CREATE TABLE indiv_transactions
            (ac_no integer, trans_date text, description text, amount float)""")

with open('/var/www/html/example/static/expenses.csv', 'r') as f:
    reader = csv.reader(f.readlines()[1:])  # exclude header line
    cur.executemany("""INSERT INTO indiv_transactions VALUES (?,?,?,?)""",
                    (row for row in reader))
#    for row in reader:
#     print len(row) 
conn.commit()
conn.close()
