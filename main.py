import mapper
import json
import re 

map_in_fname = "map_in.json"
names_fname = "names.json"
map_out_fname = "map_out.json"

dict_ = mapper.GetDict(map_in_fname)

print("dict file name: ",map_in_fname)
mapper.PrintDict(dict_)


arr_name_dict_ = {}

# print("Below is the find() test:")
for keys,values in dict_.items():
	print(keys," : ",values)
	if keys == values :
		print("the same : ")
		if re.search("\[+[0-9]+\]$",values) :
			print("match!!")
			for m in re.finditer("\[+[0-9]+\]$", values):
				# print(values[m.start(0):m.end(0)])
				number_ = values[m.start(0)+1:m.end(0)-1]
				value_name_ = values[:m.start(0)]
				# print(value_name_," : ",number_ )
				if value_name_ in arr_name_dict_ :
					arr_name_dict_[value_name_][1].add(number_)
				else :
					number_set_ = set()
					number_set_.add(number_)
					arr_name_dict_[value_name_] = [0, number_set_]
			# print([(m.start(0), m.end(0)) for m in re.finditer("\[+[0-9]+\]$", values)])
			# print(re.finditer("\[+[0-9]+\]$", values))
			dict_[keys] = [0, number_]
		else :
			print("no match!!")
	elif values.find(keys) == 0 and len(keys) != len(values):
		dict_[keys] = [1, values[len(keys):len(values)]]
# mapper.PrintDict(dict_)
print("arr_name_dict_ :")
mapper.PrintDict(arr_name_dict_)

file_out = open("%s%s" % ("./testcase/map_in_compress/",map_in_fname),'w')
json.dump(dict_,file_out,sort_keys=True,indent=1,separators=(',', ':'))

names_ = mapper.GetNames(names_fname)
print("names set file name: ",names_fname)
mapper.PrintNames(names_)

mapped_ = {}	
mapper.MapName(dict_,arr_name_dict_, names_, map_out_fname, mapped_)
mapper.PrintDict(mapped_)

file_out = open("%s%s" % ("./testcase/map_out/",map_out_fname),'w')
json.dump(mapped_,file_out,sort_keys=True,indent=1,separators=(',', ':'))
