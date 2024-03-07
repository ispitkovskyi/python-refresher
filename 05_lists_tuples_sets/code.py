l = ["Bob", "Rolf", "Anne"] # Lists and tuples always keep the order of elements
t = ("Bob", "Rolf", "Anne")
s = {"Bob", "Rolf", "Anne"} # Sets do NOT guarantee order of elements

# Access individual items in lists and tuples using the index.

print(l[0])
print(t[0])
# print(s[0])  # This gives an error because sets are unordered, so accessing element 0 of something without order doesn't make sense.

# Modify individual items in lists using the index.

l[0] = "Smith"
# t[0] = "Smith"  # This gives an error because tuples are "immutable".

print(l)
print(t)

# Add to a list by using `.append`
l.append("Jen")
print(l)
# Removal
l.remove("Smith")
print(l)


# Tuples cannot be appended to because they are immutable.

# Add to sets by using `.add`
s.add("Jen")
print(s)

# Sets can't have the same element twice.
s.add("Bob")
print(f"Set after adding Bob {s}")
print(f"Print poped element: {s.pop()}") # removes 1st element from set and returns it
print(f"Set after poping element {s}")

s.remove("Rolf") # removes element from set
print(f"Set after removal of Rolf {s}")


