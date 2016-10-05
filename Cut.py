import jieba
if __name__ == '__main__':
	import sys
	import io
	sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

go = lambda x:list(jieba.cut_for_search(x))

if __name__ == '__main__':
	seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造")  # 搜索引擎模式
	print(list(seg_list))
	print(go("安徽省闺女请问想组"))