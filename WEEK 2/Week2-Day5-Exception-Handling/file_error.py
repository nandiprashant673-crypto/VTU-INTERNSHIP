try:
    file = open("nofile.txt", "r")
    print(file.read())
except FileNotFoundError:
    print("Error: File not found.")
