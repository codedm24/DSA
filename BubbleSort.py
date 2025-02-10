array1 = [64,34,25,12,22,11,90]

n = len(array1)

for i in range(n-1):
    print(f"i: {i}")
    for j in range(n-i-1):
        print(f"j: {j}")
        if(array1[j] > array1[j+1]):
            array1[j], array1[j+1] = array1[j+1], array1[j]

print(f"Sorted array: {array1}")