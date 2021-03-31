n = int(input())
arr = list()
cnt=0
for x in range(0,n):
	i = input()
	arr.append(i)
for x in range(1,n):
	if(int(arr[x])>int(arr[x-1])):
		cnt+=1
print(cnt)