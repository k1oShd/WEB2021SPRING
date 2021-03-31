n = int(input())
arr = list()
cnt=0
for x in range(0,n):
	i = input()
	arr.append(i)
for x in range(1,n):
	if( (int(arr[x])>0 and int(arr[x-1])>0) or (int(arr[x])<0 and int(arr[x-1])<0) ):
		cnt+=1
if(cnt==0):
	print("NO")
else:
	print("YES")