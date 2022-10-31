# * Trabalho 01 de CN - Sistema Linear 
print('Trabalho 01 de CN - Sistema Linear \n') 

# & Biblioteca Pandas
import pandas as pd
from IPython.display import display

# & Biblioteca numpy
import numpy as np
from numpy.linalg import solve

# & Biblioteca que pega o arquivo
import os


# & Colocar caminho
arquivo_csv = input("Entre com o caminho do arquivo: \n")

# & Carregar o caminho do CSV
while not os.path.isfile(arquivo_csv):
    print("Arquivo não encontrado... Tente novamente! \n")
    arquivo_csv = input("Entre com o nome arquivo")

try:
    # & Leitura do CSV
    dados_df = pd.read_csv(arquivo_csv, header=0)
    display('\n', dados_df, '- Sistema Linear \n')

    # & Variaveis
    result = dados_df['result'] # * Variavel do resultado
    colunas = dados_df.shape[1] # * Numero de colunas do CSV

    # & Condição para os números de colunas do CSV
    
    if colunas == 1 or colunas == 2:
        # & Sistema com apenas uma ou duas colunas
        print("Sistema indeterminado \n")
    else:
        # & Sistema com 3 ou mais colunas
        array_variavel = dados_df.iloc[:,:colunas - 1]
        
        
        # & Matriz e Vetor
        matriz_variavel = np.array(array_variavel)
        vetor_resultado = np.array(result)
        
        # & Resolve a equação linear
        sistema_resolvido = solve(matriz_variavel, vetor_resultado)
        
        display(matriz_variavel, '- Matriz das variaveis \n')
        display(vetor_resultado, '- Vetor do resultado \n') 
        print(sistema_resolvido, '- Variaveis do sistema resolvido \n')
except BaseException as erro:
    print(f"Erro: {erro}")

print('Integrantes: \n ')
print('Carlos Eduardo de Almeida Carvalho - F14ADF5')
print('Nicolas Sander Zanutelli - N599DG8')
print('Luca Ximenes Melchior - F1875G3')
print('Thiago Infanger Soares da Silva - F1657J9')



