import json 
# from pprint import pprint

with open('testcase/map_in.json', 'r') as file_in:
    dict = json.load(file_in)
	
# print(dict)
print(type(dict))

for keys,values in dict.items():
    print(keys," : ",values)


with open('testcase/names.json', 'r') as file_in:
    nameset = json.load(file_in)
	
# print(nameset)
# print(type(nameset))
# for set in nameset: 
	# for name in set:
		# print(name, sep=' ')
	# print('');

names = nameset[0]
print(type(names))
for name in names:
	print(name)

# file_out = open('./testcase/test_out.json','w')
# json.dump(dict,file_out,sort_keys=True,indent=4,separators=(',', ': '))



# mapped_ = dict.fromkeys(names_)
# mapper.PrintDict(mapped_)

# print("none"," = ",dict['none'])
for name_ in names_:
	if name_ in dict_:
		print(name_, dict_[name_])
		# mapped_ = dict.fromkeys(name_,dict_[name_])
	
# mapper.PrintDict(mapped_)

for name_ in names_:
	if name_ in dict_:
		# print(name_, dict_[name_])
		mapped_[name_] = dict_[name_]