nums = [0, 1, 2, 4, 5, 7]

result = []
nums_len = len(nums)
i = 0
while i < nums_len:
    first = nums[i]
    last = nums[i]
    while True:
        if last+1 in nums:
            last += 1
        else:
            break
    if first == last:
        result.append(str(first))
    else:
        result.append(str(first)+"->"+str(last))
    i = i+last-first+1
    print(i)
print(result)
