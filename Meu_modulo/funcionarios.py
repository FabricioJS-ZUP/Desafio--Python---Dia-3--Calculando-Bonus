from abc import ABC, abstractmethod
import unittest
from unittest.mock import patch
from io import StringIO

class Funcionario(ABC):
    def __init__(self, nome, salario):
        self.__nome = nome
        self.__salario = salario

    @abstractmethod
    def calcular_bonus(self):
        pass

    def get_nome(self):
        return self.__nome

    def get_salario(self):
        return self.__salario

    def set_salario(self, salario):
        if salario < 0:
            raise ValueError("O salário não pode ser negativo")
        self.__salario = salario

class FuncionarioComum(Funcionario):
    def calcular_bonus(self):
        return self.get_salario() * 0.10

class Gerente(Funcionario):
    def __init__(self, nome, salario, bonus_adicional):
        super().__init__(nome, salario)
        self.bonus_adicional = bonus_adicional

    def calcular_bonus(self):
        return self.get_salario() * 0.20 + self.bonus_adicional

def logar_acao(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"[LOG] Ação executada: {func.__name__} - Resultado: {result}")
        return result
    return wrapper

class SistemaRH:
    @logar_acao
    def mostrar_bonus(self, funcionario):
        bonus = funcionario.calcular_bonus()
        print(f"Funcionário: {funcionario.get_nome()}, Bônus: {bonus}")

# Etapa 4 – Testes automatizados
class TestSistemaRH(unittest.TestCase):
    def test_calculo_bonus_funcionario_comum(self):
        funcionario = FuncionarioComum("FC", 1000)
        self.assertEqual(funcionario.calcular_bonus(), 100)

    def test_calculo_bonus_gerente(self):
        gerente = Gerente("Ger", 2000, 500)
        self.assertEqual(gerente.calcular_bonus(), 900)

    def test_set_salario_negativo(self):
        funcionario = FuncionarioComum("FC", 1000)
        with self.assertRaises(ValueError):
            funcionario.set_salario(-100)

    @patch('sys.stdout', new_callable=StringIO)
    def test_mostrar_bonus(self, mock_stdout):
        sistema = SistemaRH()
        funcionario = FuncionarioComum("FC", 1000)
        sistema.mostrar_bonus(funcionario)
        self.assertIn("Funcionário: FC, Bônus: 100", mock_stdout.getvalue())

if __name__ == '__main__':
    unittest.main()