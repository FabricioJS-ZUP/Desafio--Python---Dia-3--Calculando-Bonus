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
