import pymysql

conf = {
    'host':'192.168.143.7',
    'user':'root',
    'password':'123456',
    'database':'slw',
    'port':3306
}
#创建数据库连接

cnn = pymysql.connect(**conf)

#游标cursor
cursor = cnn.cursor()

#sql语句
query_sql = 'select * from user_info'

#执行sql
cursor.execute(query_sql)

#获取结果，打印
# res = cursor.fetchone()   #获取1条数据
# res = cursor.fetchmany(2)  #获取n条数据
res = cursor.fetchall()  #获取所有数据

print(res)

#关闭游标，数据库连接
cursor.close()
cnn.close()
