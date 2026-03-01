while True:
    print("\n1. Say Hello\n2. Show Date\n3. Exit")
    ch = input("Enter choice: ")

    if ch == "1":
        print("Hello User!")
    elif ch == "2":
        import datetime
        print(datetime.date.today())
    elif ch == "3":
        break
    else:
        print("Invalid choice")
