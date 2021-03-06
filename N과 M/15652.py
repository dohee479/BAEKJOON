# N과 M(4)
import sys
sys.stdin = open('input.txt', 'r')


def seq(idx, n, m):
    if idx == m:
        for i in range(m):
            print(num[i], end=' ')
        print()
        return

    for i in range(1, n+1):
        if visited[i] == 1:
            continue
        num[idx] = i
        for j in range(i):
            visited[j] = 1
        seq(idx+1, n, m)
        for j in range(1, n+1):
            visited[j] = 0


N, M = 4, 2
visited = [0] * (N+1)
num = [0] * M
seq(0, N, M)