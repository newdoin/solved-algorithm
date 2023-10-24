T = int(input())

for i in range(T):
    operator = "<"
    a, b = map(int, input().split())
    if a > b:
        operator = ">"
    elif a == b:
        operator = "="
    print(f"#{i+1} {operator}")