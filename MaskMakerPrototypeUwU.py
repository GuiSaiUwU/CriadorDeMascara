#  Perguntar a quantidade de ossos total.
#  Criar uma lista com essa quantidade de ossos apenas com Zeros.
#  Perguntar os ossos que irá colocar o valor de máscara.
#  O valor ser possível de editar, entre 0.1 e 1.
import time

qtd_total = ""  # Definindo uma “string” vazia para usar no ciclo abaixo ^^

while not qtd_total.isnumeric() or qtd_total == "0":
    # Ciclo infinito enquanto a pessoa não digitar um valor numérico inteiro
    # Também enquanto o usuário não colocar um número maior que 0
    qtd_total = input("Qual a quantidade de ossos total? ")
    if not qtd_total.isnumeric() or qtd_total == "0":
        # Se a entrada não for um valor numérico, ou for igual a 0
        print("Por favor, insira um número")

# Assim que sair do ciclo, irá transformar num valor de número inteiro
qtd_total = int(qtd_total)

# Explicação de como o usuário deve digitar
print("\nDigite os ossos que vão sofrer influência, separe por virgula.")
print("Exemplo: 12,13,14,15,64,65")

ossos_com_mask = input("Insira: ")
# Transformar o input do usuário em lista, separada por vírgula
ossos_com_mask = ossos_com_mask.split(",")

print("A máscara deve conter um valor entre 0 e 1.\nExemplo de valor quebrado: 0.5")

#  Ciclo infinito até o input ser um número
while True:
    valor_mask = input("Qual o valor da máscara? ")

    try:
        # Testando se o input é possível transformar em float
        valor_mask = float(valor_mask)

        #  Se o valor da máscara for menor que
        if 0 >= valor_mask:
            print("A Máscara não pode valer 0, ou menor que 0! ")

        elif valor_mask == 1:
            break  # Esse break aqui se não iria ficar em 1 ciclo para sempre :D
        if valor_mask != 0 and valor_mask > 0:
            break  # Mesma coisa do break anterior

    except Exception as erro:
        print("Por Favor, digite um número LOL!")
        error = erro  # Essa variável só existe pq o PyCharm tava enchendo o saco

#  Criar a estampa de tempo em base na data, e hora
tempo = time.strftime("%d-%m-%y-=-%H.%M.%S", time.localtime())

#  Criando o arquivo ->
with open(f"Mask-{tempo}.txt", "x") as file:
    file.write("Obrigado por usar meu app <3\n")  # Linha 1
    file.write("Escrevendo máscara:\n\n")  # Linha 2 e 3
    file.write("        mMaskDataMap: map[hash,embed] = {\n")  # Cabeçalho de uma máscara
    file.write('            "MaskUwU" = MaskData {\n')  # Nome da máscara uwu
    file.write('                mWeightList: list[f32] = {\n')  # Sla só se que precisa disso haha

    #  Iterando sobre o número de ossos total
    for i in range(qtd_total):
        i += 1  # Precisa disso para arrumar um erro aí de escrever a máscara 1 casa antes
        i = str(i)  # Converter inteiro pra string

        if i in ossos_com_mask:  # Testar se a string está na lista de strings
            #  Exemplo: ["2","3","4","16"]
            #  Se tiver em um desses valores, irá escrever a máscara
            file.write(f"                    {valor_mask}\n")

        else:
            #  Se não tiver irá escrever 0
            file.write("                    0\n")
    file.write("                }\n            }")  # Criando as últimas 2 linhas duma máscara :D
