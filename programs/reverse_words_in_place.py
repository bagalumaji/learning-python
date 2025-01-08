def reverse(s1: str) -> str:
    return s1[::-1]


def reverse_words(s1: str) -> str:
    words = s1.split(" ")
    result: [str] = []
    for w in words:
        result.append(reverse(w))

    return ' '.join(result)


s = "welcome to python programming"
print(reverse_words(s))
