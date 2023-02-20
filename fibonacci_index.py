def fib_index(indx):
    if indx <= 1:
        return indx
    else:
        return fib_index(indx - 1) + fib_index(indx-2)
    
print("Enter '0' to stop.")
num = int(input('Enter a number: '))
print(fib_index(num))
