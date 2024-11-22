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
    caminho = "biblioteca2.0\dados_usuario.json"
    if os.path.exists(caminho):    
        with open(caminho, "r") as arquivo2:
            return json.load(arquivo2)
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
    caminho = "biblioteca2.0\dados_usuario.json"
    with open(caminho, "w") as arquivo:
        json.dump(dados, arquivo, indent=4)
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
def add_livro():
    # colocando o id altomaricamente
    if dados['livros'] == []:
        ident = 0
    else:
        ident = dados['livros'].index(dados['livros'][-1]) + 1
    titulo = input('titulo: ')
    autor = input('autor: ')
    dataNascimento = input('data de nascimento: ') 
    
    # adicionando os dados digitados nas listas autores e livros e tambem atualizando o dicionario biblioteca
    dados['autores'].append({
        "id": ident,
        "nome": autor,
        "dataNascimento": dataNascimento
    })
    dados['livros'].append({
        "id": ident,
        "titulo": titulo,
        "autor": autor
    })                      
    dados['biblioteca']['livros'].append(titulo)
    dados['biblioteca']['autores'].append(autor)         
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
def del_livro():
    # verificando se algum livro ja foi adicionado
    # caso algum livro ja tenha sido adicionado
    if dados['livros'] != []:
        escolha = input('titulo: ')
        # verificando se o livro escolhido existe na biblioteca
        # caso o livro esteja na biblioteca
        if escolha in dados['biblioteca']['livros']:
            # removendo o livro da lista livros e do dicionario biblioteca
            for x in dados['livros']:
                if x['titulo'] == escolha:
                    dados['livros'].remove(x)
                    dados['biblioteca']['livros'].remove(escolha)
        # caso o livro não esteja na biblioteca
        else:
            print('Esse livro não se encontra em nosso sistema')            
    # caso nenhum livro tenha sido adicionado
    else:
        print('Nenhum livro foi adicionado ao sistema ainda')
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
def del_autor():
    # verificando se algum autor ja foi adicionado
    # caso algum autor ja tenha sido adicionado
    if dados['autores'] != []:
        escolha = input('autor: ')
        # verificando se o autor escolhido existe na biblioteca
        # caso o autor esteja na biblioteca
        if escolha in dados['biblioteca']['autores']:
            # removendo o autor da lista autores e da biblioteca
            for x in dados['autores']:
                if x['nome'] == escolha:
                    dados['autores'].remove(x)
                    dados['biblioteca']['autores'].remove(escolha)
        # caso o autor não esteja na biblioteca
        else:
            print('Esse autor não se encontra em nosso sistema')            
    # caso nenhum autor tenha sido adicionado
    else:
        print('Nenhum autor foi adicionado ao sistema ainda')
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
def listar_livros():
    print('LIVROS')
    print('=-'*10)
    for x in dados['biblioteca']['livros']:
        print(x)
    print('=-'*10)
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
def listar_autores():
    print('AUTORES')
    print('=-'*10)
    for x in dados['biblioteca']['autores']:
        print(x)
    print('=-'*10)
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
def add_aluno():
    if dados['alunos'] == []:
        ident = 0
    else:
        ident = dados['alunos'].index(dados['alunos'][-1]) + 1
    nome = input('nome: ')
    dataNascimento = input('data de nascimento: ')
    email = input('emai-l: ')
    dados['alunos'].append({
        'id': ident,
        'nome': nome,
        'dataNascimento': dataNascimento,
        'email': email
    })
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
def del_aluno():
    if dados['alunos'] != []:
        pass
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
def zerar_tudo():
    dados['livros'] = []
    dados['autores'] = []
    dados['alunos'] = []
    dados['biblioteca'] = {
        "livros": [],
        "autores": [],
        "emprestimos": []
    }
                
       