N = int(input())

while N != 0:
    pontosA = 0
    pontosB = 0

    for i in range(N):
        A, B = map(int, input().split())

        if A > B:
            pontosA += 1
        elif A < B:
            pontosB += 1

    print(pontosA, pontosB)

    N = int(input())