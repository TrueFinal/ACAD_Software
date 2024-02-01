# Inicio: 29/01/2024
# Atualizacao: 31/01/2024
# Versao: 1.3

""" HISTÓRICO DE VERSÃO

1.0     a) Implementação dos métodos duplicados(), cad_aluno(),
		   cad_professor() e cad_disciplina();
		b) União dos métodos ao método menu().
----------------------------
1.1     a) Correção e adaptação do método cad_professor();
		b) Adequação da classe menu();
		c) Adequação das mensagens de saida.
----------------------------
1.2     a) Correção do parâmetro lista enviada para o método duplicados() no
		   método cad_professor(), que antes estava enviando DISCIPLINAS e
		   cod_disciplina no lugar de PROFESSORES e pro_matricula;
----------------------------
1.3     a) Implantação parcial dos métodos cad_turmas() e cad_notas().
		b) Implantação dos métodos procurar_valor(), imprimir_lista(), salvar() e relatório().
		c) Implantação da rotina para salvar as informações em um arquivo csv.
1.3b    a) Correção do método duplicados(), procurar_valores() e imprimir_lista().
		b) Correção de erro do método cad_turma() que não verificava os valores ímpares.
		c) Adequação do método imprimir_lista() para realizar a impressão da tabela TURMAS
		d) Implantação parcial do método cad_frequencia()
"""
import csv
import os
from time import sleep
import re



PROFESSORES=list()
ALUNOS=list()
DISCIPLINAS=list()
TURMAS=list()
NOTAS=list()
FREQUENCIAS=list()



nome_arquivo = 'arquivo.csv'
try:
	with open(nome_arquivo, newline='') as arquivo:
		dados=list()
		leitura = csv.reader(arquivo, delimiter=';')
		
		for i in leitura:
			dados.append(i)
			
		arquivo.close()
		
		PROFESSORES = dados[0]
		ALUNOS = dados[1]
		DISCIPLINAS = dados[2]
		TURMAS = dados[3]
	
except FileNotFoundError:
	arquivo = open(nome_arquivo, 'w+')
	arquivo.close()
		
	



def duplicados(lista, valor, tipo):
	if len(lista) == 0:
		return False
	else:
		if tipo == 0:
			for i in range(len(lista)):
				if i % 2 == 0:
					if int(lista[i]) == valor:
						return True
		if tipo == 1:
			for i in range(0, len(lista), 6):
				if int(lista[i]) == valor:
					return True

		if tipo == 2:
			for i in range(len(lista)):
				if int(lista[i]) == valor:
					return True
 
		return False



def procurar_valor(lista, valor, tipo):
	if duplicados(lista, valor, tipo) == True:
		if tipo == 0:
			for i in range(0, len(lista), 2):
				if i % 2 == 0:
					if int(lista[i]) == valor:
						return i
		if tipo == 1:
			for i in range(0, len(lista), 6):
				if lista[i] == valor:
					return i

		if tipo == 2:
			for i in range(len(lista)):
				if lista[i] == valor:
					return i

	return 0



