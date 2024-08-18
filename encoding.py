def ctt(character):
	two=ord(character)
	return two
	
sentence=input("输入句子")
with open("./output.txt","w")as f:
	f.write("")

for i in sentence:
	output=ctt(i)
	with open("./output.txt","a") as f:
		f.write(str(output))
		f.write("\n")
	
	
	