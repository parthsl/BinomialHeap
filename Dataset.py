import random
import sys


def dijkstra(N):
    matrix = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(0, N):
        for j in range(i + 1, N):
            matrix[i][j] = random.randint(0, N * random.randint(0, N))
            matrix[j][i] = matrix[i][j]
    return matrix


def display_matrix(matrix):
    N = len(matrix)
    for i in range(0, N):
        print(matrix[i])
