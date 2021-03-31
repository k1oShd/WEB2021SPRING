n = int(input())
i = 0
ans=""
while i<n:
	if(2**i<n):
		ans+=str(2**i)
		ans+=" "
	i+=1
print(ans)