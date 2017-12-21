# Fibonacci Numbers less 100

a = 0
b = 1

while True:
	c = a+b
	if c > 100:
		break
	a = b
	b = c
	print(c)


# Fibonacci Numbers 100th
# version 1
a = 1
b = 1
index  = 2
print('{}, {}'.format(0,0))
print('{}, {}'.format(1,1))
print('{}, {}'.format(2,1))
while True:
	c = a+b
	a = b
	b = c
	index += 1
	print('{}, {}'.format(index,c))
	if index >= 101:
		break
