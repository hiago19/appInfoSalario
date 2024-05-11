class Funcionario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        self.horas = {}
        self.salario_hora = {}

    def cadastro_hora(self, mes, horas):
        if mes not in self.horas:
            self.horas[mes] = horas

    def cadastro_salario_hora(self, mes, valor):
        if mes not in self.salario_hora:
            self.salario_hora[mes] = valor

    def calcula_salario(self, mes):
        if (mes not in self.horas) or (mes not in self.salario_hora):
            print('Mês Inexistente!!')
        else:
            return f"R$ {self.horas[mes] * self.salario_hora[mes]}"

    def __repr__(self):
        return f'O funcionário {self.nome}({self.email}), com às horas/mês: {self.horas}, e salário-hora: {self.salario_hora}'
