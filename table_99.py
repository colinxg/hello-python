# Multiplication table
# version 1

for i in range(1, 10):
	for j in range(1, i+1):
		print(str(j)+'*'+str(i)+'='+str(i*j),end='  ')
	print()


print()
# version 2

for i in range(1, 10):
	for j in range(1, i+1):
		product = i*j
		if j > 1 and product < 10:
			product = str(product) + ' '
		print(str(j)+'*'+str(i)+'='+str(product), end=' ' )
	print()


print()
# version 3

for i in range(1, 10):
	print(' '*7*(i-1), end='' )
	for j in range(i, 10):
		product = i*j
		if product < 10:
			end = '  '
		else:
			end = ' '
		print(str(i)+'*'+str(j)+'='+str(i*j),end=end)
	print()


print()
# version 4

for i in range(1,10):
	line = ''
	for j in range(1, i+1):
		line += '{}*{}={:<3}'.format(j, i, i*j)
	print(line)

