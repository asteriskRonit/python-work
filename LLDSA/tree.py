x = list(map(int, input("Enter multiple values: "). split()))
print(x[0])
for c in range(int(input())):
    vc = list(map(int, input().split()))
    y = (vc[0] / 10) * vc[1]
    print(y)
