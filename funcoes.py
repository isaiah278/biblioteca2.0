import os
import json
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
def limpar_tela():
    return os.system('cls')
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
def menu():
    print('''
livros [1]
autores [2]
alunos [3]
empréstimos [4]
sair do sistema [0]
''')
    return int(input('escolha: '))
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
def menus(opcao):
    if opcao == 1:
        print('''
add_livro [1]
del_livr [2]
list_livros [3]
menu principal [4]
''')
        decisao = int(input('escolha: '))
        return decisao
    elif opcao == 2:
        print('''
del_autor [1]
list_autores [2]
menu principal [3]
''')
        decisao = int(input('escolha: '))
        return decisao
    elif opcao == 3:
        print('''
cadastrar_aluno [1]
remover_aluno [2]
listar alunos [3]
menu principal [4]
''')
        decisao = int(input('escolha: '))
        return decisao
    elif opcao == 4:
        print('''
fazer_empréstimo [1]
devolver_emprestimo [2]
menu principal [3]
''')
        decisao = int(input('escolha: '))
        return decisao
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# funcao puxar dados
def puxar_dados():
    # se o arquivo dados_usuario.json existir ele somente retorna os dados ja existentes no arquivo
    if os.path.exists('dados_usuario.json'):    
        with open("dados_usuario.json", "r") as arquivo:
            return json.load(arquivo)
    # se o arquivo não existir ele retorna as listas e o dicionario biblioteca
    else:
        return {
            "livros": [],
            "autores": [],
            "alunos": [],
            "biblioteca": {
                "livros": [],
                "autores": [],
                "emprestimos": []
            }
        }
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# adiocinando os dados ao dicionario dados
dados = puxar_dados()
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# funcao que salva todos os dados do dicionario dados dentro do arquivo dados_usuario.json
def escrever_dados():
    with open("dados_usuario", "w") as arquivo:
        json.dump(dados, arquivo)
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
def zerar_dados():
    dados = {}
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
def add_livro():
    