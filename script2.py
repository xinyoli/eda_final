import sys,json 

i=json.load(open(sys.argv[1])) 
json.dump(dict(zip(sorted(i[0]),sorted(i[1]))),open(sys.argv[2],'w')) 