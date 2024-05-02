intervals = [[3, 5], [12, 15]]
newInterval = [6, 8]
int_len = len(intervals)
# if int_len==0:
#     return [newInterval]
result = []
is_used = False
if newInterval[0] <= intervals[0][0]:
    result.append(newInterval)
    is_used = True
else:
    result.append(intervals[0])

re_len = 1
for value in intervals:
    c = result[re_len-1]

    if is_used == True:
        if value[0] >= c[0] and value[0] <= c[1]:
            result[re_len-1][1] = value[1] if value[1] > c[1] else c[1]
        elif value[1] >= c[0] and value[1] <= c[1]:
            result[re_len-1][0] = value[0] if value[0] < c[0] else c[0]
        else:
            result.append(value)
            re_len = re_len+1
    elif value != intervals[0]:
        result.append(value)
        re_len = re_len+1

    c = result[re_len-1]
    if is_used == False:
        print(result, newInterval)
        if newInterval[0] >= c[0] and newInterval[0] <= c[1]:
            result[re_len-1][1] = newInterval[1] if newInterval[1] > c[1] else c[1]
            is_used = True
        elif newInterval[1] >= c[0] and newInterval[1] <= c[1]:
            result[re_len-1][0] = newInterval[0] if newInterval[0] < c[0] else c[0]
            is_used = True
        elif newInterval[0] <= c[0] and newInterval[1] >= c[1]:
            result[re_len-1][0] = newInterval[0]
            result[re_len-1][1] = newInterval[1]
            is_used = True
        elif newInterval[0] >= c[0] and newInterval[1] <= c[1]:
            is_used = False
        elif newInterval[1] < c[0]:
            temp=result[re_len-1]
            result[re_len-1]=newInterval
            result.append(temp)
            re_len = re_len+1
            is_used = True

if is_used == False:
    result.append(newInterval)

print(result)
