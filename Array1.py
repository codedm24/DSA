array1 = [7,12,9,4,11]
min_val = array1[0]

for item in array1:
    if item < min_val:
        min_val = item

print(f"Min val: {min_val}")