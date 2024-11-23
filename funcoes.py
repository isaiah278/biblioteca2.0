# bibliotecas usadas para salvar os dados do usuario
import os
import json
# biblioteca usada para mostrar as datas de cadastro, atualizacao, emprestimo e devolucao
from datetime import datetime as data, timedelta as data_mais
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# limpar o terminal
def limpar_tela():
    return os.system('cls')
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
def menu():
    print('''
livros [1]
autores [2]
alunos [3]
empréstimos [4]
formatar sistema [5]
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
    caminho = "dados_usuario.json"
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
    caminho = "dados_usuario.json"
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
    limpar_tela()
    print('data de nascimento do autor no formato dia, mes e ano respectivamente: 00/00/0000 \nDigite o dia e dê ENTER')
    dia = input()
    limpar_tela()
    print('data de nascimento do autor no formato dia, mes e ano respectivamente: 00/00/0000 \nDigite o mês e dê ENTER')
    print(f'{dia}/', end='')
    mes = input()
    limpar_tela()
    print('data de nascimento do autor no formato dia, mes e ano respectivamente: 00/00/0000 \nDigite o ano e dê ENTER')
    print(f'{dia}/{mes}/', end='')
    ano = input()
    limpar_tela()
    dataNascimento = f'{dia}/{mes}/{ano}'
    dataCadastro = data.now().strftime('%d/%m/%Y')
    dataAtualizacao = dataCadastro
    
    # adicionando os dados digitados nas listas autores e livros e tambem atualizando o dicionario biblioteca
    dados['autores'].append({
        "id": ident,
        "nome": autor,
        "dataNascimento": dataNascimento
    })
    dados['livros'].append({
        "id": ident,
        "titulo": titulo,
        "autor": autor,
        "dataCadastro": dataCadastro,
        "dataAtualizacao": dataAtualizacao,
        "disponivel": True
    })                      
    dados['biblioteca']['livros'].append(titulo)
    dados['biblioteca']['autores'].append(autor)         
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
def del_livro():
    # verificando se algum livro ja foi adicionado
    # caso algum livro ja tenha sido adicionado
    if dados['livros'] != []:
        # verificando se o livro escolhido existe na biblioteca
        escolha = input('titulo: ') 
        # caso o livro esteja na biblioteca
        if escolha in dados['biblioteca']['livros']:
            # if
                # verificando se o livro não esta emprestado
                # se o livro nao estiver emprestado
                # removendo o livro da lista livros e do dicionario biblioteca
                [dados['livros'].remove(x) for x in dados['livros'] if x['titulo'] == escolha]
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
            [dados['autores'].remove(x) for x in dados['autores'] if x['nome'] == escolha] 
            dados['biblioteca']['autores'].remove(escolha)
        # caso o autor não esteja na biblioteca
        else:
            print('Esse autor não se encontra em nosso sistema')            
    # caso nenhum autor tenha sido adicionado
    else:
        print('Nenhum autor foi adicionado ao sistema ainda')
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
def listar_livros():
    if dados['livros'] != []:
        print('LIVROS')
        print('=-'*10)
        [print(x) for x in dados['biblioteca']['livros']]
        print('=-'*10)
    else:
        print('Nenhum livro adicionado')
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
def listar_autores():
    # se algum autor ja adicionado
    if dados['autores'] != []:
        print('AUTORES')
        print('=-'*10)
        [print(x) for x in dados['biblioteca']['autores']]
        print('=-'*10)
    # se senhum autor adicionado
    else:
        print('Nenhum autor adicionado')
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
def add_aluno():
    # colocando altomaticamente o id do aluno
    if dados['alunos'] == []:
        ident = 0
    else:
        ident = dados['alunos'].index(dados['alunos'][-1]) + 1
    nome = input('nome: ')
    limpar_tela()
    print('data de nascimento do aluno no formato dia, mes e ano respectivamente: 00/00/0000 \nDigite o dia e dê ENTER')
    dia = input()
    limpar_tela()
    print('data de nascimento do aluno no formato dia, mes e ano respectivamente: 00/00/0000 \nDigite o mês e dê ENTER')
    print(f'{dia}/', end='')
    mes = input()
    limpar_tela()
    print('data de nascimento do aluno no formato dia, mes e ano respectivamente: 00/00/0000 \nDigite o ano e dê ENTER')
    print(f'{dia}/{mes}/', end='')
    ano = input()
    dataNascimento = f'{dia}/{mes}/{ano}'
    limpar_tela()
    email = input('emai-l: ')
    # adicionando os dados do aluno na lista alunos
    dados['alunos'].append({
        'id': ident,
        'nome': nome,
        'dataNascimento': dataNascimento,
        'email': email,
        'emprestimos': []
    })
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
def del_aluno():
    #verificando se ja foi adicionado algum aluno ao sistema
    # se ja tiver algum aluno no sistema
    if dados['alunos'] != []:
        # verificando se o nome do aluno consta no sistema
        escolha = input('aluno(a): ')
        # se o aluno consta no sistema
        if escolha in [x['nome'] for x in dados['alunos']]:
            [dados['alunos'].remove(x) for x in dados['alunos'] if x['nome'] == escolha]
        # se o aluno nao consta no sistema
        else:
            print('O aluno não consta no sistema')
    # se nao tiver nenhum aluno no sistema
    else:
        print('Nenhum aluno no sistema')
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
def listar_alunos():
    # se algum aluno adicionado
    if dados['alunos'] != []:
        print('ALUNOS')
        print('=-'*10)
        [print(x['nome']) for x in dados['alunos']]
        print('=-'*10)
    # se nenhum aluno adicionado
    else:
        print('Nenhum aluno adicionado')
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
def fazer_emprestimo():
    # verificando se algum livro ja foi adicionado
    # se algum livro ja adicionado
    if dados['livros'] != []:
        # verificando se tem algum livro disponivel
        # se houver algum livro disponivel
        if True in [x['disponivel'] for x in dados['livros']]:
            # verificando se o aluno esta cadastrado
            # se o aluno estiver cadastrado
            aluno = input('Aluno(a): ')
            if aluno in [x['nome'] for x in dados['alunos']]:
                # mostrando os livros disponiveis
                print('LIVROS DISPONIVEIS')
                print('=-'*10)
                [print(x['titulo']) for x in dados['livros'] if x['disponivel'] == True]
                print('=-'*10)
                # verificando se o livro escolhido esta disponivel
                escolha = input('titulo: ')
                # se o livro estiver disponivel
                if escolha in [x['titulo'] for x in dados['livros'] if x['disponivel'] == True]:
                    # adicionando o livro aos emprestimos do aluno
                    [x['emprestimos'].append(escolha) for x in dados['alunos'] if x['nome'] == aluno]
                    # adicionando o emprestimo a biblioteca
                    dados['biblioteca']['emprestimos'].append(escolha)
                    # atualizando o estado de disponivel do livro para False
                    [x.update({'disponivel': False}) for x in dados['livros'] if x['titulo'] == escolha]
                    # data de devolucao
                    data_emprestimo = data.now().strftime('%d/%m/%Y')
                    data_devolucao = (data_mais(days=7)+data.now()).strftime('%d/%m/%Y')
                    print(f'Livro: "{escolha}" emprestado com sucesso')
                    print(f'Data de emprestimo: {data_emprestimo}')
                    print(f'Data de devolução: {data_devolucao}')
                # se o livro nao estiver disponivel
                else:
                    print('livro indisponivel')
            # se o aluno nao estiver cadastrado        
            else:
                print('Aluno não cadastrado')
        # se nao houver livro disponivel
        else:
            print('Nenhum livro esta disponivel para emprestimo')
    # se nenhum livro foi adicionado
    else:
        print('Nenhum livro adicionado')      
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
def devolver_livro():
    # verificar se algum livro ja foi adicionado
    # se algum livro ja foi adicionado
    if dados['livros'] != []:
        # verificar se algum empréstimo ja foi feito
        # se algum emprestimo ja foi feito
        if dados['biblioteca']['emprestimos'] != []:
            # verificar se o aluno ja foi cadastrado
            aluno = input('Aluno(a): ')
            # se o aluno ja foi cadastrado
            if aluno in [x['nome'] for x in dados['alunos']]:
                # verificar se o aluno tem algum empréstimo
                # se o aluno tiver algum emprestimo
                if aluno in [x['nome'] for x in dados['alunos'] if x['emprestimos'] != []]:
                    # mostrando os livros emprestados pro aluno
                    lista_alunos = []
                    print(f'Emprestimos de {aluno}')
                    print('=-'*10)
                    [[print(y) for y in x['emprestimos']] for x in dados['alunos'] if x['nome'] == aluno]
                    [[lista_alunos.append(y) for y in x['emprestimos']] for x in dados['alunos'] if x['nome'] == aluno]
                    print('=-'*10)
                    # verificar se o livro escolhido esta nos empréstimos do aluno
                    escolha = input('')
                    # se o livro escolhido estiver nos emprestimos do aluno
                    if escolha in lista_alunos:
                        # mudar a situação de disponível do livro para True
                        [x.update({'disponivel': True}) for x in dados['livros'] if x['titulo'] == escolha]
                        # retirar o livro dos empréstimos da biblioteca
                        dados['biblioteca']['emprestimos'].remove(escolha)
                        # retirar o livro dos empréstimos do aluno
                        [x['emprestimos'].remove(escolha) for x in dados['alunos'] if x['nome'] == aluno]
                        # atualizando a data de atualizacao do livro
                        data_atualizacao = data.now()
                        [x.update({'dataAtualizacao': data_atualizacao}) for x in dados['livros'] if x['titulo'] == escolha] 
                    # se o livro escolhido não estiver nos emprestimos do aluno
                    else:
                        print('Este livro nao foi emprestado para o aluno')
                # se o aluno nao tiver nenhum emprestimo
                else:
                    print('O aluno ainda não fez nenhum emprestimo')
            # se o aluno nao esta cadastrado
            else:
                print('O aluno não foi cadastrado')
        # se nenhum emprestimo foi feito
        else:
            print('Nenhum emprestimo foi feito ainda')
    # se nenhum livro foi adicionado
    else:
        print('Nenhum livro foi adicionado')
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
                
       