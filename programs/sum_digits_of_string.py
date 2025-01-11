def sum_of_numbers(s: str):
    total = 0
    num_string = ""
    for ch in s:
        if ch.isdigit():
            num_string += ch
        else:
            if num_string != "":
                total += int(num_string)
                num_string = ""

    if num_string != "":
        total += int(num_string)

    print("sum of all numbers : ", total)


if __name__ == "__main__":
    s1 = "s10d40d3r50d"
    sum_of_numbers(s1)
