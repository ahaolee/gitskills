def calculate(number):
    result = 0
    i = 1
    while i <= number:
        result = i + result
        i = i + 1
    return result
result = calsulate(200)
print('1~200 value is:',result)
