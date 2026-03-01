while True:
    print("\n1. Add Record\n2. View Records\n3. Exit")
    ch = input("Choice: ")

    if ch == "1":
        name = input("Name: ")
        with open("records.txt", "a") as f:
            f.write(name + "\n")
        print("Saved.")
    elif ch == "2":
        with open("records.txt", "r") as f:
            print(f.read())
    elif ch == "3":
        break
