# this works
N = int(input())

height = 0
width = 0
list = []

for i in range(N):
	x, y = map(int, input().split())
	height = x
	width = y
	area = height * width
	list.append(area)

# sort from smallest to largest
list.sort()

# print the largest one (the one at the end)
print(list[-1])
