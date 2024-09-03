print("─"*30)
palavra = str(input("Digite uma palavra: "))
print("─"*30)

for i in range(len(palavra) -1, -1, -1):
    print(palavra[i], end='')

