# 1
FILENAME = "name.txt"
name = input("Enter name: ")
out_file = open(FILENAME, "w")
out_file.write(name)
out_file.close()
# 2
in_file = open(FILENAME, "r")
text = in_file.read()
print(f"Your name is {text}")
in_file.close()

# 3
in_file = open("numbers.txt", "r")
line_1 = int(in_file.readline().strip())
line_2 = int(in_file.readline().strip())
print(f"{line_1 + line_2}")

# 4
total = 0
with open("numbers.txt", "r") as in_file:
    for line in in_file:
        number = int(line)
        total += number
print(total)