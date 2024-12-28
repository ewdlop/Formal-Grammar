# A non-1NF table with non-atomic values
table = {
    "ID": [1, 2],
    "Name": ["Alice", "Bob"],
    "PhoneNumbers": [["123-4567", "234-5678"], ["345-6789"]]
}

# A 1NF table with atomic values
table_1nf = {
    "ID": [1, 1, 2],
    "Name": ["Alice", "Alice", "Bob"],
    "PhoneNumber": ["123-4567", "234-5678", "345-6789"]
}

print(table_1nf)
