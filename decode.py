def read_txt():
	with open("/sdcard/代码/output.txt","r") as f:
		get=f.readlines()
		lis=[]
		for i in get:
			i=i[:-1]
			print(i)
			lis.append(i)
			with open("./sentence.txt","w") as f:
				f.write("")
		return lis
		

lis=read_txt()
words=[]

for i in lis:
	output=chr(int(i))
	
	words.append(output)
	
for i in words:
	with open("./sentence.txt","a") as f:
		f.write(i)
		
with open("./sentence.txt","r") as f:
	sentence=f.read()
	print(sentence)
		
		
	