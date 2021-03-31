n = int(input())
arr = list()
cnt=0
for x in range(0,n):
	i = input()
	arr.append(i)
for x in range(1,n-1):
	if( int(arr[x])>int(arr[x-1]) and int(arr[x])>int(arr[x+1]) ):
		cnt+=1
print(cnt)