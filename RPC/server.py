from xmlrpc.server import SimpleXMLRPCServer

def soma(n,m):
    print(f'Requisição de soma: {n, m}')
    return n + m

def subtracao(n,m):
    print(f'Requisição de subtração: {n, m}')
    return n - m

def multiplicacao(n,m):
    print(f'Requisição de multiplicação: {n, m}')
    return n * m

def divisao(n,m):
    print(f'Requisição de soma: {n, m}')
    if m > 0:
        return n / m
    return 'invalido'



server = SimpleXMLRPCServer(('localhost', 6000))
print('Listening on port 6000...')

server.register_function(soma, 'soma')
server.register_function(subtracao, 'subtracao')
server.register_function(multiplicacao, 'multiplicacao')
server.register_function(divisao, 'divisao')

server.serve_forever()