def sum_natural_loop(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

n = int(input("Enter a number: "))
print("Sum:", sum_natural_loop(n))
