if __name__ == "__main__":
    list1 = []
    list2 = []
    with open("./1/data.txt", "r") as file:
        for line in file:
            input1 = line.strip()
            num1, num2 = input1.split()
            list1.append(int(num1))
            list2.append(int(num2))

    list1.sort()
    list2.sort()
    diff = [abs(i - j) for i, j in zip(list1, list2)]
    total_sum = sum(diff)
    print(total_sum)

    similarity = 0
    num = 0
    for i in list1:
        for j in list2:
            if i == j:
                num += 1
        similarity += i * num
        num = 0

    print(similarity)
