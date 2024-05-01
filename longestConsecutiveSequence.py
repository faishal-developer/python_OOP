nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
dict_nums = {}
max_terms = 0
for i in nums:
    dict_nums[i] = True

for key in dict_nums:
    temp = 1
    if dict_nums[key] == False:
        continue
    current = key
    while True:
        print("kkkkkkk")
        current = current+1
        if current in dict_nums:
            temp = temp+1
            dict_nums[current] = False
        else:
            break
    current = key
    while True:
        print('llllllllll')
        current = current-1
        if current in dict_nums:
            temp = temp+1
            dict_nums[current] = False
        else:
            break
    if temp > max_terms:
        max_terms = temp

print(max_terms)
