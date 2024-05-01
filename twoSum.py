nums = [2, 7, 11, 15]
target = 9
dict = {}
result = []
nums_len = len(nums)

for i in range(nums_len):
    if nums[i] in dict:
        result.append(dict[nums[i]])
        result.append(i)
        break
    else:
        newTarget = target-nums[i]
        dict[newTarget] = i
print(result)
