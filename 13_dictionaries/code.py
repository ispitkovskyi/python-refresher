friend_ages = {"Rolf": 24, "Adam": 30, "Anne": 27}

friend_ages["Bob"] = 20

print(friend_ages)  # {'Rolf': 24, 'Adam': 30, 'Anne': 27, 'Bob': 20}
print(friend_ages["Bob"])

# -- List of dictionaries --

friends = [
    {"name": "Rolf Smith", "age": 24},
    {"name": "Adam Wool", "age": 30},
    {"name": "Anne Pun", "age": 27},
]

print(friends)

for friend in friends:
    print("Iterate dictionary by elements:")
    print("Name: ", friend["name"], " Age: ", friend["age"])
print("-----------------------------")
for i in range(len(friends)):
    print("Iterate dictionary by index:")
    print("Name: ", friends[i]["name"], " Age: ", friends[i]["age"])

# -- Iteration --
print("==============================================================")
student_attendance = {"Rolf": 96, "Bob": 80, "Anne": 100}

for student in student_attendance:
    print(f"{student}") # prints keys only
    print(f"{student}: {student_attendance[student]}")


# Better!!!
for student, attendance in student_attendance.items():
    print(f"{student}: {attendance}")


# -- Using the `in` keyword --
if "Bob" in student_attendance:
    print(f"Bob: {student_attendance[student]}")
else:
    print("Bob isn't a student in this class!")

# NOTE: It is NOT possible to check if something is among dictionary values. It is possible to only check presense of keys

# -- Calculate an average with `.values()` --

attendace_values = student_attendance.values()
print(sum(attendace_values) / len(attendace_values))
