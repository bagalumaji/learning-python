def count_of_characters(s1: str):
    count = {}
    for ch in s1:
        count[ch] = count.get(ch, 0) + 1

    return count


if __name__ == "__main__":
    s = "abcabcedfs"
    print(count_of_characters(s))
