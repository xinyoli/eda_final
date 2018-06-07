import mapper
import json

dict_ = mapper.GetDict()
mapper.PrintDict(dict_)

names_ = mapper.GetNames()
mapper.PrintNames(names_)

mapped_ = {}
mapper.PrintDict(mapped_)

for name_ in names_:
	if name_ in dict_:
		mapped_[name_] = dict_[name_]
	
mapper.PrintDict(mapped_)
		
file_out = open('./testcase/names/test_out.json','w')
json.dump(mapped_,file_out,sort_keys=True,indent=4,separators=(',', ' : '))
