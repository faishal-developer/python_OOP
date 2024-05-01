n = 2
result = False
while True:
    number_str = str(n)
    next_number = 0
    for i in number_str:
        next_number = next_number+int(i)*int(i)
        if next_number < 10:
            if next_number == 1 or next_number == 7:
                result = True
            else:
                result = False
            break
        n = next_number


print(result)
