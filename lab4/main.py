import random
import numpy

matrix = numpy.array([  [0.15, 0, 0, 0.2],
                        [0.05, 0, 0.1, 0],
                        [0, 0.1, 0, 0.05],
                        [0.2, 0, 0, 0.15]])


X = sum(matrix[:, i] for i in range(4))
test = [0.35, 0.5, 0.65, 1]

Y = numpy.copy(matrix)
for row in range(4):
    sum = 0
    for col in range(4):
        sum += matrix[row][col]
    for col in range(4):
        Y[row][col] = Y[row][col] / sum

for row in range(4):
    for col in range(3, -1, -1):
        if Y[row][col] > 0:
            sum = 0
            for i in range(col):
                sum+= Y[row][i]
            Y[row][col] += sum

result = [[0 for _ in range(4)] for _ in range(4)]
for _ in range(100000):
    rand = numpy.random.random()
    for row in range(4):
        if rand < test[row]:
            rand = numpy.random.random()
            for col in range(4):
                if rand < Y[row][col]:
                    result[row][col] += 1
                    break
            break

for line in result:
    print(line)
