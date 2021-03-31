n = int(input())
arr = list()
cnt=0
for x in range(0,n):
	i = input()
	arr.append(i)
for x in range(0,n):
	if(int(arr[x])>0):
		cnt+=1
print(cnt)