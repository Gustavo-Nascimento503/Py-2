class Aluno:
    def _init_(self, nome, idade, ra, curso):
        self.nome = nome
        self.idade = idade
        self.ra = ra
        self.curso = curso
    
    def _str_(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, RA: {self.ra}, Curso: {self.curso}"

class CadastroAlunos:
    def _init_(self):
        self.alunos = []
        
    def incluir_aluno(self):
        nome = input('Digite o nome do aluno: ')
        idade = int(input('Digite a idade do aluno: '))
        ra = input('Digite o RA do aluno: ')
        curso = input('Digite o curso do aluno: ')

        aluno = Aluno(nome, idade, ra, curso)
        self.alunos.append(aluno)
        print('Aluno cadastrado com sucesso!')

    def atualizar_aluno(self):
        ra = input('Digite o RA do aluno a ser atualizado: ')
        for aluno in self.alunos:
            if aluno.ra == ra:
                nome = input('Digite o novo nome do aluno: ')
                idade = int(input('Digite a nova idade do aluno: '))
                curso = input('Digite o novo curso do aluno: ')
                aluno.nome = nome
                aluno.idade = idade
                aluno.curso = curso
                print('Aluno atualizado com sucesso!')
                break
        else:
            print('Aluno não encontrado!')
    
    def excluir_aluno(self):
        ra = input('Digite o RA do aluno a ser excluído: ')
        for aluno in self.alunos:
            if aluno.ra == ra:
                self.alunos.remove(aluno)
                print('Aluno excluído com sucesso!')
                break
        else:
            print('Aluno não encontrado!')
    
    def exibir_alunos(self):
        for aluno in self.alunos:
            print(aluno)
    
    def exibir_menu(self):
        while True:
            print('1 - Incluir')
            print('2 - Atualizar')
            print('3 - Excluir')
            print('4 - Exibir')
            print('5 - Sair')

            opcao = int(input('Digite a opção escolhida: '))

            if opcao == 1:
                self.incluir_aluno()

            elif opcao == 2:
                self.atualizar_aluno()

            elif opcao == 3:
                self.excluir_aluno()

            elif opcao == 4:
                self.exibir_alunos()

            elif opcao == 5:
                break

            else:
                print('Opção inválida!')
