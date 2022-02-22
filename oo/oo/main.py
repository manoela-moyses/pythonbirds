from calculadora import Calculadora, Operacao

def produto(operandos):
    return operandos[0] * operandos[1]

class CalculadoraPrefixa(Calculadora):
    def extrair_inputs(self):
        operandos = []
        sinal = input('Digite o sinal da operação: ')
        operandos.append(float(input('Digite o primeiro operando: ')))
        operandos.append(float(input('Digite o segundo operando: ')))
        return operandos, sinal


if __name__ == '__main__':
    calculadora = CalculadoraPrefixa()
    calculadora.adicionar_operacao('*', produto)
    print(calculadora.calcular())
    print(calculadora.calcular())