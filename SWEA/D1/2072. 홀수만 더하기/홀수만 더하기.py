T = int(input())

for i in range(T):
    num_list = list(map(int, input().split()))
    odd_num_list = [x for x in num_list if x % 2 != 0]
    print(f"#{i+1} {sum(odd_num_list)}")
