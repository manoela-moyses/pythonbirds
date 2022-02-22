from abc import ABC, abstractmethod


class OperacaoNaoEncontrada(Exception):
    pass


# Para criar novas operações, crie uma classe herdando de Operacao, sobrescreva o método __call__ recebendo um parâmetro e retornando o resultado da operação.
# Depois instancie uma calculadora e use o método adicionar_operacao para adicionar a operação.


class Operacao(ABC):
    """
    Classe base para todas as operações. Método __call__ precisa ser sobrescrito.
    """
    @abstractmethod
    def __call__(self, operandos):
        raise NotImplementedError()
        """
        Método deve executar operação e retornar resultado
        """


class Soma:
    def __call__(self, operandos):
        return operandos[0] + operandos[1]


class Subtracao:
    def __call__(self, operandos):
        return operandos[0] - operandos[1]

# Para alterar a obtenção de inputs, herde de Calculadora e sobrescreva o método extrair_inputs

class Calculadora:
    """
    Classe responsável por conter operações, obter inputs e efetuar cálculo
    """

    def __init__(self):
        self.operacoes = {}
        self.adicionar_operacao('+', Soma())
        self.adicionar_operacao('-', Subtracao())

    def adicionar_operacao(self, sinal, operacao):
        self.operacoes[sinal] = operacao

    def calcular(self):
        operandos, sinal = self.extrair_inputs()
        try:
            operacao = self.operacoes[sinal]
            resultado = operacao(operandos)
        except KeyError as e:
            raise OperacaoNaoEncontrada(f'Operação não encontrada para o sinal: {sinal}') from e
        return resultado

    def extrair_inputs(self):
        operandos = []
        operandos.append(float(input('Digite o primeiro operando: ')))
        sinal = input('Digite o sinal da operação: ')
        operandos.append(float(input('Digite o segundo operando: ')))
        return operandos, sinal
