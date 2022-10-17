#Insert a row in table
import pymysql
conn=pymysql.connect(host="localhost",port=3306,user="root",passwd="",db="b296",autocommit=True)
cur=conn.cursor()

name=input("Enter the name : ")
branch=input("Enter the branch : ")
rollno=input("Enter the rollno : ")

sql="insert into student values('"+name+"','"+branch+"','"+rollno+"')"
print(sql)
cur.execute(sql)
n=cur.rowcount
if(n>0):
	print("Data saved")
else:
	print("Error: Cannot save data")
