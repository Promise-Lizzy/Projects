#Loop Control Statements

fruits = ["apple", "banana", "cherry", "date"]

for fruit in fruits:
    if fruit =="cherry":
        break  # Exit the loop when fruit is "cherry"
    print(fruit)
    
    print()
    
for fruit in fruits:
    if fruit =="cherry":
        continue  # Skip cherry and move to the iteration
    print(fruit)
    
print()
    
for fruit in fruits:
    if fruit =="cherry":
        pass # Placeholder, no action is needede for cherry
    print(fruit)