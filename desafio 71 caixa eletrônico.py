while True:
    n = int(input(' valor a ser sacado: '))
    cinq = n // 50
    res = n - (cinq * 50)
    vint = res // 20
    res1 = n - ((cinq * 50)+(vint * 20))
    dez = res1 // 10
    res2 = n - ((cinq * 50)+(vint * 20) +(dez * 10))
    um = res2 // 1
    break
if cinq > 0:
    print(f'{cinq} de galo')
if vint > 0:
    print(f'{vint} de 20')
if dez > 0:
    print(f'{dez} de 10')
if um > 0:
    print(f'{um} notas de um, que nem existem mais')

    