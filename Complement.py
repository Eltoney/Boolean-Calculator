def comp_9th(n):
    """takes a decimal number (n) in string fomat
        returns the 9's complement of the number"""
    n=str(n)
    result=[]
    for digit in n:
        a=str(9-int(digit))
        result.append(a)
    return "".join(result)
def comp_1st(n):
    """takes a binary number (n) in string fomat
        returns the 1's complement of the number"""
    n=str(n)
    result=[]
    for digit in n:
        a=str(1-int(digit))
        result.append(a)
    return "".join(result)
def comp_2nd(n):
    """takes a binary number (n) in string fomat
        returns the 2's complement of the number"""
    n=str(n)
    count = 0
    for digit in n[::-1]:
        if digit == '1':
            break
        count += 1
    change=n[:len(n)-(count+1)]
    unchange=n[len(n)-(count+1):]
    final=comp_1st(change)
    return final+unchange
def comp_10th(n):
    """takes a decimal number (n) in string format
        return the 10's complement of the number"""
    n=str(n)
    count = 0
    for digit in n[::-1]:
        if digit != '0':
            break
        count += 1
    change=n[:len(n)-(count+1)]
    special=n[len(n)-(count+1):len(n)-count]
    var=str(10-int(special))
    unchange=n[len(n)-count:]
    final=comp_9th(change)
    return final+var+unchange
def decimalSub(m,n):
    """takes 2 decimal numbers in any format(sting or integer)
        return the result of subtraction usin complement rules"""
    m=str(m)
    n=str(n)
    req=max(len(m),len(n))
    while len(m) < req:
        m="0"+m
    while len(n) < req:
        n="0"+n
    if int(n)> int(m):
        n_10th=int(comp_10th(str(n)))
        summation=int(m)+n_10th
        result=comp_10th(str(summation))
        return "-"+result
    else:
        n_10th=int(comp_10th(str(n))) 
        summation=int(m)+n_10th
        result=str(summation)
        return result[1:]
def BinarySum(n,m):
    result=[]
    carry=0
    x=str(n)[::-1]
    y=str(m)[::-1]
    for i in range(len(x)):
        a=int(x[i])+int(y[i])+carry
        if a==1 or a==0:
            result.append(str(a))
            carry=0
        elif a==2:
            result.append("0")
            carry=1
        elif a==3:
            result.append("1")
            carry=1
    if carry==1:
        result.append("1")
    result.reverse()
    return "".join(result)
        
def binarySub(m,n):
    """takes 2 binary numbers in any format(sting or integer)
        return the result of subtraction usin complement rules"""
    m=str(m)
    n=str(n)
    req=max(len(m),len(n))
    while len(m) < req:
        m="0"+m
    while len(n) < req:
        n="0"+n
    if int(n)> int(m):
        n_2nd=comp_2nd(str(n))
        summation=BinarySum(m,n_2nd)
        result=comp_2nd(str(summation))
        return "-"+result
    else:
        n_2nd=comp_2nd(str(n))
        summation=BinarySum(m,n_2nd)
        result=str(summation)
        return result[1:]

operations=[comp_1st,comp_2nd,comp_9th,comp_10th,decimalSub,binarySub]
operation_names=["The first complement of the binary number:",
                 "The second complement of the binary number:",
                 "The ninth complement of the decimal number:",
                 "The tenth complement of the decimal number:",
                 "The difference between the two decimal numbers"
                 "The difference between the two binary numbers"]
print("This program deals with the complment and operations involving them")
n=int(input("Enter number of operations: "))
for num in range(n):
    print("Select the number of operation: ")
    print("0 to find the 1st  complement of a binary  number")
    print("1 to find the 2nd  complement of a binary  number")
    print("2 to find the 9th  complement of a decimal number")
    print("3 to find the 10th complement of a decimal number")
    print("4 to find the differnece between two decimal numbers")
    print("5 to find the differnece between two binary numbers")
    m=int(input("Enter the number of the required operation: "))
    if m==0 or m==1 or m==2 or m==3:
        x=input("Enter the reqired number to convert: ")
        print(operation_names[m],x,"is",operations[m](x))
    elif m==4 or m==5:
        x=input("Enter the first number: ")
        y=input("Enter the second number: ")
        print(operation_names[m],x,"and",y,"is",operations[m](x,y))
    else:
        print("Wrong number of operation selected")
        
    
    

    
    


    
