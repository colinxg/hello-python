# count average
# version 1

n = 0
sums = 0

while True:
	i = input('>>>')
	if i == 'quit' or i == 'Q':
		break
	n += 1
	sums += int(i)
	avg = sums/n
	print(avg)	
