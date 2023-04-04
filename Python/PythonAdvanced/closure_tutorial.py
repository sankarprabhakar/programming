# Python closure is a nested function that allows us to access variables of the outer function even after the outer function is closed.

## 1 . Example of nexted function

def print_hi(name):
    def hi():
        print("Hi " + name)
    hi()

print_hi("sankar")

## 2.  accessing a local variable after out function dies
print("Closure example - Accessing a variable after the funciton exit")
def print_hi(name):
    return lambda : "Hi " + name

greet = print_hi("Paru")
print(greet())

## advantages
# Closures can be used to avoid global values and provide data hiding.
