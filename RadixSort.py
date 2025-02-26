#Radix sort algorithm
import logging

logging.basicConfig(level=logging.DEBUG, format='%(levelname)%s: %(message)s')

arr1 = [170,45,75,90,802,24,2,66]

logging.info(f"Original array: {arr1}")

radixArr1 = [[],[],[],[],[],[],[],[],[],[]]

maxVal = max(arr1)

logging.info(f"Max value: {maxVal}")

exp = 1

logging.info(f"Exp: {maxVal // exp}")

while maxVal // exp > 0:
    while len(arr1) > 0:
        num = arr1.pop()
        radixIndex = (num // exp) % 10
        radixArr1[radixIndex].append(num)

    for bucket in radixArr1:
        while len(bucket) > 0:
            val = bucket.pop()
            arr1.append(val)
    
    exp *= 10

logging.info(f"Sorted array: {arr1}")