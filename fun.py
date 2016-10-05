debug = True
def msg(msg,t=0):
	if debug == False:
		return
	_type = ['[OK]','[ERR]','[INFO]']
	try:
		print(_type[t] + str(msg))
	except:
		print("Info format wrong!")