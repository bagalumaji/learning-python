def reverse_number(num):
    result = 0
    while num != 0:
        d = num % 10
        num = num // 10
        result = result * 10 + d

    return result


print(reverse_number(1234))
