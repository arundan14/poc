import csv
import sqlite3

conn = sqlite3.connect('mvp.db')
cur = conn.cursor()
cur.execute("""DROP TABLE IF EXISTS mvp_users""")
cur.execute("""CREATE TABLE mvp_users
            (User_ID text, User_Name text, User_Hash text)""")

cur.execute("""DROP TABLE IF EXISTS mvp_vault""")
cur.execute("""CREATE TABLE mvp_vault
            (Item_ID text, Item_Name text,Item_Catg text, User_ID text, price integer)""")
cur.execute("""DROP TABLE IF EXISTS mvp_handshake""")
cur.execute("""CREATE TABLE mvp_handshake
            (Item_ID text, Item_Name text,Item_Catg text, User_ID text, price integer)""")
cur.execute("""DROP TABLE IF EXISTS mvp_trans""")
cur.execute("""CREATE TABLE mvp_trans
            (Trans_ID text, Block_hash text, User_ID text, Description text, Date text)""")

with open('/var/www/html/example/mvpdata/mvp_users.csv', 'r') as f:
    reader = csv.reader(f.readlines()[1:])  # exclude header line
    cur.executemany("""INSERT INTO mvp_users VALUES (?,?,?)""",
                    (row for row in reader))
f.close()
#    for row in reader:
#     print len(row)
with open('/var/www/html/example/mvpdata/mvp_vault.csv', 'r') as f:
    reader = csv.reader(f.readlines()[1:])  # exclude header line
    cur.executemany("""INSERT INTO mvp_vault VALUES (?,?,?,?,?)""",
                    (row for row in reader))
#    for row in reader:
#     print len(row)
with open('/var/www/html/example/mvpdata/mvp_handshake.csv', 'r') as f:
    reader = csv.reader(f.readlines()[1:])  # exclude header line
    cur.executemany("""INSERT INTO mvp_handshake VALUES (?,?,?,?,?)""",
                    (row for row in reader))
with open('/var/www/html/example/mvpdata/mvp_trans.csv', 'r') as f:
    reader = csv.reader(f.readlines()[1:])  # exclude header line
    cur.executemany("""INSERT INTO mvp_trans VALUES (?,?,?,?,?)""",
                    (row for row in reader))
 
conn.commit()
conn.close()
