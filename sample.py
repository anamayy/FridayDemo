def sum_natural(n):
<<<<<<< HEAD
    return n * (n + 1) // 2
=======
    total = 0
    for i in range(1, n + 1):
        total += i
    return total
>>>>>>> main

n = int(input("Enter a number: "))
print("Sum:", sum_natural(n))
