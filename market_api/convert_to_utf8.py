import sqlite3
import psycopg2

# Connect SQLite
sqlite_conn = sqlite3.connect('db.sqlite3')
sqlite_cur = sqlite_conn.cursor()

# Connect PostgreSQL
pg_conn = psycopg2.connect(
    dbname='market',
    user='postgres',
    password='1234',
    host='localhost'
)
pg_cur = pg_conn.cursor()

# مثال نقل جدول واحد
sqlite_cur.execute("SELECT * FROM auth_user")
rows = sqlite_cur.fetchall()

for row in rows:
    pg_cur.execute("INSERT INTO your_table VALUES (%s, %s, %s, ...)", row)

pg_conn.commit()
pg_cur.close()
pg_conn.close()
sqlite_cur.close()
sqlite_conn.close()
