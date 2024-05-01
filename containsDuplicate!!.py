nums = [1, 2, 3, 1]
k = 3
dict_nums = {}
nums_length = len(nums)
result = False

for i in range(nums_length):
    if nums[i] in dict_nums:
        temp = i-dict_nums[nums[i]]
        if temp <= k:
            result = True
            break
        dict_nums[nums[i]] = i
    else:
        dict_nums[nums[i]] = i

print(result)
