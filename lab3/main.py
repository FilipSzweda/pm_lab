import math
import random


def zad1():
    p = [0.2, 0.6, 0.75, 1]
    count = [0, 0, 0, 0]
    N = 100000

    numbers = []
    for i in range(N):
        numbers.append(random.random())

    for i in range(N):
        if numbers[i] < p[0]:
            count[0] += 1
        elif numbers[i] < p[1]:
            count[1] += 1
        elif numbers[i] < p[2]:
            count[2] += 1
        elif numbers[i] < p[3]:
            count[3] += 1

    print(count)


def zad2():
    N = 100000
    numbers = [100 * random.random() + 50 for i in range(N)]
    p = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for i in range(N):
        index = int((numbers[i] / 10) - 5)
        p[index] += 1

    print(p)


def main():
    zad1()
    zad2()


if __name__ == '__main__':
    main()
