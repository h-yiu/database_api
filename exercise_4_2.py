import psycopg2

conn = psycopg2.connect(host="localhost", dbname = "ricedb0621", user = "riceuser", password = "ricepw")

cur = conn.cursor()

DB_func_name = "max3"

fi_num = input("Enter the first number: ")
se_num = input("Enter the second number: ")
th_num = input("Enter the third number: ")

DB_args = (fi_num, se_num, th_num)

cur.callproc(DB_func_name, DB_args)
res = cur.fetchone()

if res is not None:
    print(res[0])
