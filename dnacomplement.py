file = open('/home/jtan/Downloads/rosalind_revc.txt','r')
fileLines = file.readlines() 
result = ""

for lines in reversed(fileLines):
	for char in reversed(lines):
		if char == 'A':
			result += 'T'
		elif char == 'T':
			result += 'A'
		elif char == 'C':
			result += 'G'
		elif char == 'G':
			result += 'C'
print result	
