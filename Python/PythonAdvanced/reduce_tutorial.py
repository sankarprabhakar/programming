from functools import reduce


if __name__ == "__main__":
    ##reduce syntax
    ## reduce(func, iterable,[intial value])
    ## Reduce function reduces the iterable to one value. 
    ## func --takes two argument, i.e first and second element from iterables, then gets a result
    ## this result will be passed to func again with 3rd element in the iterable so on and so forth.

    ##if initial value is given, then on first iteration then initial value and first elment of iterable will be passed to func    

    ## Finding sum of values of a list
    my_int_list = [1,2,3,4,5]
    def custom_sum(a,b):
        return a+b

    print(reduce(custom_sum,my_int_list))

    print(reduce(custom_sum,my_int_list,10)) 
