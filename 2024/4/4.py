import re


def count_xmas(line: list[str]) -> int:
    regex1 = r"XMAS"
    regex2 = r"SAMX"
    tot = 0
    for row in line:
        tot += len(re.findall(regex1, row))
        tot += len(re.findall(regex2, row))

    return tot


if __name__ == "__main__":
    chars = []
    tot = 0
    with open("./4/data.txt", "r") as file:
        for line in file:
            chars.append(line.strip())

    rows = len(chars)
    cols = len(chars[0])
    vertical_lines = [
        "".join(chars[row][col] for row in range(rows)) for col in range(cols)
    ]

    top_left_to_bot_right = []
    bot_left_to_top_right = []

    for d in range(rows + cols - 1):
        top_left_to_bot_right.append(
            "".join(
                chars[i][d - i]
                for i in range(max(d - cols + 1, 0), min(d + 1, rows))
                if 0 <= d - i < cols
            )
        )

    for d in range(rows + cols - 1):
        bot_left_to_top_right.append(
            "".join(
                chars[rows - 1 - i][d - i]
                for i in range(max(d - cols + 1, 0), min(d + 1, rows))
                if 0 <= d - i < cols
            )
        )

    tot += count_xmas(chars)
    tot += count_xmas(vertical_lines)
    tot += count_xmas(top_left_to_bot_right)
    tot += count_xmas(bot_left_to_top_right)
    print(tot)
