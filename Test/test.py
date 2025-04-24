import unittest
from unittest.mock import patch
from io import StringIO
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