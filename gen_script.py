import json
import mapper

map_in_fname = "case4.json"
dict_ = mapper.GetDict(map_in_fname)

argument_string = \
"""
names_fname = "names_case4.json"
map_out_fname = "case4_out.json"

dict_ = \
"""

mapper_string = \
"""
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

map_in_fname = "\
"""

main_string = \
"""
print("dict file name: ",map_in_fname)
PrintDict(dict_)

names_ = GetNames(names_fname)
print("names set file name: ",names_fname)
PrintNames(names_)

mapped_ = {}	
MapName(dict_, names_, map_out_fname, mapped_)
PrintDict(mapped_)

file_out = open("%s%s" % ("./testcase/map_out/",map_out_fname),'w')
json.dump(mapped_,file_out,sort_keys=False,indent=4,separators=(',', ' : '))

"""

with open("script.py", 'w') as the_script: 
	the_script.write(mapper_string)
	the_script.write("%s%s" % ("map_in.json","\""))
	the_script.write(argument_string)
	the_script.write(str(dict_))
	the_script.write(main_string)
