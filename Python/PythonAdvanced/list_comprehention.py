## Example 1
## Split the string into a list of literal eg: Hello as a list of 'H','e','l','l','o'

# without list comprehention 
hello = "Hello"
hello_list = []
for let in hello:
    hello_list.append(let)
print(hello_list)

print("Using list comprehention")

hello_list = [let for let in hello]
print(hello_list)

### syntax is [expression for iter in itertable]


## Problem get list of even numbers
print("Prob#2 : List of even numbers")
my_even_list = [i for i in range(20) if i%2 ==0]
print(my_even_list)

print ("Prob#3 : List of even number and divisible by 5")
my_div_5_list = [i for i in range(50) if i%2 ==0  if i%5 ==0]
print(my_div_5_list)

print ("Prob#4 : Nexted list comprehend")
matrix = [[1, 2], [3,4], [5,6], [7,8]]
transpose = [[row[i] for row in matrix] for i in range(2)]
print (transpose)

