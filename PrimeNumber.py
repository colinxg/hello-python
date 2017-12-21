# get prime number
import datetime

# version 1
upper_limit = 10000
delta = [0, 0, 0]
counts = [0, 0, 0]

start = datetime.datetime.now()
for _ in range(10):
	counts[0] = 0
	l1 = []
	for x in range(2, upper_limit):
		for i in range(2,int(x ** 0.5)+1):
			if x % i == 0:
				break
		else:
			#print(x)
			counts[0] +=1
			l1.append(x)		
delta[0] = (datetime.datetime.now() - start).total_seconds()

# version 2
start = datetime.datetime.now()
for _ in range(10):
	counts[1] = 1
	l2 = [2]
	for x in range(3, upper_limit, 2):
		for i in range(3, int(x ** 0.5)+1, 2):
			if x % i == 0:
				break
		else:
			#print(x)
			counts[1] += 1
			l2.append(x)
delta[1] = (datetime.datetime.now() - start).total_seconds()

# version 3
start = datetime.datetime.now()
for _ in range(10):
	counts[2] = 1
	l3 = [2]
	for x in range(3,upper_limit,2):
		for i in l3:
			if x % i == 0:
				break
		else:
			l3.append(x)
			counts[2] += 1 
delta[2] = (datetime.datetime.now() - start).total_seconds()

print(delta, sep = '\t')
print(counts, sep = '\t')
