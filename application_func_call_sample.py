"""
Example Python program calling PostgreSQL database functions
"""

# Import library to connect to PostgreSQL.
import psycopg2

# Establish PostgreSQL DB connection.
conn = psycopg2.connect("dbname='ricedb' user='riceuser' host='localhost' password='ricepassword'")

# Open a cursor to perform database operations.
cur = conn.cursor()



### Example of calling a function returning one row of data

DB_func_name = 'CubeVolume'         # a string
DB_args = (5,)                      # a tuple

# Function call and return
cur.callproc(DB_func_name, DB_args)
row = cur.fetchone()                # hardcodes expectation of one row of data

# Do something with the returned data.
# Here, just print the data.
if row is not None:
    print(row)
    
    
### Example of calling a function returning multiple rows of data

DB_func_name = 'SquaresInRange'     # a string
DB_args = (3,8)                     # a tuple

# Function call and return
cur.callproc(DB_func_name, DB_args)
rows = cur.fetchall()               # allows any number of rows of data

# Do something with the returned data.
# Here, print the column names, then the data.
print ([desc[0] for desc in cur.description])
for row in rows:
    print(row)
    
    

# Make any changes to the database persistent
# There shouldn't be any changes with these examples, but still good practice.
conn.commit()

# Close communication with the database
cur.close()
conn.close()
