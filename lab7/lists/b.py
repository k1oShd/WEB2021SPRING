n = int(input())
arr = list()
ans=""
for x in range(0,n):
	i = input()
	arr.append(i)
for x in range(0,n):
	if(int(arr[x])%2==0):
		ans+=str(arr[x])
		ans+=" "
print(ans)