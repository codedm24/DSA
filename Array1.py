array1 = [7,12,9,4,11]
min_val = array1[0]

for item in array1:
    if item < min_val:
        min_val = item

print(f"Min val: {min_val}")

#code check
gen = (i for i in range(10))
print(list(gen))
print(list(gen))