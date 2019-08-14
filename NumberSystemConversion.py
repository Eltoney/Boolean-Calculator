Bin_Base=['0','1']
Oct_Base=['0', '1', '2', '3', '4', '5', '6', '7']
Hex_Base=['0', '1', '2', '3', '4', '5', '6', '7','8','9','A','B','C','D','E','F']
def BinTesting(n):
    n=str(n)
    for digit in n:
        if digit in Bin_Base:
            continue
        else:
            return False
    return True
def OctTesting(n):
    n=str(n)
    for digit in n:
        if digit in Oct_Base:
            continue
        else:
            return False
    return True
def HexTesting(n):
    n=str(n)
    for digit in n:
        if digit in Hex_Base:
            continue
        else:
            return False
    return True

def DecToBin(n):
    n=int(n)
    if n==0:
        return 0
    else:
        result=[]
        while n!=0:
            result.append(str(n%2))
            n = n//2
        result.reverse()
        return "".join(result)
def BinToDec(n):
    if BinTesting(n) == False:
        return "Base error"
    n=str(n)
    x=len(n)-1
    result =0
    for digit in n:
        result += int(digit)*2**x
        x -= 1
    return result
def DecToHex(n):
    n=int(n)
    if n==0:
        return 0
    else:
        sys={10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
        result=[]
        while n!=0:
            a=n%16
            if a in sys:
                result.append(sys[a])
            else:
                result.append(str(a))
            n=n//16
        result.reverse()
        return "".join(result)
def HexToDec(n):
    n=str(n)
    if HexTesting(n) == False:
        return "Wrong Base"
    sys={'A':10,'B':11,'C':12,'D':13,'E':14,'F':15} 
    x=len(n)-1
    result =0
    for digit in n:
        if digit in sys:
            a=sys[digit]
        else:
            a=digit
        result += int(a)*16**x
        x -= 1
    return result
def DecToOct(n):
    n=int(n)
    if n==0:
        return 0
    else:
        result=[]
        while n!=0:
            result.append(str(n%8))
            n = n//8
        result.reverse()
        return "".join(result)
def OctToDec(n):
    n=str(n)
    if OctTesting(n) == False:
        return "Base error"
    x=len(n)-1
    result =0
    for digit in n:
        result += int(digit)*8**x
        x -= 1
    return result
def Filter(result):
    while result[0]=='0':
        result = result[1:]
    return result
def HexToBin(n):
    n=str(n)
    if HexTesting(n) == False:
        return "Base error"
    if n=='0':
        return 0
    else:
        sys={'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
        result=[]
        for digit in n:
            if digit in sys:
                a=DecToBin(sys[digit])
                result.append(a)
            else:
                a=DecToBin(digit)
                while len(str(a))<4:
                    a='0'+a
                result.append(a)
        return Filter("".join(result))
def BinToHex(n):
    n=str(n)
    if BinTesting(n) == False:
        return "Base error"
    if n=='0':
        return 0
    else:
        sys={10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
        while len(n)%4 != 0:
            n='0'+n
        value=n
        result=[]
        for i in range((len(n)//4)):
            if i== len(n)//4:
                num = value
                
            else:
                num=value[0:4]
                value=value[4:]
            a=BinToDec(num)
            if a in sys:
                result.append(sys[a])
                
            else:
                result.append(str(a)) 
        return "".join(result)
def OctToBin(n):
    n=str(n)
    if OctTesting(n) == False:
        return "Base error"
    if n =='0':
        return 0
    else:
        result=[]
        for digit in n:
            a=DecToBin(digit)
            while len(str(a))<3:
                a='0'+str(a)
            result.append(a)
        return Filter("".join(result))
def BinToOct(n):
    n=str(n)
    if BinTesting(n) == False:
        return "Base error"
    if n=='0':
        return 0
    else:
        sys={10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
        while len(n)%3 != 0:
            n='0'+n
        value=n
        result=[]
        for i in range((len(n)//3)):
            if i== len(n)//3:
                num = value
                
            else:
                num=value[0:3]
                value=value[3:]
            a=BinToDec(num)
            result.append(str(a)) 
        return "".join(result)
def OctToHex(n):
    a=OctToBin(n)
    b=BinToHex(a)
    return b
def HexToOct(n):
    a=HexToBin(n)
    b=BinToOct(a)
    return b
                
Operations=[DecToBin,BinToDec,DecToHex,HexToDec,DecToOct,OctToDec,HexToBin,BinToHex,OctToBin,BinToOct,OctToHex,HexToOct]
Operations_names=["From decimal to binary is:","From binary to decimal is:",
                  "From decimal to hexadecimal is:","From hexadecimal to decimal is:",
                  "From decimal to octal is:","From octal to decimal is:",
                  "From hexadecimal to binary is:",
                  "From binary to hexadecimal is:","From octal to binary is:",
                  "From binary to octal is:"
                  ,"From octal to hexadecimal is:","From hexadecimal to octal is:"]


def opt():
    print("Number Systems Conversion")
    print("Select the operation by enetering its number from the list below then enter the starting number")
    print("0  From Decimal system to Binary system")
    print("1  From Binary system to Decimal system")
    print("2  From Decimal system to Hexadecimal system")
    print("3  From Hexadecimal system to Deicmal system")
    print("4  From Decimal system to Octal system")
    print("5  From Octal system to Decimal system")
    print("6  From Hexadecimal system to Binary system")
    print("7  From Binary system to Hexadecimal system")
    print("8  From Octal system to Binary system")
    print("9  From Binary system to Octal system")
    print("10 From Octal system to Hexadecimal system")
    print("11 From Hexadecimal system to Octal system")
    opt_ord=int(input("Enter the number of the selected operation: "))
    number=input("Enter the number: ")
    try:
        print("The Conversion of",number,Operations_names[opt_ord],Operations[opt_ord](number))
    except:
        print("Wrong operation number")
count=int(input("Number of operations: "))
for i in range(count):
    opt()




