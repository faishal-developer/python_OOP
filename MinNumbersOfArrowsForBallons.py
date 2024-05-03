points = [[3, 9], [7, 12], [3, 8], [6, 8], [
    9, 10], [2, 9], [0, 9], [3, 9], [0, 6], [2, 8]]
points = sorted(points, key=lambda x: x[1])
result = 0
print(points)
p_len = len(points)

i = 0
while i < p_len:
    c = points[i]
    result += 1
    j = i+1
    while j < p_len:
        if c[1] >= points[j][0]:
            i = i+1
            j = j+1
        else:
            break
    i = i+1
print(result)
