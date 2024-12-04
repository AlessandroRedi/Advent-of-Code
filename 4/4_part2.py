import re


def count_xmas(chars: list[str]) -> int:
    tot = 0
    for i in range(1, len(chars) - 1):
        for j in range(1, len(chars[0]) - 1):
            diagonal1 = chars[i - 1][j - 1] + chars[i][j] + chars[i + 1][j + 1]
            diagonal2 = chars[i + 1][j - 1] + chars[i][j] + chars[i - 1][j + 1]

            if ("MAS" == diagonal1 or "SAM" == diagonal1) and (
                "MAS" == diagonal2 or "SAM" == diagonal2
            ):
                tot += 1
    return tot


if __name__ == "__main__":
    chars = []
    tot = 0
    with open("./4/data.txt", "r") as file:
        for line in file:
            chars.append(line.strip())

    tot = count_xmas(chars)
    print(tot)
