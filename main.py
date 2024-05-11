from funcionario import Funcionario

nome = input("Informe o nome do Funcionario: ")
email = input("Agora, informe o email do Funcionario: ")

funcionario = Funcionario(nome, email)

mes = input("Informe o mês: ")
horas_trabalhadas = int(input(f"Informe as horas trabalhadas em {mes}: "))


salario_hora = float(input("Informe o salário por hora: "))

funcionario.cadastro_hora(mes, horas_trabalhadas)
funcionario.cadastro_salario_hora(mes, salario_hora)

print(funcionario)
print("Salário do mes:", funcionario.calcula_salario(mes))