def imprimir_lista(lista, tipo):
	if tipo == 0:
		aux_a = list()
		aux_b = list()
		for i in range(len(lista)):
			if i % 2 == 0:
				aux_a.append(lista[i])
			else:
				aux_b.append(lista[i])

		print("+","-" * 52)

		for i in range(len(aux_a)):
			print(" | %s\t\t| %s" %(aux_a[i], aux_b[i]))

		print("+","-" * 52)
		
	if tipo == 1:
		aux_a = list()
		aux_b = list()
		aux_c = list()
		aux_d = list()
		aux_e = list()
		aux_f = list()
		for i in range(0, len(lista), 6):
			aux_a.append(lista[i]) # Armazena o código da turma
			aux_b.append(lista[i+1]) # Armazena o máximo de aula
			aux_c.append(lista[i+2]) # Armazena o mínimo de aula
			aux_d.append(lista[i+3]) # Armazena o código da disciplina
			aux_e.append(lista[i+4]) # Armazena a matrícula do professor
			aux_f.append(re.sub('[\]\[ ]', '', lista[i+5])) # Armazena as matrículas dos alunos
		print("valor: ")
		for i in range(len(aux_a)):
			print("+","-" * 52)
			print("Código da Turma: %s" %aux_a[i])
			print("Número de Aulas: %s" %aux_b[i])
			print("Frequência Mínima: %s" %aux_c[i])
			print("Disciplina: %s." %DISCIPLINAS[procurar_valor(DISCIPLINAS, aux_d[i], 0)+1])
			print("Professor(a): %s." %PROFESSORES[procurar_valor(PROFESSORES, aux_e[i], 0)+1])
			print("+","-" * 52)
			print("Alunos Matriculados")
			print("+","-" * 52)
			temp = aux_f[i].split(',')
			for j in range(len(temp)):
				print("%s\t\t%s" %(ALUNOS[procurar_valor(ALUNOS, int(temp[j]), 0)],ALUNOS[procurar_valor(ALUNOS, int(temp[j]), 0)+1]))
			print("+","-" * 52)
			print("")
			print("")
	print("")



def salvar():
	with open('arquivo.csv', 'w', newline='\n') as arquivo:
		leitura = csv.writer(arquivo, delimiter=';')
		
		if len(PROFESSORES) != 0:
			leitura.writerow(PROFESSORES)
			
		if len(ALUNOS) != 0:
			leitura.writerow(ALUNOS)
			
		if len(DISCIPLINAS) != 0:
			leitura.writerow(DISCIPLINAS)
			
		if len(TURMAS) != 0:
			leitura.writerow(TURMAS)
			
		arquivo.close()


	
def cad_aluno():
	print("CADASTRO DE ALUNO")
	print("Informe os dados abaixo ou digite 0 (zero) voltar ao menu inicial.\n")
	while True:
		alu_mat = int(input("Digite a matrícula do Aluno: "))
		if alu_mat == 0:
			print("Voltando ao menu inicial...")
			break
		if duplicados(ALUNOS, alu_mat, 0) == False:
			alu_nome = input("Digite o nome do Aluno: ")
			print("")
			ALUNOS.append(alu_mat)
			ALUNOS.append(alu_nome)
		else:
			print("Código já existe!")
			print("")
	salvar()



def cad_professor():
	print("CADASTRO DE PROFESSOR")
	print("Informe os dados abaixo ou digite 0 (zero) voltar ao menu inicial.\n")
	while True:
		pro_matricula = int(input("Digite a matrícula do Professor: "))
		if pro_matricula == 0:
			print("Voltando ao menu inicial...")
			break
		if duplicados(PROFESSORES, pro_matricula, 0) == False:
			pro_nome = input("Digite o nome do Professor: ")
			PROFESSORES.append(pro_matricula)
			PROFESSORES.append(pro_nome)
			print("")
		else:
			print("O código informado já foi cadastrado!")
			print("")
	salvar()
		


def cad_disciplina():
	print("CADASTRO DE DISCIPLINA")
	print("Informe os dados abaixo ou digite 0 (zero) voltar ao menu inicial.\n")
	while True:
		dis_codigo = int(input("Digite o codigo da Disciplina: "))
		if dis_codigo == 0:
			print("Voltando ao menu inicial...")
			break
		if duplicados(DISCIPLINAS, dis_codigo, 0) == False:
			dis_nome = input("Digite o nome da Disciplina: ")
			DISCIPLINAS.append(dis_codigo)
			DISCIPLINAS.append(dis_nome)
			print("")
		else:
			print("O código informado já foi cadastrado!")
			print("")
	salvar()
		  


