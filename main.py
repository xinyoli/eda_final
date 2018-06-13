import mapper
import json

map_in_fname = "map_in.json"
names_fname = "names.json"
map_out_fname = "map_out.json"

# dict_ = mapper.GetDict(map_in_fname)
dict_ = { 
	"a[dog]" : "a0",  
	"b[dog]" : "b0", 
	"a[cat]" : "a1", 
	"b[cat]" : "b1",  
	"a[0][0]" : "a_0_", 
	"a[0][1]" : "a_1_", 
	"a[1][0]" : "a_2_", 
	"a[1][1]" : "a_3_" 
}
print("dict file name: ",map_in_fname)
mapper.PrintDict(dict_)

names_ = mapper.GetNames(names_fname)
print("names set file name: ",names_fname)
mapper.PrintNames(names_)

mapped_ = {}	
mapper.MapName(dict_, names_, map_out_fname, mapped_)
mapper.PrintDict(mapped_)

file_out = open("%s%s" % ("./testcase/map_out/",map_out_fname),'w')
json.dump(mapped_,file_out,sort_keys=True,indent=4,separators=(',', ' : '))
