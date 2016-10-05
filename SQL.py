import pymysql
import fun
import sys
import io
if __name__ == '__main__':
	sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
	import Cut
class Sql(object):
	def __init__(self,host,usernamep,password,db):
		try:
			self.db = pymysql.connect(host,usernamep,password,db,charset='utf8')
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
	def getStringResult(self,sql=""):
		string = self.exec(sql)
		lst = []
		for j in string:
			tmp = []
			for i in j:
				tmp.append(str(i))
			lst.append(" ".join(tmp))
		return lst
if __name__ == '__main__':
	s = Sql("127.0.0.1","root","","oj")
	print(s.getStringResult("select * from oj_contest"))
	for i in s.getStringResult("select * from oj_contest"):
		print(Cut.go(i))