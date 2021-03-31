a = int(input())
cnt=0
for x in range(0,a):
	j = input()
	for i in range(0,len(j)):
		if(j[i]=='0'):
			cnt+=1
print(cnt)