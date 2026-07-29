def armstrong(n):
    num=n
    total=0
    nod=len(str(n))
    while num>0:
        ld=num%10
        total=total+(ld**nod)
        num=num//10
    return total==n

print(armstrong(153))