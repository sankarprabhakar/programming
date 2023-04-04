if __name__ == "__main__":
    ## filter syntax 
    ## filter(func, iterable)
    ## func --> takes one argument and return true or false.
    ## filter return all the element of iterable for which the func returned true.

    ## filtering out odd numbers from the list (out put only even)
    my_a_list = [1,2,3,4,5,6,7,8,9,10]
    def is_even(x):
        return x % 2 == 0
    print(list(filter(is_even,my_a_list)))

    ##filter out the even number from the list (print only odd)
    def is_odd(x):
        return x % 2 == 1
    print(list(filter(is_odd,my_a_list)))


    ## revesing a string
    input_str  = "Hello world"
    print(input_str[::-1])

    ##filter out palindromes
    my_str_list = ["madam", "dad", "cow", "supply", "python", "chetak"]

    print(list(filter(lambda x : x == x[::-1], my_str_list)))
    

