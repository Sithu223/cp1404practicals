for i in range(1, 21, 2):
    print(i, end=' ')
print()

# a.
for second in range(0, 101, 10):
    print(second, end=" ")
print()

# b.
for second in range(20, 0, -1):
    print(second, end=" ")
print()

# c.
number_of_stars = int(input("Number of stars: "))
print(number_of_stars * "*")

# d.
number_of_star = int(input("Number of stars: "))
for i in range(number_of_star):
    print("*" * (i+1))
print()