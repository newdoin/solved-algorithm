T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    n_list = list(map(int, input().split()))
    m_list = list(map(int, input().split()))

    answer = 0

    if N <= M:
        for idx in range(M-N+1):
           answer = max(answer, sum(list(map(lambda x, y: x * y, n_list, m_list[idx:idx + N]))))
    else:
        for idx in range(N-M+1):
           answer = max(answer, sum(list(map(lambda x, y: x * y, m_list, n_list[idx:idx + M]))))

    print(f"#{tc} {answer}")