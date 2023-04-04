if __name__ == "__main__":
    ## zip syntax
    ## zip(*iterables)
    ## return a tuples. First tuple is formed fromh first elments of all iterators, 
    ## second tuple from second element of iterator etc etc.

    my_a_list = [1,2,3,4,5]
    my_b_list = ['a','b','c','d','e']
    my_c_list = [1.1,1.2,1.3,1.4,1.5]
    for item in zip(my_a_list,my_b_list,my_c_list):
        print(item) 


    print(list(zip(my_a_list,my_b_list,my_c_list)))
