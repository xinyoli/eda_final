import mapper
import json
from random import shuffle

map_in_fname = "case8.json"
names_fname = "names_case8.json"


dict_ = mapper.GetDict(map_in_fname)
print("dict file name: ",map_in_fname)
mapper.PrintDict(dict_)

dict_keys = list(dict_.keys())
shuffle(dict_keys)
names_ = [dict_keys,list(dict_.values())]
print(names_)
file_out = open("%s%s" % ("./testcase/names/",names_fname),'w')
json.dump(names_,file_out,sort_keys=True,indent=4,separators=(',', ' : '))