def cad_turmas():  
	print("CADASTRO DE TURMA")
	print("Informe os dados abaixo ou digite 0 (zero) voltar ao menu inicial.\n")
	while True:
		while True:
			tur_codigo = int(input("Digite o codigo da Turma: "))
			if tur_codigo == 0:
				print("Voltando ao menu inicial...")
				salvar()
				return
			if duplicados(TURMAS, tur_codigo, 1) == False:
				TURMAS.append(tur_codigo)
				break
			else:
				print("O código informado já foi cadastrado!")
				print("")

		tur_aulas = int(input("Digite o total de aulas: "))
		TURMAS.append(tur_aulas)
		
		tur_minimo = int(input("Digite o mínimo de aulas: "))
		TURMAS.append(tur_minimo)
		sleep(1)
		
		print("\n Disciplinas Disponíveis")
		imprimir_lista(DISCIPLINAS, 0)
		
		while True:
			dis_codigo = int(input("Digite o codigo da Disciplina: "))
			if duplicados(DISCIPLINAS, dis_codigo, 0) == True:
				print("Disciplina %s adicionada na turma!\n" %DISCIPLINAS[procurar_valor(DISCIPLINAS, dis_codigo, 0)+1])
				TURMAS.append(dis_codigo)
				break
			else:
				print("O código da Disciplina não foi encontrado!\n")
		sleep(1)
		
		print("\n Professores Cadastrados")
		imprimir_lista(PROFESSORES, 0)
		
		while True:
			pro_matricula = int(input("Digite a matrícula do Professor: "))
			if duplicados(PROFESSORES, pro_matricula, 0) == True:
				print("Professor %s adicionado(a) na turma!" %PROFESSORES[procurar_valor(PROFESSORES, pro_matricula, 0)+1])
				TURMAS.append(pro_matricula)
				break
			else:
				print("A matrícula do Professor não foi encontrada!")
		sleep(1)
		
		print("\n--------\nCadastro de Alunos na Turma %i." %tur_codigo)
		print("Informe a matrícula 0 (zero) para finalizar o cadastro dos alunos na Turma %i.\n--------" %tur_codigo)
		
		print("\n Alunos Cadastrados")
		imprimir_lista(ALUNOS, 0)
		
		tur_aux=list() 
		while True:
			alu_mat = int(input("===| Digite a matrícula do Aluno: "))
			if alu_mat == 0:
				print("Cadastro de alunos na Turma %i finalizado!" %tur_codigo)
				print("")
				break
			if duplicados(ALUNOS, alu_mat, 0) == True:
				if duplicados(tur_aux, alu_mat, 2) == False:
					print("%s adicionado(a) na turma!" %ALUNOS[procurar_valor(ALUNOS, alu_mat, 0)+1])
					tur_aux.append(alu_mat)
				else:
					print("%s já se encontra na turma!" %ALUNOS[procurar_valor(ALUNOS, alu_mat, 0)+1])
			else:
				print("Matrícula não encontrada!")
				print("")
		TURMAS.append(tur_aux)
	salvar()


"""
def cad_notas():
	print("CADASTRO DE NOTAS")
	print("Informe os dados abaixo ou digite 0 (zero) voltar ao menu inicial.\n")
	while True:
		aux=[]
		tur_codigo = int(input("Informe o codigo da turma: "))
		if duplicados(TURMAS, tur_codigo, 1) == False:
			NOTAS.append(tur_codigo)
			for i in range(len(TURMAS[LOCAL+5])):
				turma_atual = TURMAS[LOCAL+5] 
				duplicados(ALUNOS, turma_atual[i], 0)
				print("Matrícula: %i\t\t Nome: %s\n" %(turma_atual[i], ALUNOS[LOCAL+1]))
		nota1 = float(input("Informe a primeira nota: "))
		if nota1 < 0 or  nota1 > 100:
			print(" A nota deve estar entre zero e 100.")
			break
		nota2 = float(input("Informe a segunda nota: "))
		if nota2 < 0 or  nota2 > 100:
			print(" A nota deve estar entre zero e 100.")
			break
							 
					#TURMAS.append(tur_codigo,alu_matricula)
					#notamedia = (nota1 + nota2 ) / 2
					#print("A media das notas informadas é ",notamedia)
			print("")
			aux.append([turma_atual[i], nota1, nota2])
			print("-----------------------------------")
			NOTAS.append(aux)
"""
def cad_notas():
    print("CADASTRO DE NOTA")
    print("Informe os dados abaixo ou digite 0 (zero) para voltar ao menu inicial.\n")

    while True:
        alu_not = input("Digite nota do Aluno: ")

        if alu_not == 0:
            print("Voltando ao menu inicial...")
            break
        
        if duplicados(NOTAS, alu_not) == False:
            NOTAS.append(alu_not)

        else:
            print("Código já existe!")
            print("")

        
