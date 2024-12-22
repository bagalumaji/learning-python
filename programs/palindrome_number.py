def is_palindrome(num):
    reversed_number = reverse_number(num)
    if reversed_number == num:
        print(f"{num} is palindromic number")
    else:
        print(f"{num} is not palindromic number")


def reverse_number(num):
    result = 0

    while num != 0:
        d = num % 10
        num = num // 10
        result = result * 10 + d

    return result


is_palindrome(1221)
