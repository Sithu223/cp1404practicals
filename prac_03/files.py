
# 1
FILENAME = "name.txt"
name = input("Enter name: ")
out_file = open(FILENAME, "w")
out_file.write(name)
out_file.close()
in_file = open(FILENAME, "r")  # 2
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
in_file = open("numbers.txt", "r")
for line in in_file:
    number = int(line)
    total += number
in_file.close()
print(total)