
#Exemplos de print:

print(f'Meu nome é {nome} e tenho {idade} anos.')
print('Meu cachorro se chama {}'.format('chico'))

print('A','L','U','R','A',sep='\n')
# Criação das Variáveis
nome = 'Lais'
idade = 24

# Abordagem mais simples
print('Meu nome é',nome,'e tenho',idade,'anos.')

# Abordagem do f-string
print(f'Meu nome é {nome} e tenho {idade} anos.')

# Abordagem do .format()
print('Meu nome é {} e tenho {} anos.'.format(nome,idade))

# Abordagem da % (Formatação de String Antiga - Python 2)
print('Meu nome é %s e tenho %i anos.'%(nome,idade))


# Criando funções:

def cadastrar_restaurante():
    print('Cadastrar restaurante')
