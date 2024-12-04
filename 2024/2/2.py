def safe_check(code_list: list[int]) -> int:
    prev = -1
    asc = False
    desc = False
    for i in code_list:
        if prev == -1:
            prev = i
        elif prev - i > 0:
            desc = True
        elif prev - i < 0:
            asc = True
        else:
            return 0

        if asc and desc:
            return 0
        if abs(prev - i) > 3:
            return 0

        prev = i
    return 1


def safe_check_dampener(code_list: list[int]) -> int:

    if safe_check(code_list) == 1:
        return 1
    else:
        for i in range(len(code_list)):
            new_list = code_list[:i] + code_list[i + 1 :]
            if safe_check(new_list) == 1:
                return 1

        return 0


if __name__ == "__main__":
    code_list = []
    safe_n = 0
    with open("./2/data.txt", "r") as file:
        for line in file:
            input = line.strip()
            code_list = [int(x) for x in input.split()]
            safe_n += safe_check_dampener(code_list)

    print(safe_n)
