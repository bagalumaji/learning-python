def is_palindrome(s):
    if s.__eq__(reverse_string(s)):
        print(s, " is palindromic string")
    else:
        print(s, " is not palindromic string")


def reverse_string(s):
    result = ''
    cnt = len(s) - 1

    while cnt >= 0:
        result += s[cnt]
        cnt -= 1

    return result


def reverse_string_1(s):
    result = ''
    cnt = 0
    index = -1

    while cnt < len(s):
        result += s[index]
        index -= 1
        cnt += 1

    return result


is_palindrome("aba")
