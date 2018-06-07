import json

def GetDict(map_in_fname = "map_in.json"):
	# with open("testcase/map_in/map_in.json", 'r') as file_in:
	with open("%s%s" % ("testcase/map_in/",map_in_fname), 'r') as file_in:
		dict = json.load(file_in)
	return dict

def PrintDict(dict):
	print(type(dict))
	for keys,values in dict.items():
		print(keys," : ",values)
	print()
		
def GetNames(names_fname = "names.json"):
	with open("%s%s" % ("testcase/names/",names_fname), 'r') as file_in:
		nameset = json.load(file_in)
	return nameset[0]
	
def PrintNames(names):
	print(type(names))
	for name in names:
		print(name)
	print()
		
def MapName(dict_,names_,map_out_fname = "map_out.json",mapped_ = {}):
	print("initialize file: ",map_out_fname)	
	PrintDict(mapped_)

	for name_ in names_:
		if name_ in dict_:
			mapped_[name_] = dict_[name_]

	print("map_out file name: ",map_out_fname)	