def cad_frequencia():
    print("CADASTRO DE FREQUÊNCIA")
    print("Informe os dados abaixo ou digite 0 (zero) para voltar ao menu inicial.\n")

    while True:
        alu_fre = input("Digite a frequência do Aluno: ")

        if alu_fre == 0:
            print("Voltando ao menu inicial...")
            break
        
        if duplicados(FREQUENCIAS, alu_fre) == False:
            FREQUENCIAS.append(alu_fre)

        else:
            print("Código já existe!")
            print("")

        print(FREQUENCIAS)
        print("")

def relatorio():
	if len(DISCIPLINAS) == 0:
		print("Não há Disciplinas cadastradas no Banco de Dados")
	else:
		print("\nDisciplinas Disponíveis")
		imprimir_lista(DISCIPLINAS, 0)

	if len(ALUNOS) == 0:
		print("Não há Alunos cadastradas no Banco de Dados")
	else:
		print("\nAlunos Cadastrados")
		imprimir_lista(ALUNOS, 0)

	if len(PROFESSORES) == 0:
		print("Não há Professores cadastrados no Banco de Dados")
	else:
		print("\nProfessores Cadastrados")
		imprimir_lista(PROFESSORES, 0)

	if len(TURMAS) == 0:
		print("Não há Turmas cadastradas no Banco de Dados")
	else:
		print("\nTurmas Cadastradas")
		imprimir_lista(TURMAS, 1)
	print("")
	os.system("pause")



def menu():
	while True:
		os.system('cls')
		print("===================================")
		print("            ==| ACAD |==           ")
		print("   Sistema de Cadastro Acadêmico   ")
		print("===================================")
		print("""\t [1] - ALUNO
\t [2] - PROFESSOR
\t [3] - DISCIPLINA
-----------------------------------
\t [4] - TURMAS
-----------------------------------
\t [5] - NOTAS
\t [6] - FREQUENCIAS
-----------------------------------
\t [7] - RELATÓRIO
-----------------------------------
\t [0] - Sair""")
		print("")
		opcao = int(input("Digite a opção desejada: "))

		if opcao == 1:
			print("\n")
			print("=" * 35)
			os.system('cls')
			cad_aluno()
		elif opcao == 2:
			print("\n")
			print("=" * 35)
			os.system('cls')
			cad_professor()
		elif opcao == 3:
			print("\n")
			print("=" * 35)
			os.system('cls')
			cad_disciplina()
		elif opcao == 4:
			print("\n")
			print("=" * 35)
			os.system('cls')
			cad_turmas()
		elif opcao == 5:
			print("\n")
			print("=" * 35)
			os.system('cls')
			cad_notas()
		elif opcao == 6:
			print("\n")
			print("=" * 35)
			os.system('cls')
			cad_notas()
		elif opcao == 7:
			print("\n")
			print("=" * 35)
			os.system('cls')
			relatorio()
			
		elif opcao == 0:
			print("\nSistema finalizado!")
			break
		else:
			print("Codigo invalido!")
		print("\n\n")

		sleep(2)


menu()

	
