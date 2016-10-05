import pymysql
import fun
import sys
import io
if __name__ == '__main__':
	sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

class Sql(object):
	def __init__(self,host,usernamep,password,db):
		try:
			self.db = pymysql.connect(host,usernamep,password,db)
		except:
			fun.msg("db connect error",1)
			sys.exit(1)
	def exec(self,sql=""):
		if sql != "":
			cursor = self.db.cursor()
			try:
			   cursor.execute(sql)
			   self.db.commit()
			except:
			   self.db.rollback()
			   fun.msg("exec" + str(sql) + "error",1)
			   return None
		return cursor.fetchall()

if __name__ == '__main__':
	s = Sql("127.0.0.1","root","","oj")
	print(s.exec("select * from oj_contest"))