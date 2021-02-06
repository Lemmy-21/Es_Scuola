import os

data = input("per che data bisogna consegnare l'esercizio?(dividi con dei punti)\
   es/ 04. 02 \n").split('. ')

for i in range(len(data)):
   cifre = str(data[i]).split()
   
   if '0' not in cifre and int(data[i]) < 10:
      cifre.insert(0, '0')
      i2 = str(cifre[0]) + str(cifre[1])
      data[i] = i2

num_pag_es = input("quali sono numero e pagina dell'esercizio?(dividi con dei punti)\
   es/ 17. 189 \n").split('. ')
consegna_es = input("scrivi la consegna dell'esercizio\n")

id_dir = int(open('cronolog_es.txt', 'r').read())
id_dir += 1
riscrittura = open('cronolog_es.txt', 'w')
riscrittura.write(str(id_dir))
riscrittura.close()

cwd = os.getcwd()
id_es = num_pag_es[0] + 'p' + num_pag_es[1] + '.py'
cartella = cwd + "\\" + str(id_dir) + '.' + '[ ' + data[0] + ' - ' + data[1] + ' ]'
testo_es = "'''\n\n" + "[ es " + num_pag_es[0] + ' - pag ' + \
num_pag_es[1] + ' ]\n' + consegna_es + "\n\n'''"

os.makedirs(cartella)
os.chdir(cartella)
file_es = open(id_es, 'w')
file_es.write(testo_es)
file_es.close