# soal 36

def BiggestNum(num1,num2,num3):
    if num1>num2 and num1>num3:
        return num1
    elif num2>num1 and num2>num3:
        return num2
    elif num3>num2 and num3>num1:
        return num3
    
# soal 37

def SortNums(num1,num2,num3):
    if num1>num2 and num1>num3:
        BiggestNum = num1
    elif num2>num1 and num2>num3:
        BiggestNum = num2
    elif num3>num2 and num3>num1:
        BiggestNum = num3
    if num2>num3 and num2<num1:
        MiddleNum = num2
    elif num2<num3 and num2>num1:
        MiddleNum = num2
    elif num1>num3 and num1<num2:
        MiddleNum = num1
    elif num1<num3 and num1>num2:
        MiddleNum = num1
    elif num3>num1 and num3<num2:
        MiddleNum = num1
    elif num3<num1 and num3>num2:
        MiddleNum = num1
    if num1<num2 and num1<num3:
        SmallestNum = num1
    elif num2<num1 and num2<num3:
        SmallestNum = num2
    elif num3<num2 and num3<num1:
        SmallestNum = num3
    print("Biggest Number : ",BiggestNum,"MiddleNumber : ",MiddleNum,"Smallest Number : ",SmallestNum)

# soal 38

def CurrentWeek(day):
    if day<8:
        print("1st week")
    elif day>7 and day<15:
        print("2nd week")
    elif day>14 and day<22:
        print("3rd week")
    elif day>21 and day<29:
        print("4th week")

# soal 39

def remove_zero():
    x = int(input("enter a number: "))

    x_str = str(x)
    final_str = ""

    for char in x_str:

        if char != '0':
            final_str += char

    print(final_str)

# soal 40

def sumbinaries():
    number1 = input("enter Number 1 : ")
    number2 = input("enter Number 2 : ")

    if(number1 == "111" and number2 == "111"):
        print("1110")
    elif(number1 == "111" and number2 == "110" or number2 == "111" and number1 == "110"):
        print("1101")
    elif(number1 == "111" and number2 == "100" or number2 == "111" and number1 == "100"):
        print("1011")
    elif(number1 == "111" and number2 == "101" or number2 == "111" and number1 == "101"):
        print("1100")
    elif(number1 == "111" and number2 == "101" or number2 == "111" and number1 == "101"):
        print("1100")

# soal 66

def count_odd_fibonacci():
    count = 0

    for i in range(100):
        num = int(input("enter a number: "))
        a, b = 0, 1

        while b <= num:
            if b % 2 == 1:
                count += 1
            a, b = b, a + b

    print(count)

# soal 67

def count_fibonacci_factors(n):
    count = 0
    a, b = 0, 1

    while a <= n:
        if n % a == 0:
            count += 1
        a, b = b, a + b

    print(count)

# soal 68

def zero_count():
    x = int(input("enter a number: "))
    count = 0
    x_str = str(x)

    for char in x_str:

        if char == '0':
            count += 1

    print(count)

# soal 69

def remove_zeroes():
    x = int(input("enter a number: "))

    x_str = str(x)
    final_str = ""

    for char in x_str:

        if char != '0':
            final_str += char

    print(final_str)

# soal 70

def factors():
    for i in range(56,1985):
        for j in range(1,i):
            if i % j == 0:
                print(j)

# soal 86

def find_max_number(n):
    max_number = -1

    for i in range(n):
        number = int(input("enter a number : "))

        if number > max_number:
            max_number = number

    print(max_number)

# soal 87

def min_and_max():
    n = int(input("enter count of numbers : "))
    max_number = -1
    min_number = float('inf')
    for i in range(n):
        num = int(input("enter a number : "))
        if num > max_number:
            max_number = num
        elif num < min_number:
            min_number = num
    print(max_number,min_number)

# soal 88

def sortedNum():
    n = int(input("Enter count of numbers: "))
    
    previous_number = int(input("Enter a number: "))
    
    for j in range(1, n):  
        number = int(input("Enter a number: "))
        
        if number < previous_number:
            print("false")
            return
        
        previous_number = number
    
    print("true")

# soal 89

def deleteprimes():
    def isprime(number):
        for j in range(2,number):
            if number % j != 0:
                return True
            else: return False
    nonPrimes = []
    for i in range(10):
        x = int(input("enter number : "))
        if not isprime(x):
            nonPrimes.append(x)
        else: pass
    print(nonPrimes)




# soal 90

def factorial():
    n = int(input("enter count of numbers : "))
    result = 1
    for i in range(n):
        x = int(input("enter number : "))
        for j in range(1,x+1):
            result = j * result
        print(x,"! ",result)
        result = 1

# soal 106

def zojnums():
    count = 0
    for i in range(5):
        x = int(input("enter ur number : "))
        if x%2 == 0:
            count += 1
    print(count)

# soal 107

def avgdistance():
    avg = 0
    x = [0] * 5
    for i in range(5):
        x[i] = int(input("Enter your number: "))
        avg = avg + x[i]
    avg = avg / 5
    for i in range(5):
        if x[i] > avg + 2 or x[i] < avg - 2:
            print(x[i])

# soal 108

def primenumbers():
    x = (int(input("enter count of numbers : ")))
    for i in range(x):
        number = int(input("enter numbers : "))
        for j in range(2,number):
            if number % j != 0:
                print(number)


# soal 109

def factorialll():
    n = int(input("enter count of numbers : "))
    result = 1
    for i in range(n):
        x = int(input("enter number : "))
        for j in range(1,x+1):
            result = j * result
        print(x,"! ",result)
        result = 1

# soal 110

def minimum_and_maximum():
    n = int(input("enter count of numbers : "))
    max_number = -1
    min_number = float('inf')
    for i in range(n):
        num = int(input("enter a number : "))
        if num > max_number:
            max_number = num
        elif num < min_number:
            min_number = num
    print(max_number,min_number)

# soal 117

def capitalize(sentence):
    words = sentence.split()
    result = ""

    for word in words:
        word = word[0].upper() + word[1:]
        result += word + " "

    result = result.rstrip()
    return result

# soal 118

def findnumsinstring():
    x = str(input("write ur string : "))
    numlist = []
    for i in x:
        if i.isdigit():
            numlist.append(i)
    print(numlist)

# soal 119

def removeA():
    x = str(input("write ur string : "))
    newx = []
    for i in x:
        if i != 'a':
            newx.append(i)
    print(newx)

# soal 120

def removeSpace():
    x = str(input("write ur string : "))
    newx = []
    for i in x:
        if i != ' ':
            newx.append(i)
    print(newx)

# soal 121

def sum16digits():
    num1 = str(input("enter ur num : "))
    num2 = str(input("enter ur num : "))
    num1 = int(num1)
    num2 = int(num2)
    print(num1+num2)
