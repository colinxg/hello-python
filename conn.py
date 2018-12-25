import pymysql


conn = pymysql.connect(user='root', password='123456', host='10.11.16.213', port=3306, database='xiao')
cursor = conn.cursor()
try:

    insert_sql = "insert into t1 (name) values ('七小福');"
    row = cursor.execute(insert_sql)
    for i in range(10):
        sql = "insert into t1(id, name) values({},'哇哈哈{}')".format(i, i)
        row2 = cursor.execute(sql)
    conn.commit()
    sql2 = 'select * from t1;'
    cursor.execute(sql2)
    print(cursor.fetchone())
    print(cursor.fetchmany(10))
    print(cursor.fetchall())
except:
    conn.rollback()
finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()


