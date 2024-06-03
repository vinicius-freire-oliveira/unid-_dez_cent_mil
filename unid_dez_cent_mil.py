numero = int(input('Digite um numero inteiro positivo: '))

# Extraindo a unidade
unidade = numero % 10

# Eliminando a unidade de nosso número
numero = (numero - unidade)/10

# Extraindo a dezena
dezena = numero % 10

# Eliminando a dezena do número original, fica a centena
numero = (numero - dezena)/10

# Extraindo a centena
centena = numero % 10

# Eliminando a centena do número original, fica o milhar
numero = (numero - centena)/10

# Extraindo o milhar
milhar = numero

# Fazendo ser inteiros
dezena = int(dezena)
centena = int(centena)
milhar = int(milhar)

print(milhar, 'milhar(es)', centena,'centena(s)', dezena,'dezena(s) e', unidade,'unidade(s)')