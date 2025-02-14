#Selection sort

array1 = [64,34,25,5,22,11,90,12]

n = len(array1)

code_run = 2

if code_run == 1:

    for i in range(n-1):
        min_index = i
        for j in range(i+1,n):
            if(array1[j] < array1[min_index]):
                min_index = j
        min_value = array1.pop(min_index)
        array1.insert(i,min_value)

    print("Sorted array {}".format(array1))

elif code_run == 2:
    
    for i in range(n-1):
        #print(f"i:{i}:{array1[i]}")
        min_index = i
        for j in range(i+1,n):
            #print(f"j:{j}:{array1[j]}")
            if(array1[j] < array1[min_index]):
                min_index = j
        array1[i], array1[min_index] = array1[min_index], array1[i]

    print("Sorted array {}".format(array1))