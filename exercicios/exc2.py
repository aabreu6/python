# 2 - Leia duas strings do usuário e escreva na tela qual das duas é a maior string.
str1 = input("Digite algo: ")
str2 = input("Digite algo: ")
tamanho1 = len(str1)
tamanho2 = len(str2)
if tamanho1 > tamanho2:
    print(f"{str1} é maior")
elif tamanho1 < tamanho2:
    print(f"{str2} é maior")