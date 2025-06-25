n1 = int(input("Digite um numero:"))
n2 = int(input("Digite um numero:"))
n3 = int(input("Digite um numero:"))
if n1>n2>n3:
    maior=n1
    menor=n2
if n1>n3>n2:
    maior=n1
    menor=n3
if n2>n1>n3:
    maior=n2
    menor=n1
if n2>n3>n1:
    maior=n2
    menor=n3
if n3>n1>n2:
    maior=n3
    menor=n1
if n3>n2>n1:
    maior=n3
    menor=n2
while menor<maior+1:
    print(menor)
    menor = menor+1
