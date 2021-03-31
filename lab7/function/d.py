votes = input().split()
def foo():
	zeroes = votes.count('0')
	ones = votes.count('1')
	if(zeroes>ones):
		return 0
	else:
		return 1 
print(foo())