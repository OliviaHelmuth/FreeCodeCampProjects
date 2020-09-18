arr = [1, 5, 24, 1, 54, 42, 11]

max_value = arr[0]
min_value = arr[0]
for i in arr:
    if i > max_value:
        max_value = i
    if i < min_value:
        min_value = i

print(max_value)
print(min_value)


arr = [1, 1, 2, 4, 4, 4, 5, 7, 7]
# -> arr = [1, 2, 4, 5, 7]

arr2 = list(set(arr))

print(arr2)
