notas = {}
note_finished = False

def find_highest_notader(note_record):
  highest_nota = 0
  aluno = ""
  # note_record = {"Vinicius": 10, "Maria": 8...}
  for alunos in note_record:
    note_value = note_record[alunos]
    if note_value > highest_nota: 
      highest_nota = note_value
      aluno = alunos
  print(f"{aluno} com a nota {highest_nota}, foi o aluno com a maior nota")

while not note_finished:
  name = input("Qual o nome do aluno?: ")
  nota = float(input("Qual foi a nota tirada?: "))
  notas[name] = nota
  should_continue = input("Você irá acrescentar mais uma nota de aluno? Type 'yes or 'no'.\n")
  if should_continue == "no":
    note_finished = True
    find_highest_notader(notas)

