import mapper
import json
import re 

map_in_fname = "case8.json"
names_fname = "names_case8.json"
map_out_fname = "case8_out.json"

dict_ = mapper.GetDict(map_in_fname)

print("dict file name: ",map_in_fname)
mapper.PrintDict(dict_)


# arr_name_dict_ = {}

# print("Below is the find() test:")
for keys,values in dict_.items():
	# print(keys," : ",values)
	if keys == values :
		dict_[keys] = True
	elif values.find(keys) == 0 and len(keys) != len(values):
		dict_[keys] = [0, values[len(keys):len(values)]]
	# elif :
		# print("the same : ")
		# if re.search("\[+[0-9]+\]$",values) :
			# print("match!!")
			# for m in re.finditer("\[+[0-9]+\]$", values):
				# number_ = values[m.start(0)+1:m.end(0)-1]
				# value_name_ = values[:m.start(0)]
				# if value_name_ in arr_name_dict_ :
					# arr_name_dict_[value_name_][1].add(number_)
				# else :
					# number_set_ = set()
					# number_set_.add(number_)
					# arr_name_dict_[value_name_] = [0, number_set_]
			# dict_[keys] = [0, number_]
		# else :
			# print("no match!!")
# mapper.PrintDict(dict_)
# print("arr_name_dict_ :")
# mapper.PrintDict(arr_name_dict_)

file_out = open("%s%s" % ("./testcase/map_in_compress/",map_in_fname),'w')
json.dump(dict_,file_out,sort_keys=True,indent=1,separators=(',', ':'))

names_ = mapper.GetNames(names_fname)
print("names set file name: ",names_fname)
mapper.PrintNames(names_)

mapped_ = {}	
mapper.MapName(dict_, names_, map_out_fname, mapped_)
mapper.PrintDict(mapped_)

file_out = open("%s%s" % ("./testcase/map_out/",map_out_fname),'w')
json.dump(mapped_,file_out,sort_keys=True,indent=1,separators=(',', ':'))
