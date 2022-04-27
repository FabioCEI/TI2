print("\tPROGRAMA PARA VERIFICACAO DE NUMEROS PRIMOS")

cont = 1
divisor = 0
 
while True:   
    try:
        num = int(input("\nNumero: "))
        if num < 0:
            print("APENAS POSITIVOS")
    except ValueError:
        print("APENAS NUMEROS")
    try:
        while True:
            num1 = num % cont
            if num1 == 0:
                divisor = divisor + cont
            cont += 1
            if cont > num:
                break
            
        if divisor == num + 1:
            print(f"\n{num} é numero primo")
        else:
            print(f"\n{num} não é numero primo")
    except num == 2:
        print("\n2 é numero primo")
    
    while True:
        sn = input("\nGostaria de imprimir outro numero? (S/N): ").upper()
        if sn not in ["S", "N"]:
            print("S/N")
        if sn == "N":
            break
        else:
            break
    if sn == "N":
        break