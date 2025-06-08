# 1
FILENAME = "name.txt"
name = input("Enter name: ")
out_file = open(FILENAME, "w")
out_file.write(name)
out_file.close()
