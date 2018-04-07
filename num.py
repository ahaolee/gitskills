def calculate(number):
    result = 0
    i = 1
    while i <= number:
        result = result + 1
    return result

result = calculate(100)
print('1~100 value is:',result)
