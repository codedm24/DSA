#Insertion Sort alogrithm

array1 = [64,34,25,12,22,11,90,5]

n = len(array1)

run_code = 1

if run_code == 1:

    for i in range(1,n):
        print(f"i: {i}, value: {array1[i]}")
        insert_index = i
        current_value = array1.pop(i)
        for j in range(i-1,-1,-1):
            print(f"j: {j}, value: {array1[j]}")
            if current_value < array1[j]:
                insert_index = j
        array1.insert(insert_index,current_value)
        print(f"Sorted array: {array1}")
    print(f"Sorted array: {array1}")

elif run_code == 2:

    for i in range(1,n):
        print(f"i: {i}, value: {array1[i]}")
        insert_index = i
        current_value = array1[i]
        for j in range(i-1,-1,-1):
            print(f"j: {j}, value: {array1[j]}")
            if array1[j] > current_value:
                array1[j+1] = array1[j]
                insert_index = j
            else:
                break
        array1[insert_index] = current_value
        print(f"Sorted array: {array1}")
        
    print(f"Sorted array: {array1}")