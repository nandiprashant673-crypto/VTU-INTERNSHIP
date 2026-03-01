class AgeTooSmallError(Exception):
    pass

try:
    age = int(input("Enter your age: "))
    if age < 18:
        raise AgeTooSmallError
    else:
        print("You are eligible.")
except AgeTooSmallError:
    print("Error: Age must be 18 or above.")
