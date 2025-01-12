def reverse_only_vowels(s1: str):
    result = list(s1)
    vowels = ['a', 'e', 'i', 'o', 'u']
    lp = 0
    rp = len(s1) - 1
    while lp < rp:
        if result[lp] in vowels and result[rp] in vowels:
            result[lp], result[rp] = result[rp], result[lp]
            lp += 1
            rp -= 1
        elif  result[lp] not in vowels:
            lp += 1
        elif  result[rp] not in vowels:
            rp -= 1

    print(''.join(result))


if __name__ == "__main__":
    s = "sayaji"
    print(s)
    reverse_only_vowels(s)
