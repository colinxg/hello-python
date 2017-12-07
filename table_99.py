# Multiplication table
print('# version 1')

for i in range(1, 10):
	for j in range(1, i+1):
		print(str(j)+'*'+str(i)+'='+str(i*j),end='  ')
	print()

print()
print('# version 2')

for i in range(1, 10):
	for j in range(1, i+1):
		product = i*j
		if j > 1 and product < 10:
			product = str(product) + ' '
		print(str(j)+'*'+str(i)+'='+str(product), end=' ' )
	print()

