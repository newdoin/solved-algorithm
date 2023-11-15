day_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
total = 0
day_sum = [0]
for day in day_list:
    total += day
    day_sum.append(total)

T = int(input())

for tc in range(1, T + 1):
    m1, d1, m2, d2 = map(int, input().split())
    answer = (d2 + day_sum[m2-1]) - (d1 + day_sum[m1-1]) + 1
    print(f"#{tc} {answer}")