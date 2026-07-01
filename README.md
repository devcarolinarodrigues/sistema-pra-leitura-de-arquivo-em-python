# sistema-pra-leitura-de-arquivo-em-python
# 📊 Análise de Dados: Cálculo e Classificação de Ticket Médio com Python

Este projeto consiste em um script de automação para análise descritiva de dados de vendas. O objetivo principal é processar o histórico de transações de uma lanchonete fictícia referente ao período de um mês, calcular o **Ticket Médio** e segmentar cada pedido individualmente com base nesse indicador.

A estratégia de gerar um novo arquivo foi adotada para preservar a integridade dos dados originais, permitindo uma análise mais aprofundada posteriormente sem alterar a base nativa.

---

## 🚀 Funcionalidades do Script

* **Leitura Estruturada:** Importação automatizada da base de dados tratando separadores de colunas e padrões de casas decimais.
* **Cálculo de Indicador:** Obtenção do Ticket Médio da operação de forma dinâmica.
* **Segmentação Inteligente:** Aplicação de regras condicionais vetorizadas para classificar as vendas.
* **Exportação Segura:** Geração de uma nova base de dados atualizada sem corromper o arquivo original.

---

## 📐 Metodologia e Cálculo Utilizado

O indicador financeiro central deste projeto é o **Ticket Médio**, mensurado a partir do cálculo da média aritmética simples dos valores de vendas. A análise foi aplicada sobre o histórico de transações de um período de 30 dias (um mês), permitindo identificar o comportamento de consumo e o valor médio gasto por pedido.

A fórmula matemática utilizada para a obtenção deste indicador é:

$$Ticket\ Médio = \frac{\text{Soma de todos os valores das vendas (R\$)}}{\text{Quantidade total de pedidos realizados}}$$

No código, essa operação é executada de maneira otimizada pela biblioteca Pandas através do método `.mean()`.

---

## 🔍 Passo a Passo do Código (`ticketmedio.py`)

A lógica de execução do script `ticketmedio.py` foi estruturada da seguinte forma:

1. **Leitura do Arquivo (Linha 5):** Realiza a leitura do arquivo `relatorio_vendas_lanchonete.csv`. O método `read_csv` especifica o ponto e vírgula como separador (`sep=';'`) e a vírgula para decimais (`decimal=','`), garantindo a correta interpretação dos dados numéricos pelo Python.
2. **Validação Inicial (Linhas 8 e 9):** Exibe as primeiras linhas do arquivo original (`df.head()`) para verificação visual da estrutura das colunas.
3. **Mapeamento (Linha 11):** Armazena o nome exato da coluna financeira (`'Valor total de itens'`) na variável `coluna_valores`.
4. **Processamento da Média (Linha 13):** Calcula a média aritmética de todos os valores da coluna mencionada e imprime o resultado formatado com duas casas decimais na tela.
5. **Configuração de Condições (Linhas 17 a 21):** Cria a lista `condicoes` para estabelecer os critérios de comparação (Maior, Menor ou Igual ao ticket médio).
6. **Definição de Etiquetas (Linha 24):** Cria a lista `opcoes` contendo os rótulos correspondentes: `'Acima da média'`, `'Abaixo da média'` e `'Igual à média'`.
7. **Aplicação da Lógica (Linha 27):** Cria a nova coluna `comparacao_ticket` utilizando a função `np.select()`, que mapeia as condições criadas de forma rápida e eficiente.
8. **Validação Final (Linhas 30 e 31):** Exibe o DataFrame atualizado na tela para conferência da nova coluna gerada.
9. **Exportação (Linhas 34 e 35):** Salva o resultado em um novo arquivo chamado `relatorio_vendas_atualizado.csv`, utilizando `index=False` para não poluir a tabela com índices numéricos.

---

## 🛠️ Ferramentas e Tecnologias Utilizadas

* **Linguagem:** [Python](https://www.python.org/) (Foco em manipulação e análise de dados)
* **IDE:** [Visual Studio Code (VS Code)](https://code.visualstudio.com/)
* **Bibliotecas:**
  * **Pandas:** Para estruturação de DataFrames, tratamento de arquivos CSV e cálculo estatístico.
  * **NumPy:** Para otimização de lógica condicional vetorizada através da função `np.select()`.

---

## 📁 Estrutura do Repositório

* `ticketmedio.py`: Script principal contendo o código fonte em Python.
* `relatorio_vendas_lanchonete.csv`: Base de dados original com o histórico de vendas.
* `relatorio_vendas_atualizado.csv`: Base de dados gerada pelo script contendo a nova coluna de classificação.

## ATENÇÂO: 
Todos os dados manipulados são ficticios. 
