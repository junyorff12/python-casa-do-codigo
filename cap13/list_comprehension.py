numbers = []

for i in range(5):
    numbers.append(i)

print("lista 1", numbers)

# list comprehension

numbers2 = [i for i in range(5)]
print("lista 2", numbers2)


numbers_time_2 = [i*2 for i in range(5)]
print("lista 3", numbers_time_2)

evens = [i for i in range(5) if i % 2 == 0]
print("lista 4", evens)