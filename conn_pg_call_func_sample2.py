import psycopg2
import pgclnames as pn

conn = psycopg2.connect(host = "localhost", database = "ricedb0621", user = "riceuser", password = "ricepw")

cur = conn.cursor()

DB_func_name = "calmovavgprice"

cur.callproc(DB_func_name)

results = cur.fetchall()

# Do something with the returned data.
# Here, print the column names, then the data.

# pgclnames is a self-define function to get column names of the table
heads = pn.getnames(cur)

print(heads)

for r in results:
    print(r[0], r[1], r[2])

conn.commit()
cur.close()
conn.close()



