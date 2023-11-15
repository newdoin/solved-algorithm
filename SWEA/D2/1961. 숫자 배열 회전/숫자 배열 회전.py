"""
(0, 0), (0, 1), (0, 2)
(1, 0), (1, 1), (1, 2)
(2, 0), (2, 1), (2, 2)

90도 회전!
(2, 0), (1, 0), (0, 0)
(2, 1), (1, 1), (0, 1)
(2, 2), (1, 2), (0, 2)

90도 회전한거에 90도 회전! => 180도!!
(2, 2), (2, 1), (2, 0)
(1, 2), (1, 1), (1, 0)
(0, 2), (0, 1), (0, 0)

90도 회전한거에 90도를 또 회전한거에 90도 회전!! => 270도!!!
(0, 2), (1, 2), (2, 2)
(0, 1), (1, 1), (2, 1)
(0, 0), (1, 0), (2, 0)
"""
T = int(input())

for i in range(T):
    N = int(input())

    map_list = [list(input().split()) for _ in range(N)]
    rotate_90 = [[0] * N for _ in range(N)]
    rotate_180 = [[0] * N for _ in range(N)]
    rotate_270 = [[0] * N for _ in range(N)]

    for row in range(N):
        for col in range(N):
            rotate_90[row][col] = map_list[N - col - 1][row]

    for row in range(N):
        for col in range(N):
            rotate_180[row][col] = rotate_90[N - col - 1][row]

    for row in range(N):
        for col in range(N):
            rotate_270[row][col] = rotate_180[N - col - 1][row]

    print(f"#{i+1}")
    for idx in range(N):
        print(''.join(rotate_90[idx]), end=' ')
        print(''.join(rotate_180[idx]), end=' ')
        print(''.join(rotate_270[idx]), end=' ')
        print()