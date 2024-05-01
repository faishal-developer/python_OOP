strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

strs_len = len(strs)
dict = {}

result = []

for i in range(strs_len):
    temp = ''.join(sorted(strs[i]))
    if temp in dict:
        dict[temp].append(strs[i])
    else:
        dict[temp] = [strs[i]]

for keys in dict:
    result.append(dict[keys])

print(result)
