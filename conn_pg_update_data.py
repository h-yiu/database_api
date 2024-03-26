import psycopg2

conn = psycopg2.connect(host = "localhost", database = "ricedb0621", user = "riceuser", password = "ricepw", port = "5432")

cur = conn.cursor()

sql = "UPDATE data SET a = %s WHERE a = %s"

db_arg = ((14, 15),)

cur.executemany(sql, db_arg)

conn.commit()

cur.close()
conn.close()