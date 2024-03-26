import psycopg2

conn = psycopg2.connect(database = "ricedb0621", user = "riceuser", password = "ricepw", host = "localhost")

cur = conn.cursor()

cur.execute('''SELECT * FROM peak LIMIT 10''')

row1 = cur.fetchone()
if row1 is not None:
    print(row1)
    print(len(row1))

result = cur.fetchall()
for row in result:
    print(list(row))

conn.commit()
cur.close()
conn.close()