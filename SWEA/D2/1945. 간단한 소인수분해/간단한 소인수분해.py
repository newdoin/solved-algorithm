T = int(input())
for i in range(T):
    count_dict = {
        "2":0, 
        "3":0, 
        "5":0, 
        "7":0, 
        "11":0
        }
    N = int(input())
    while N != 1:
        for num in count_dict.keys():
            if N % int(num) == 0:
                N = N // int(num)
                count_dict[num] += 1
    print(f"#{i+1}", end=' ')
    for key, val in count_dict.items():
        print(val, end=' ')
    print()