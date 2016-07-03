file = open('/home/jtan/Downloads/rosalind_dna.txt', 'r')
values = {}

for line in file:
	for char in line:
		if char in values:
			values[char] += 1
		elif char not in values:
			values[char] = 1
print values['A'], values['C'], values['G'], values['T']
