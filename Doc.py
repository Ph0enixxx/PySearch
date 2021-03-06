import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
import time
import json
####################
import Cut
from Data import Data
from SQL import Sql
import fun
import conf
####################

#不同的词后面加上不同的题号即可

class Doc(object):
	__slots__ = ('data')
	def __init__(self):
		self.data = Data()
	def save(self,doc=""):
		data_ = doc
		#每个非空词 先获取 再提交
		print(data_)
		for i in data_:
			num  = i[0]
			data = i[1]
			#fun.msg(num,2)
			#fun.msg(data,2)

			for x in data:
				if x != "" and x != " ":
					#获取json 转换 添加 写回
					##try catch
					#print(type(x))
					#fun.msg(x,1)
					#print(x)
					js = self.data.get(x)
					fun.msg(js,2)
					if js == None:
						l = [num,]
						numx = self.data.json_encode(l)
						self.data.set(x,numx)
					else:
						try:
							js = list(self.data.json_decode(str(js)))
							js.append(num)
							if len(js) >1:
								js = list(set(js))
							numx = self.data.json_encode(js)
							self.data.set(x,numx)
						except:
							fun.msg(str(js) + "出了点毛病",1)
		#分词
			#判断空
		#每个都提交数据库
		##避免重复添加
		pass
	def get(self,key="",page=1,size=0):
		#分词
		#获取每个数据

		##分词找并集

		if key == "":
			return None ##None好还是""好
		lst = []
		words = Cut.go(key)
		#print(words)
		for i in words:
			#print(type(self.data.json_decode(self.data.get(i))))
			try:
				lst.extend(self.data.json_decode(self.data.get(i)))
			except:
				pass
		lst = list(set(lst))
		if size == 0:
			try:
				return self.data.json_encode(lst)
			except:
				return self.data.json_encode([])
		##分页功能未测试！
		else:
			return self.data.json_encode(lst[(page-1)*size:page*size])
		pass
	def getData(self):
		s = Sql(conf.SQL_HOST,conf.SQL_USER,conf.SQL_PASS,conf.SQL_DB)
		try:
			p = [(i[0],Cut.go(i[1]))for i in s.getStringResult(conf.QUERY_DATA)]
		#print(p)
			return p
		except:
			fun.msg("获取数据失败",1)
if __name__ == '__main__':
	a = Doc()
	a.save(a.getData())
	# print(a.get("了"))
	# print(a.getData())