mydict = {"python": "a programming language"}

while True:
    print("\n1. Add\n2. Search\n3. Display\n4. Exit")
    ch = input("Choice: ")

    if ch == "1":
        k = input("Word: ")
        v = input("Meaning: ")
        mydict[k] = v
    elif ch == "2":
        k = input("Enter word: ")
        print(mydict.get(k, "Not found"))
    elif ch == "3":
        print(mydict)
    elif ch == "4":
        break
