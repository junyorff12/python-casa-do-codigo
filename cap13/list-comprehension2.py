nested = []
for i in range(2):
    for j in range(3):
        nested.append((i, j))

print("lista 1", nested)

#list comprehension

nested2 = [(i, j, k) for i in range(2) for j in range(3) for k in range(3)]
print("lista 2", nested2)