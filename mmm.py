import menu
from menu import R,G,Y,C,W

menu = f"""-----------------------------------------
TIPOS DE EXERCÍCIO:
{Y}[1]{W} Dados não agrupados
{Y}[2]{W} Dados agrupados por classe

{Y}[0]{W} Sair
-----------------------------------------
"""

def calc_media(nums):
	cont = 0
	soma = 0
	for num in nums:
		cont +=1
		soma += num
	media = soma/cont
	string = f"Media = {soma}/{cont} = {media}"
	print(string)
	return media

def calc_mediana(nums):
	len_nums = len(nums)
	nums.sort()
	print(nums)
	if len_nums%2 == 0:
		indice1 = int((len_nums+1)/2)
		indice2 = indice1+1
		mediana = (nums[indice1-1]+nums[indice2-1])/2
		string = f"mediana = ({nums[indice1-1]} + {nums[indice2-1]}) / 2  =  {mediana}"
		print(string)
	else:
		indice = int((len_nums+1)/2)
		mediana = nums[indice-1]
		string = f"mediana = {nums[indice-1]}"
		print(string) 
	return mediana

def calc_moda(nums):
	dicionario = {}
	for num in nums:
		cont = nums.count(num)
		dicionario.update({num: cont})
	valores_dict = list(dicionario.values())
	maior = max(valores_dict)
	maiores = []
	for k, v in dicionario.items():
		if dicionario[k] == maior:
			maiores.append(k)
	return maiores

def calc_moda_classe():
	print("__________________\nSolicitação da moda para classe:")
	li = float(input("Digite o li: "))
	h = float(input("Digite o h: "))
	d1 = float(input("Digite o d1: "))
	d2 = float(input("Digite o d2: "))
	moda = li + (d1/(d1+d2)*h)
	return moda

def calc_mediana_classe():
	print("__________________\nSolicitação da mediana para classe:")
	li = float(input("Digite o li: "))
	h = float(input("Digite o h: "))
	f = float(input("Digite o f: "))
	fant = float(input("Digite o fant: "))
	n = float(input("Digite o n: "))
	mediana = li + ((n/2 - fant)/f)*h
	return mediana

if __name__ == '__main__':
	pede = True
	while pede:
		try:
			op = int(input("Digite o tipo de exercício: "))
		except Exception as e:
			print(f"{R}!!! Opção Inválida !!!\nDigite novamente{W}")

	pede = True
	nums = []
	while pede:
		try:
			num = int(input("numero: "))
			nums.append(num)
		except ValueError:
			print("Numero Inválido !")
		except KeyboardInterrupt:
			pede = False
			print("")
	numeros = [0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4]

	media = calc_media(nums)
	mediana = calc_mediana(nums)
	moda = calc_moda(nums)

	print("Média:   " + str(media))
	print("Mediana: " + str(mediana))
	print("Moda:    " + str(moda))
	0


	moda_classe = calc_moda_classe()
	print("Moda Classe = " + str(moda_classe))

	mediana_classe = calc_mediana_classe()
	print("Mediana Classe = " + str(mediana_classe))
