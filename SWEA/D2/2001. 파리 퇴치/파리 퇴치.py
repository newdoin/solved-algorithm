T = int(input())

for tc in range(1, T+1):
    max_kill = 0
    N, M = map(int, input().split())
    map_list = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N - M + 1):
        for j in range(N - M + 1):
            max_kill = max(max_kill, sum([sum(map_list[i+k][j:j+M]) for k in range(M)]))

    print(f"#{tc} {max_kill}")