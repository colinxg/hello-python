# version 1

print([1])
ln = [1,1]
print(ln)

for _ in range(10):
	lx = [1]
	for i in range(len(ln)-1):
		lx.append(ln[i]+ln[i+1])
	lx.append(1)
	print(lx)
	ln=lx.copy()
