def bitparabyte(value):
    print('valor para bit para byte')
    return float(value)

def bitParaByte(valorASerConvertido):
    print('Valor convertido de bit para byte')
    bytesCalculado = valorASerConvertido / 8
    return bytesCalculado

print('insira o valor')
entradaDoTecladoValorASerConvertido  = bitParaByte(int(input()))
valorConvertido = bitParaByte(entradaDoTecladoValorASerConvertido)
print(valorConvertido)