import re


def mul_eval(line: str) -> int:
    regex = r"mul\(\d{1,3},\d{1,3}\)"
    results = re.findall(regex, line)
    reg2 = r"\d{1,3}"
    numbers = [
        int(nums[0]) * int(nums[1]) for i in results for nums in [re.findall(reg2, i)]
    ]
    mul = sum(numbers)
    return mul


def cleaning(char: str) -> str:
    regex1 = "do\(\)"
    regex2 = "don't\(\)"
    while re.search(regex2, char) and re.search(regex1, char):
        point1 = re.search(regex2, char)
        point2 = re.search(regex1, char)
        if point2.end() < point1.start():
            char = char[: point2.start()] + char[point2.end() :]
        else:
            char = char[: point1.start()] + char[point2.end() :]
    return char


if __name__ == "__main__":
    mul_tot = 0
    with open("./2024/3/data.txt", "r") as file:
        chars = file.read()
        chars = cleaning(chars)
        mul_tot = mul_eval(chars.strip())

    print(mul_tot)
