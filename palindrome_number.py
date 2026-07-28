def palindrome(n):
    num=n
    result=0
    while num>0:
        ld=num%10
        result=(result*10)+ld
        num=num//10
    return n==result

print(palindrome(1221))