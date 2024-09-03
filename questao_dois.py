print("─"*30)
print("TESTE DO FIBONACCI".center(30))
print("─"*30)

n = int(input("Qual número será testado: "))

fibonacci = [0, 1]

print(f"{fibonacci[0]} → {fibonacci[1]}", end='')

cont = 3

while cont <= 20:  # Esse 20 é para exibir os 20 primeiros termos da sequencia de fibonacci
    t3 = fibonacci[-2] + fibonacci[-1]
    fibonacci.append(t3)
    print(f" → {fibonacci[-1]}", end='')
    t1 = fibonacci[1]
    t2 = fibonacci[-1]
    cont += 1

print("\n")

if n in fibonacci:
    print("O número pertence a sequencia de fibonacci")
else:
    print("O número NÃO pertence a sequencia de fibonacci")

