#Bubble sort
run_code = 1
array1 = [64,34,25,12,22,11,90]

n = len(array1)

if run_code == 1:

    for i in range(n-1):
        print(f"i: {i}")
        for j in range(n-i-1):
            print(f"j: {j}")
            if(array1[j] > array1[j+1]):
                array1[j], array1[j+1] = array1[j+1], array1[j]

    print(f"Sorted array: {array1}")

elif run_code == 2:
    
    #Bubble sort improvement
    for i in range(n-1):
        #print(f"i: {i}")
        swapped = False
        for j in range(n-i-1):
            print(f"j: {j}")
            if(array1[j] > array1[j+1]):
                array1[j], array1[j+1] = array1[j+1], array1[j]
                swapped = True
        if not swapped:
            break
    print(f"Sorted array: {array1}")