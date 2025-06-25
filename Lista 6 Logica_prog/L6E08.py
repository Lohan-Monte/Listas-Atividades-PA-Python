n1 = int(input("Digite um numero:"))
while n1>5:
    print("Digite um numero menor que 5.")
    n1 = int(input("Digite um numero:"))
while n1<21:
    n1 = n1+1
    if n1%2==0:
        print(n1)
