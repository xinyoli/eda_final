import json

def GetDict():
	with open('testcase/map_in.json', 'r') as file_in:
		dict = json.load(file_in)
	return dict

def PrintDict(dict):
	print(type(dict))
	for keys,values in dict.items():
		print(keys," : ",values)
	print()
		
def GetNames():
	with open('testcase/names.json', 'r') as file_in:
		nameset = json.load(file_in)
	return nameset[0]
	
def PrintNames(names):
	print(type(names))
	for name in names:
		print(name)
	print()
		
