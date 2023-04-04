from audioop import mul


if __name__ == "__main__":
    print("Hello world")
    ## Map function args is as below
    ##syntax
    ## map(func, *iterable) ; function would be applied to each element of iterable
    ## if func is having 2 arg, two iterable can be passed. func will take first element
    ## from first iterable and second from the second iterable

    ## return value is map object which is a generator. List is applied to print elements.
    
    def doubler(x):
        return 2*x
    
    my_number = [1,2,3,4,5]
    print(list(map(doubler,my_number)))

    def multiplier(a,b):
        return a *b
    
    my_a_list = [1,2,3]
    my_b_list = [3,4,5]

    print(list(map(multiplier, my_a_list, my_b_list)))


    ## if the iterables are not of same size then return would be 
    my_a_list = [1,2,3,4,5,6,7] ## 7 elements
    my_b_list = [1] # 1 element

    print(list(map(multiplier, my_a_list, my_b_list))) ## output will be only on element

    ## Example of rounding 
    circle_area = [2.3423423,4.4543452345,3.5642345,7.756543645]
    print(list(map(round,circle_area,range(1,5)))) ## each element in area will be rounded to 1,2,3,4 digits respectively


    ## implementation of zip function using map
    my_alphabets = ['a','b','c','d']
    my_number = [1,2,3,4]

    print(list(map(lambda a,b: (a,b), my_alphabets, my_number )))

