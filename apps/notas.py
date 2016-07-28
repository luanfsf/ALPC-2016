#!/usr/bin/env python
alunos = 0
aprovados = 0
reprovados = 0
exame = 0
mediatotal = 0
while alunos < 6:
  alunos = alunos + 1
  print "Aluno:", alunos
  print ("Digite duas notas de seis alunos alunos")
  nota = int(input())
  notanota = int(input())
  media = float(nota + notanota ) / 2
  mediatotal = mediatotal + media 
  print ("A media e"), media
  if media <= 3: # or media >3 and media <=7
    print "Reprovado"
    reprovados = reprovados + 1
  else:
    if media > 3 and media <= 7:
      print "Exame"
      exame = exame +1
    else:
      if media >7 and media <= 10:
        print "Aprovado"
        aprovados = aprovados + 1
print ("Total de alunos reprovados ="), reprovados
print ("Total de alunos em exame ="), exame
print ("Total de alunos aprovados ="), aprovados
print ("A media da turma e"), mediatotal /6

print (":)")