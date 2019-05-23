count = 0

def fakt(n):
    global count
    count += 1
    print(f"N: {n}")
    if n == 0:
        return 1
    return n*fakt(n-1)


print(f"faktorial: {fakt(50)}")
print(f"zavolani: {count}")
