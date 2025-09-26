""" tasks = []

tasks.append('Estudar Python com IA.')
tasks.append('Ler um artigo sobre IA.')
tasks.append('Responder E-mails')

print('=========================== MINHAS TAREFAS ===========================')

for i in tasks: 
  print(f'Tarefa: {i}') """

student = {
  'name': input('Nome do aluno: '),
  'age': int(input('Idade do aluno: ')),
  'grade': input('Nota do aluno: ')
}

print(f"{student['name']} tem {student['age']} anos e tirou nota {student['grade']}.")
