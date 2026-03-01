student = {
    "Name": "Prashant",
    "Course": "MCA"
}

print("Original:", student)

student["Marks"] = 90
print("After Add:", student)

student["Marks"] = 95
print("After Update:", student)

del student["Course"]
print("After Delete:", student)
