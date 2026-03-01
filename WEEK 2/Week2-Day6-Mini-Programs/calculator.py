def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b): return a / b

print("1.Add 2.Sub 3.Mul 4.Div")
ch = int(input("Enter choice: "))
a = int(input("Enter a: "))
b = int(input("Enter b: "))

if ch == 1: print("Result:", add(a, b))
elif ch == 2: print("Result:", sub(a, b))
elif ch == 3: print("Result:", mul(a, b))
elif ch == 4: print("Result:", div(a, b))
else: print("Invalid")
