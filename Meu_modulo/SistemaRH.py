def logar_acao(func):
    def wrapper(*args, **kwargs):
        print("Exibindo bônus do funcionário.")
        return func(*args, **kwargs)
    return wrapper

class SistemaRH:
    def __init__(self):
        self.funcionarios = []

    @logar_acao
    def mostrar_bonus(self, funcionario):
        print(f"Funcionário: {funcionario.get_nome()}, Bônus: {funcionario.calcular_bonus()}")

    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)

    def listar_bonuses(self):
        for funcionario in self.funcionarios:
            self.mostrar_bonus(funcionario)