N = int(input())
num_list = list(map(int, input().split()))
sorted_num_list = sorted(num_list)
print(sorted_num_list[N//2])