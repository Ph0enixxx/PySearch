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
			fun.msg(num,2)
			fun.msg(data,2)

			for x in data:
				if x != "" and x != " ":
					#获取json 转换 添加 写回
					##try catch
					print(type(x))
					#fun.msg(x,1)
					print(x)
					js = self.data.get(x)
					fun.msg(js,2)
					if js == None:
						l = [num,]
						fun.msg(l,2)
						numx = self.data.json_encode(l)
						fun.msg(numx)
						self.data.set(x,numx)
					else:
						js = list(self.data.json_decode(js))
						js.append(num)
						if len(js) >1:
							js = list(set(js))
						numx = self.data.json_encode(js)
						self.data.set(x,numx)
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
			lst.extend(self.data.json_decode(self.data.get(i)))
			lst = list(set(lst))
		if size == 0:
			return self.data.json_encode(lst)
		else:
			return self.data.json_encode(lst[(page-1)*size:page*size])
		pass
	def getData(self):
		s = Sql("127.0.0.1","root","","oj")
		try:
			p = [(i[0],Cut.go(i[1]))for i in s.getStringResult("select * from problem")]
		#print(p)
			return p
		except:
			fun.msg("获取数据失败",1)
if __name__ == '__main__':
	a = Doc()
	#a.save(a.getData())
	print(a.get("了"))
