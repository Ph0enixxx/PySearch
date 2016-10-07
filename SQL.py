import pymysql
import fun
import sys
import io
import conf
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
			lst.append((str(j[0])," ".join(tmp)))
		return lst
if __name__ == '__main__':
	s = Sql(conf.SQL_HOST,conf.SQL_USER,conf.SQL_PASS,conf.SQL_DB)
	print(s.getStringResult("select * from problem"))
	for i in s.getStringResult("select * from problem"):
		p = Cut.go(i[1])
		print(p)