import mapper
import json

map_in_fname = "map_in.json"
names_fname = "names_0607.json"


dict_ = mapper.GetDict(map_in_fname)
print("dict file name: ",map_in_fname)
mapper.PrintDict(dict_)

# print(type(dict_.items()))
# print(dict_.items())

# print(type(dict_.keys()))
# print(dict_.keys())
# dict_keys_ = dict_.keys()
# print(type(dict_keys_))
# print(dict_keys_)

# print(type(dict_.values()))
# print(dict_.values())
# dict_values_ = dict_.values()
# print(type(dict_values_))
# print(dict_values_)


names_ = [list(dict_.keys()),list(dict_.values())]
print(names_)
file_out = open("%s%s" % ("./testcase/names/",names_fname),'w')
json.dump(names_,file_out,sort_keys=True,indent=4,separators=(',', ' : '))