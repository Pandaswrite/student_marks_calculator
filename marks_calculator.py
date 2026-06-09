subjects = []

for i in range(6):
    mark = float(input(f"Enter marks for subject {i+1}: "))
    subjects.append(mark)

total = sum(subjects)
percentage = total / 6

print("\nTotal Marks:", total)
print("Percentage:", percentage)

if percentage >= 35:
    print("Result: PASS")
else:
    print("Result: FAIL") 
