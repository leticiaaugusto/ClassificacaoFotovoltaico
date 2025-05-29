from sklearn.tree import DecisionTreeClassifier
import pandas as pd

 

df = pd.read_csv("Dados.csv")

dados = df[["tensao","corrente","potencia"]]
target = df ["manutencao"]



# Criando o classificador.
decisao = DecisionTreeClassifier()

# Treinar o modelo.
decisao.fit(dados, target)

print("--Verificando condições dos Sistemas fotovoltaicos.--\n")

# Fazer a previsão de sim ou não.
sistemas = {
    "Sistema 1": [21, 5,  100],
    "Sistema 2": [37, 9,  300],
    "Sistema 3": [31, 9,  280],
    "Sistema 4": [38, 9,  301],
    "Sistema 5": [37, 8.8,299],
    "Sistema 6": [0.5,1, 0]
}

for nome, valores in sistemas.items():
    modulo = pd.DataFrame([valores], columns= ["tensao","corrente","potencia"])
    resultado = decisao.predict(modulo)

    if resultado[0] == 1:
        print(f"{nome}: Sistema não necessita de manutenção.\n")
    elif resultado[0] == 2:
        print(f"{nome}: Sistema com falha ou desligado.\n")
    else:
        print(f"{nome}: Sistema necessita de manutenção urgente, valores abaixo da média!!!\n")