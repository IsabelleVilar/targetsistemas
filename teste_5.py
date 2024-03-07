def inverter_caracteres(string):
    nova_string = ''
    for i in range(len(string) -1, -1, -1):
        nova_string += string[i]
    return nova_string

entrada = input('Digite uma palavra: ')
nova_palavra = inverter_caracteres(entrada)
print(f'A palavra invertida é {nova_palavra}.')