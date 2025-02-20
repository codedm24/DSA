run_segment = 2
#Fibonacci series using a for loop
if run_segment == 1:
    prev1 = 0
    prev2 = 1
    print(prev1)
    print(prev2)
    for i in range(10):
        newfibo = prev1 + prev2
        print(newfibo)
        prev1 = prev2
        prev2 = newfibo
elif run_segment == 2:
    print(0)
    print(1)
    count = 0

    def fibonacci(prev1,prev2):
        global count
        newfibo = prev1 + prev2
        print(newfibo)
        count += 1
        prev2 = prev1
        prev1 = newfibo
        if count <= 19:
            fibonacci(prev1,prev2)        
        else:
            return
        
fibonacci(1,0)        