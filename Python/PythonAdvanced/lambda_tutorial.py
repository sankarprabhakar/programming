#print("Hello welcome")
## Note : Lamda function is used when we need an anonymous function for a shorter period of time
if __name__ == "__main__":
    ## lamda syntax is as belw
    # lamda parameters : expression

    x = lambda a : a+10
    print(x(20))
    # lambda can take any number of arguments
    x = lambda a,b,c :  a+b+c
    print(x(4,5,6))

    x = lambda a, b : a if a > b else b
    print(x(5,50))
    x = lambda a, b,c : a if (a > b and a > c)  else b if ( b>a and b>c) else c
    print(x(5,150,100))

    
    