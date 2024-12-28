# Original table
table = {
    "StudentID": [1, 2, 3, 4],
    "Course": ["Math", "Math", "Science", "History"],
    "Instructor": ["Smith", "Smith", "Jones", "Brown"]
}

# Decomposed tables to satisfy BCNF
table1 = {
    "StudentID": [1, 2, 3, 4],
    "Course": ["Math", "Math", "Science", "History"]
}

table2 = {
    "Course": ["Math", "Science", "History"],
    "Instructor": ["Smith", "Jones", "Brown"]
}

print(table1)
print(table2)
