n = int(input())
arr = list()
cnt=0
temp = 0
for x in range(0,n):
	i = input()
	arr.append(i)
print(arr)
for x in range(0,int(n/2)):
	temp = arr[x]
	arr[x] = arr[len(arr)-1-x]
	arr[len(arr)-1-x] = temp
print(arr)