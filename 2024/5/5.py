def is_correct(input_data: str) -> int:
    sum = 0
    rules, update_str = input_data.split("\n\n")

    rule_dict = {}
    for rule in rules.split("\n"):
        before, after = rule.split("|")
        if after in rule_dict:
            rule_dict[after].append(before)
        else:
            rule_dict[after] = list(before)

    for page_l in update_str.split("\n"):
        pages = page_l.split(",")
        invalid_updates = []
        valid = True
        for page in pages:
            if page in invalid_updates:
                valid = False
                break
            invalid_updates.extend(rule_dict[page])

        if valid:
            sum += int(pages[int((len(pages) - 1) / 2)])
    return sum


def is_correct2(input_data: str) -> int:
    sum = 0
    rules, update_str = input_data.split("\n\n")

    rule_dict = {}
    for rule in rules.split("\n"):
        before, after = rule.split("|")
        if after in rule_dict:
            rule_dict[after].append(before)
        else:
            rule_dict[after] = list(before)

    for page_l in update_str.split("\n"):
        pages = page_l.split(",")
        valid, pages = rec(pages, rule_dict, False)
        if valid:
            sum += int(pages[int((len(pages) - 1) / 2)])
    return sum


def rec(pages, rule_dict, valid):
    invalid_updates = []
    for i, page in enumerate(pages):
        if page in invalid_updates:
            a = pages[i - 1]
            pages[i - 1] = pages[i]
            pages[i] = a
            valid = True
            rec(pages, rule_dict, valid)
            if valid == True:
                break
        invalid_updates.extend(rule_dict[page])
    return valid, pages


if __name__ == "__main__":
    chars = []
    updates = []
    found = False
    tot = 0
    with open("./2024/5/data.txt", "r") as file:
        input_data = file.read().strip()

    print(is_correct2(input_data))
