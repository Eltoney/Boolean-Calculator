### number of operation block
def user():
    print("Welcome, This program if for calcualting minterms and maxterms of a boolean function")
    oper=int(input("Enter number of operation you are going to perform: "))
    for opr in range(oper):
        main()


    
def main():
    ### This block is for filling the truth table of n variables (variable name -> var)
    ### It depends on the 2^n rule for deciding the number of places in the truth table
    ### filling the truth table is done by using 2^(n-1)
    var=int(input("Enter the number of used variables in the function(Between 2 and 6): "))
    assert (var > 1 and var <= 6) ,"Wrong number of variable"
    x,y,z,m,n,o=[],[],[],[],[],[]
    a=var-1
    while True:
        while len(x) < 2**var:
            x += [0] *int(2**a)
            x += [1] *int(2**a)
        a-= 1
        
        while len(y) < 2**var:
            y += [0] *int(2**a)
            y += [1] *int(2**a)
        if a==0:
            break
        a-= 1
        while len(z) < 2**var:
            z += [0] *int(2**a)
            z += [1] *int(2**a)
        if a==0:
            break
        a-= 1
        while len(m) < 2**var:
            m += [0] *int(2**a)
            m += [1] *int(2**a)
        if a==0:
            break
        a-= 1
        while len(n) < 2**var:
            n += [0] *int(2**a)
            n += [1] *int(2**a)
        if a==0:
            break
        a-= 1
        while len(o) < 2**var:
            o += [0] *int(2**a)
            o += [1] *int(2**a)
        if a==0:
            break
    ### the end of buliding truth block
    ################################################
    ### this block is for replacing the real terms with appropriate terms for calculation
    print("Please notice that the variables for the function are ")
    print("x, y, z, m, n, o in order of increasing number of terms")
    print("please enter small letters only")
    print("Avaliable operation: \n 1.And operation: use . for it \n 2.Or operation: use + for it \
    \n 3.Not operation: use ~ for it")
    print('{:^25}{:^48}'.format("functions samples","correct input examples"))
    print('{:>15}{:>35}'.format("xy + x'z","x.y+~x.z"))
    print('{:>15}{:>40}'.format("xy + x'z","x . y + ~ x . z"))
    print('{:^15}{:>40}'.format("x'yz + xy'z + xyz' + xyz","~x.y.z + x.~y.z + x.y.~z + x.y.z"))
    print("Please don't forget to restrict to our variables names")
    print("Enter your function:")
    func=list(input())
    e=" ".join(func)
    if 'x' in e:
        e=e.replace('x','x[j]')
    if 'y' in e:
        e=e.replace('y','y[j]')
    if 'z' in e:
        e=e.replace('z','z[j]')
    if 'm' in e:
        e=e.replace('m','m[j]')
    if 'n' in e:
        e=e.replace('n','n[j]')
    if 'o' in e:
        e=e.replace('o','o[j]')
    if '.' in e:
        e=e.replace('.','and')
    if '+' in e:
        e=e.replace('+','or')
    if '~' in e:
        e=e.replace('~','not')
    ### the end of function processing block
    ################################################
    ### this block for calculation and results
    result = []
    try:
        for j in range(len(x)):
            result.append(int(eval(e)))
            min_terms=[str(i) for i, x in enumerate(result) if x == 1]
        max_terms=[str(i) for i, x in enumerate(result) if x == 0]
        print("The minterm(s) for your function is(are):",", ".join(min_terms),"terms")
        print("The maxterm(s) for your function is(are):",", ".join(max_terms),"terms")
    except:
        print("Wrong variable used or wrong function notation")
        print("please READ the instruction again before performing the operation again")
        main()
        
        

user()

        
        

        
        
