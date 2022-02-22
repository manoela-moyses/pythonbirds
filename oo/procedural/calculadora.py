def calcular():
    #Pegar inputs do usuário
    operandos=[]
    operandos.append(float(input('Digite o primeiro operando: ')))
    sinal = input('Digite o sinal da operação: ')
    operandos.append(float(input('Digite o segundo operando: ')))
    return executar_calculo(sinal, operandos)


def executar_calculo(sinal, operandos):
    #Executar operação
    if sinal == '+':
        resultado = operandos[0] + operandos[1]
    elif sinal == '-':
        resultado = operandos[0] - operandos[1]
    else:
        raise OperacaoNaoEncontrada(f'Operação não encontrada para o sinal: {sinal}')

    # Retornar resultado

    return resultado


def calcular_prefixa():
    #Pegar inputs do usuário
    operandos = []
    sinal = input('Digite o sinal da operação: ')
    operandos.append(float(input('Digite o primeiro operando: ')))
    operandos.append(float(input('Digite o segundo operando: ')))
    return executar_calculo(sinal, operandos)
