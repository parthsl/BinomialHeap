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

def write_to_file(filename,matrix):
    N = len(matrix)
    file = open(filename,'w')
    for i in range(0, N):
        for j in range(0, N):
            file.write(str(matrix[i][j]))
            file.write(' ')
        file.write('\n')
    file.close()

def read_from_file(filename):
    read = open(filename,'r')
    data = read.readline().split(' ')
    matrix = [[0 for _ in range(len(data)-1)] for _ in range(len(data)-1)]
    row = -1
    while len(data)-1 > 0:
        row +=1
        for i in range(len(data)-1):
            matrix[row][i] = int(data[i])
        data = read.readline().split(' ')
    return matrix

def get_matrix(filename,N):
    tmatrix = read_from_file(filename)
    matrix = [[0 for _ in range(N)] for _ in range(N)]
    if N>len(tmatrix):
        return tmatrix
    for i in range(N):
        for j in range(N):
            matrix[i][j] = tmatrix[i][j]
    return matrix

if __name__== "__main__":
    write_to_file('random.txt',dijkstra(1000))
    matrix = read_from_file('random.txt')
    display_matrix(matrix)

