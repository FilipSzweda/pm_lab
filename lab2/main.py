# 2.2
# a = 69069
# c = 1
# X0 = 15
# n = 100000
# M = 2 ** 31

# 10 * Xn / M

def gen_two(n, M):
    a = 69069
    c = 1
    seed = 15

    sequence = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    X = (a * seed + c) % M  # X1
    number = int(10 * X / M)
    sequence[number] += 1

    for j in range(1, n):
        X = (a * X + c) % M
        number = int(10 * X / M)
        sequence[number] += 1
    return sequence


# 2.6
# M = 2 ** 31 (l. bitow), tzn. liczby 31 bitowe <0, 2 ** 31 - 1>
# p = 7
# q = 3
# 1011010
# n = 100000

# co iteracje nowe 7 bitow brac z 7 ostatnich bitow wygenerowanego ciogu 31 bitow

def gen_six(n, M):
    p = 7
    q = 3
    number = '1011010'
    sequence = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for i in range(7, 31):
        bit = int(number[i - p]) ^ int(number[i - q])
        number += str(bit)
    index = int(10 * int(number, 2) / M)
    sequence[index] += 1

    for j in range(1, n):
        number = number[24:]
        for i in range(7, 31):
            bit = int(number[i - p]) ^ int(number[i - q])
            number += str(bit)
        index = int(10 * int(number, 2) / M)
        sequence[index] += 1

    return sequence


def main():
    sequence = gen_two(100000, 2 ** 31)
    for element in sequence:
        print(element)

    print(str(sum(sequence)) + "\n")

    sequence2 = gen_six(100000, 2 ** 31)
    for element in sequence2:
        print(element)

    print(str(sum(sequence2)) + "\n")


if __name__ == '__main__':
    main()
