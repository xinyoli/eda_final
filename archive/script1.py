import sys,json 

i=json.load(open(sys.argv[1])) 
json.dump(dict(zip(i[0],[x.replace('G','R') for x in i[0]])),open(sys.argv[2],'w')) 
