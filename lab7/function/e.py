num = int(input())


def foo():
	cnt = 0
	for x in range(1,num+1):
		if(num%x==0):
			cnt+=1
	if(cnt>2):
		print("composite")
	else:
		print("prime")

foo()