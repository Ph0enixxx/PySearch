import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
import time
import jieba
from Data import Data
class Doc(object):
	def save(self,doc=""):
		#分词
		#每个都提交数据库
		pass
	def get(self,key="",page=1,size=0):
		#分词
		#获取每个数据
		pass