import pandas as pd
import numpy as np

# 1. Fazer a leitura do arquivo CSV do relatório de vendas
df = pd.read_csv('relatorio_vendas_lanchonete.csv' , sep=';', decimal=',')

# Exibir as primeiras linhas para verificar os nomes das colunas
print("Primeiras linhas do relatório original:")
print(df.head())

coluna_valores = 'Valor total de itens'

ticket_medio = df[coluna_valores].mean()
print(f"\nO Ticket Médio calculado é: R$ {ticket_medio:.2f}")

# 3. Criar as condições para a nova coluna
condicoes = [
    (df[coluna_valores] > ticket_medio),
    (df[coluna_valores] < ticket_medio),
    (df[coluna_valores] == ticket_medio)
]

# Opções de classificação correspondentes às condições acima
opcoes = ['Acima da média', 'Abaixo da média', 'Igual à média']

# Criar a nova coluna no DataFrame aplicando as condições
df['comparacao_ticket'] = np.select(condicoes, opcoes, default='Não identificado')

# Exibir o DataFrame atualizado na tela para conferência
print("\nRelatório atualizado com a nova coluna:")
print(df.head())

# 4. Salvar o resultado em um novo arquivo CSV
df.to_csv('relatorio_vendas_atualizado.csv', index=False)
print("\nNovo arquivo 'relatorio_vendas_atualizado.csv' gerado com sucesso!")