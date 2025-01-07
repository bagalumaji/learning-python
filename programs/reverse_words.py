def reverse_words(s: str):
    words = s.split(" ")
    result = words[::-1]
    print(' '.join(result))


reverse_words("welcome to python programming")

