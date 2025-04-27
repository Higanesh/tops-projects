num = [2, 5, 8, 2, 9, 1]
target = 10
op = []

lenght = len(num)
print(lenght)
i = 0
while i < lenght:
	print("pass")
	temp = num[i] + num[i+1] 
	if temp == target :
		op.append(num[i])
		op.append(num[i+1])
	else :
		i = i+1
	break	
print(op)
	