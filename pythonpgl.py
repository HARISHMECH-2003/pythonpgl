
import psycopg2
import psycopg2.extras

hostname='localhost'
database='postgres'
username='postgres'
pwd='postgres'
port_id=5432
conn=None
cur=None
try:
    conn = psycopg2.connect(
        dbname=database,
        user=username,
        password=pwd,
        host=hostname,
        port=port_id)
    cur= conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute('DROP TABLE IF EXISTS personaldetails')
    create_script= '''CREATE TABLE IF NOT EXISTS personaldetails(
           id INT NOT NULL PRIMARY KEY,
           name VARCHAR(50) NOT NULL,
           gender VARCHAR(50) NOT NULL,
           salary INT ,
           DEPARTMENT VARCHAR(50) NOT NULL
    )'''
    cur.execute(create_script)

    insert_script = 'INSERT INTO personaldetails(id,name,gender,salary,DEPARTMENT) VALUES(%s, %s, %s, %s, %s)'
    insert_values=[(1,'Harish','Male',12000,'mech'),(2,'James','Male',20000,'mech'),(3,'Kendall','Female',15000,'CSE')]
    for record in insert_values:
        cur.execute(insert_script,record) 
    update_script='UPDATE personaldetails SET salary=salary+2000'
    cur.execute(update_script)  
    delete_script='DELETE  FROM personaldetails WHERE name=%s'
    delete_record=('James',)
    cur.execute(delete_script,delete_record)
    cur.execute('SELECT * FROM personaldetails')
    for record in cur.fetchall():
        print(record['name'],record['salary'])
    conn.commit()



   
except Exception as error:
    print(error)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()