# Iterator are classes which defines two method
# __iter__()
# __next__()
#

# Example of list iterator

from re import T


my_list = [1,2,3,4,5]
## to create iterator from list object
my_list_iter = iter(my_list)
print(next(my_list_iter))
print(next(my_list_iter))
print(next(my_list_iter))
print(next(my_list_iter))
print(next(my_list_iter))
try:
    print(next(my_list_iter)) ## StopIteration excepiton 
except StopIteration:
    print("Got stop iterator")


## Creating your own iterator
class Even:
    def __init__(self, n):
        print("init is called ")
        self.max = n
        #return self
    def __iter__(self):
        print("iter is called ")
        self.n = 2
        return self
    def __next__(self):
        #print("Next is called")
        if self.n < self.max:
            result = self.n
            self.n += 2
            return result
        else:
            raise StopIteration

## Go over the iterator.
even_iter = Even(10)
for i in even_iter:
    print(i)

## Getting iterator with iter method
even_iter1 = Even(10)
even_iter1_ = iter(even_iter1)

for i in even_iter1_:
    print(i)


## Go over a list using While loop. Similar while loop is what for construct uses 
# in for <<variable>> in <<iterator>>
my_a_list = [1,2,3]
list_iter = iter(my_a_list)
while(True):
    try:
        result = next(list_iter)
        print(result)
    except:
        raise StopIteration


