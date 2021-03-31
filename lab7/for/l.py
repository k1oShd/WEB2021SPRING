n = input()
cnt=0
for x in range(0,len(n)):
	if(n[len(n)-1-x]=='1'):
		cnt+=(2**x)
print(cnt)