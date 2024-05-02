intervals = [[1, 3], [2, 6], [3, 5], [8, 10], [15, 18]]
intervals = sorted(intervals, key=lambda x: x[0])
length = len(intervals)
result = []

i = 1
result.append(intervals[0])
result_l = 1
while i < length:
    prev_second = result[result_l-1][1]
    if intervals[i][1] <= prev_second:
        i = i+1
        continue
    elif intervals[i][0] <= prev_second:
        result[result_l-1][1] = intervals[i][1]
    else:
        result.append(intervals[i])
        result_l += 1
    i = i+1
print(result)
