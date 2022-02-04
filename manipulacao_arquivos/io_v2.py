# Essa versão utiliza streaming, pois não precisa abrir o arquivo na memória
# Ideal para arquivos grandes
arquivo = open('pessoas.csv')
for registro in arquivo:
    print('Nome: {}, Idade: {}' .format(*registro.split(',')))
arquivo.close()
