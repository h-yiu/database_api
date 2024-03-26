import psycopg2

conn = psycopg2.connect(host = "localhost", database = "ricedb0621", user = "riceuser", password = "ricepw", port = "5432")

cur = conn.cursor()

# Option 1: build a complete sql string
num = input("Enter first number: ")
num2 = 0

sql = f"INSERT INTO data(a, b) VALUES (%s, %s)" % (num, num2)
print(sql)
cur.execute(sql)

# option 2: pass the parameter to execute()

# sql2 = "INSERT INTO data(a) VALUES (%s)"
# num2 = input("Enter second number: ")
# cur.execute(sql2, (num2,))

conn.commit()

cur.close()
conn.close()

