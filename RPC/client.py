import xmlrpc.client

with xmlrpc.client.ServerProxy('http://localhost:6000/') as proxy:
    n = int(input('digite o primeiro numero \n'))
    m = int(input('digite o segundo numero \n'))
    print(f'soma: de {n} + {m} = {proxy.soma(n,m)}')
    print(f'subtração: de {n} - {m} = {proxy.subtracao(n,m)}')
    print(f'multiplicação: de {n} * {m} = {proxy.multiplicacao(n,m)}')
    print(f'divisão: de {n} / {m} = {proxy.divisao(n,m)}')
    