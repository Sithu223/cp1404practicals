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


