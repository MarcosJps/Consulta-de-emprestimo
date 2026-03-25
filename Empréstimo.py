import random

print('-=' * 30)

nome = input('Informe seu nome: ').strip().title()
nome1 = nome.split()[0]
salario = float(input('Informe seu salário: R$ '))
emp = float(input('Informe o valor do empréstimo: R$ '))
pagar = int(input('Em quanto tempo pretende pagar (anos): '))

protocolo = random.randint(100000, 999999)
meses = pagar * 12
prest = emp / meses
limite = salario * 0.30

print('-=' * 30)

print('\n----- DADOS DO CLIENTE -----')
print(f'Nome completo: {nome}')
print(f'Primeiro nome: {nome1}')
print(f'Salário Bruto: R$ {salario:.2f}')

print('\n----- DADOS DO EMPRÉSTIMO -----')
print(f'Valor do Empréstimo: R$ {emp:.2f}')
print(f'Prazo: {pagar} anos')
print(f'Prestação mensal: R$ {prest:.2f}')

print(f'\nNúmero do Protocolo: {protocolo}')

if prest <= limite:
    print('\033[1;32m✅ Empréstimo APROVADO!\033[m')
else:
    print('\033[1;31m❌ Empréstimo NEGADO!\033[m')