login = input('Digite o seu login:')
senha = input('Digite a sua senha:')
if login == 'userpy' and senha == 'teste123':
    print('Bem-Vindo userpy01')
else:
    print('Login falhou')

# Se tivermos vários usuários
login = input('Digite o seu login:')
senha = input('Digite a sua senha:')
if login == 'userpy' and senha == 'teste123':
    print('Bem-Vindo userpy01')
elif login == 'userpy02' and senha == 'teste02':
    print('Bem-Vindo userpy02')
elif login == 'userpy03' and senha == 'teste03':
    print('Bem-Vindo userpy03')
else:
    print('Login falhou')