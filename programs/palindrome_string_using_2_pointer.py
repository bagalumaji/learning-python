def is_palindrome(s):
    start = 0
    end = len(s) - 1
    flag = True

    while start <= end:
        if s[start] != s[end]:
            flag = False
            break

        start += 1
        end -= 1

    return flag


print(is_palindrome("aba"))
