## Yield causes creation of generator object.

def my_generator(n):
    value = 0
    while value < n:
        yield value
        #print("coming here 1")
        value += 1
    
def my_func():
    yield "Hello"

if __name__ == "__main__":
    for i in my_generator(10):
        print(i)

## How to get generate item from 
print("Accesing items in a iterator using the Next funciton  !!!!!!")
generator = my_generator(3)
print(next(generator))
print(next(generator))
print(next(generator))

print("Checking the yield funcationality")
x = my_func()
print(next(x))
#print(next(x))

print("Python generator expression")
## PYTHON GENERATOR EXPRESSION
## SYNTAX
# (expression for item in iterable)
# Example 
my_int_list = [1,2,3]
square_generator = (i * i for i in my_int_list)
for i in square_generator:
    print(i)


## Advantages of generator
##. Easy to implement compared to iterators. (most of the error handling is done by generator so less code)
##. memory efficient
##. infinite stream
##. pipeline of generator
print("Pipelining of generators ")

def fibonacci_numbers(nums):
    x, y = 0, 1
    for _ in range(nums):
        x, y = y, x+y
        yield x

def square(nums):
    for num in nums:
        yield num**2

print(sum(square(fibonacci_numbers(10))))