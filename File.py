def ShowText():
    print("\033[30m\"Don't compare yourself with anyone in this world…")
    print("\033[35mif\033[0m you \033[35mdo so\033[0m, you are insulting yourself.\033[30m\"\033[0m")
    print("Bill Gates")

#ShowText()

def numbersCouple(a, b):
    if a > b:
        z = b
        b = a
        a = z
    elif a == b:
        return
    if a % 2 == 0:
        for i in range(a, b+1, 2):
            print(i)
    else:
        for i in range(a + 1, b+1, 2):
            print(i)

#numbersCouple(11, 101)

def DrawSquare(a, str_='*', bool_=True):
    if bool_:
        for i in range(a):
            print(str_ * a)
    else:
        print((str_ * a), str_ *2, sep='')
        for i in range(a):
            print(str_, ' ' * a,str_, sep='')
        print((str_ * a), str_ *2, sep='')

# DrawSquare(5, '7', False)
# DrawSquare(5)

def minFive(a,b,c,d,e):
    if a < b and a < c and a < d and a < e:
        print(a)
        return
    if b < a and b < c and b < d and b < e:
        print(b)
        return
    if c < b and c < b and c < d and c < e:
        print(c)
        return
    if d < b and d < c and d < a and d < e:
        print(d)
        return
    if e < b and e < c and e < d and e < a:
        print(e)
        return
    
# minFive(1 , 2, 3, 4, -5)

def DobDiapazon(a, b):
    dob = 1
    if a > b:
        z = b
        b = a
        a = z
    for i in range(a,b+1):
        dob *= i
    return dob

# print(DobDiapazon(-1, -3))

def numberNumeric(a):
    count = 0
    while a!=0:
        a = a // 10
        count += 1
    return count

# print(numberNumeric(32))

def Palindrom(a):
    len = numberNumeric(a)
    count = int(len // 2)
    while count != 0:
        count -= 1
        len -= 1
        last = a % 10
        first = a // (10 ** (len))
        if last != first:
            return False
        a = a % (10 ** (len))
        a = a // 10
        len -= 1
    return True

# (Palindrom(1234321))
