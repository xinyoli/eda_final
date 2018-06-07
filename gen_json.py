import mapper
import json

map_in_fname = "map_in.json"
names_fname = "names_0607.json"


dict_ = mapper.GetDict(map_in_fname)
print("dict file name: ",map_in_fname)
mapper.PrintDict(dict_)

# names_ = {}
# for name_ in dict_:
	# mapped_[name_] = dict_[name_]
# print("initialize file: ",names_fname)	
# mapper.PrintDict(names_)


print(type(dict_.items()))
print(dict_.items())
print(type(dict_.keys()))
print(dict_.keys())
print(type(dict_.values()))
print(dict_.values())


