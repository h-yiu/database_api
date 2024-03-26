import psycopg2

conn = psycopg2.connect(host="localhost", dbname = "ricedb0621", user = "riceuser", password = "ricepw")

cur = conn.cursor()

DB_func_name = "SquaresInRange"

DB_args = (3,8)                     # a tuple

cur.callproc(DB_func_name, DB_args)
rows = cur.fetchall()

# Do something with the returned data.
# Here, print the column names, then the data.
head = ""
cols = list(c for c in cur.description)
for c in cols:
    si = str(c).find("name=") + 6
    ei = str(c).find("',")
    head += str(c)[si:ei] + " "

print(head)

for r in rows:
    print(r[0], " ", r[1])

conn.commit()
cur.close()
conn.close()