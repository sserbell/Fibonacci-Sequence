#Name: Sharon Serbellon Barralaga
#Project Name: Fibonacci Sequence

def fibonacci(num):                           #Fibonacci Function
    sequence = []
    first = 0                            #setting the first and second numbers of the fibonacci sequence
    second = 1
    for i in range(num - 1):
        if i == 0:
            sequence.append(first)
        if i == 1:
            sequence.append(second)
        else: 
            num_add = first + second       
            sequence.append(num_add)
            first = second               #updating the numbers that need to be added for the next number in the sequence
            second = num_add
    return sequence
num = int(input("Enter a number: "))
fib_sequence = fibonacci(num)
print(f'The Fibonacci Sequence of {num} is: {fib_sequence}')
