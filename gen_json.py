import mapper
import json

map_in_fname = "case4.json"
names_fname = "names_case4.json"


dict_ = mapper.GetDict(map_in_fname)
print("dict file name: ",map_in_fname)
mapper.PrintDict(dict_)


names_ = [list(dict_.keys()),list(dict_.values())]
print(names_)
file_out = open("%s%s" % ("./testcase/names/",names_fname),'w')
json.dump(names_,file_out,sort_keys=True,indent=4,separators=(',', ' : '))