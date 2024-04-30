dict = {}
n = 10
m = 5
list = [1, 2, 3, 4, 5, 3, 2, 1, 5, 3]
for i in range(0, n):
    if list[i] in dict:
        dict[list[i]] = dict[list[i]] + 1
    else:
        dict[list[i]] = 1

for i in range(0, m):
    print(dict[list[i]])
print(dict)
