# 🏦 Analisador de Crédito Automático

## 📝 Sobre o Projeto
Um projeto pessoal simples desenvolvido em Python para simular a aprovação (ou negação) de empréstimos bancários. O sistema avalia o salário do cliente e o valor da parcela, garantindo que a prestação não ultrapasse a regra de segurança de 30% da renda mensal. 

Projeto criado para colocar em prática os conhecimentos do **Módulo 1 de Python do Curso em Vídeo**.

## 🚀 Funcionalidades
* Recebe os dados do cliente e formata as letras do nome automaticamente.
* Gera um número de protocolo aleatório para a solicitação.
* Calcula o valor da prestação mensal com base no valor total do empréstimo e no tempo (em anos).
* Verifica se a prestação cabe no orçamento (regra dos 30% do salário).
* Exibe um relatório final formatado e com cores no terminal (Aprovado ✅ / Negado ❌).

## 💻 Conceitos Utilizados
* **Linguagem:** Python 3
* Manipulação de Strings (`.strip()`, `.title()`, `.split()`)
* Operadores Aritméticos
* Importação de Módulos (`import random`)
* Estruturas Condicionais (`if` / `else`)
* Formatação de saída com `f-strings` e cores ANSI.

## ⚙️ Como testar
1. Certifique-se de ter o Python instalado no seu computador.
2. Salve o código em um arquivo `.py` (exemplo: `analise_credito.py`).
3. Abra o terminal na pasta onde salvou o arquivo e rode o comando:
   ```bash
   python analise_credito.py
