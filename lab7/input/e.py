l = 109
v = int(input())
t = int(input())
distance = v*t
if(v>0):
	print(distance%l)	
else:
	print(l-(distance%l))