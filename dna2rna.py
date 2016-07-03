file = open('/home/jtan/Downloads/rosalind_rna.txt', 'r')
rna = ""

for line in file:
	for char in line:
		if char == 'T':
			rna += 'U'
		else:
			rna += char
print rna
