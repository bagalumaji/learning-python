def print_numbers_from_string(s):
    result = ""
    for ch in s:
        if ch.isdigit():
            result += ch
        else:
            print(result)
            result =""


if __name__ == "__main__":
    s1 = "abc1cd23f89jhu213y"
    print_numbers_from_string(s1)
