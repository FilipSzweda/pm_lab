# 2.2
def gen_two(n, seed, M, a, c):
    sequence = []
    X = (a * seed + c) % M  # X1
    sequence.append(X)
    for i in range(1, n):
        X = (a * X + c) % M  # X1...Xn
        sequence.append(X)
    return sequence


def main():
    sequence = gen_two(1, 123456789, (2 ** 31) - 1, 16807, 1)  # 2 ** 31 - 2 to the power of 31
    for element in sequence:
        print(element)


if __name__ == '__main__':
    main()
