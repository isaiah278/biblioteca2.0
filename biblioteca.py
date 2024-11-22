from funcoes import menu, menus, escrever_dados, add_livro, del_livro, del_autor, listar_livros, listar_autores, zerar_tudo



while True:
    opcao1 = menu()
    # livros
    # adicionar livro [1]
    # remover livro [2]
    # listar livros [3]
    if opcao1 == 1:
        while True:
            opcao2 = menus(opcao1)
            if opcao2 == 1:
                add_livro()
                escrever_dados()
            elif opcao2 == 2:
                del_livro()
                escrever_dados()
            elif opcao2 == 3:
                listar_livros()
            else:
                break
    # autores
    # remover autor [1]
    # listar autores [2]
    elif opcao1 == 2:
        while True:
            opcao2 = menus(opcao1)
            if opcao2 == 1:
                del_autor()
                escrever_dados()
            elif opcao2 == 2:
                listar_autores()
            else:
                break
    # alunos
    # cadastrar aluno [1]
    # remover aluno [2]
    # listar alunos [3]
    elif opcao1 == 3:
        while True:
            opcao2 = menus(opcao1)
            if opcao2 == 1:
                pass
            elif opcao2 == 2:
                pass
            elif opcao2 == 3:
                pass
            else:
                break
    # emprestimos
    # fazer emprestimo [1]
    # devolver livro [2]
    elif opcao1 == 4:
        while True:
            opcao2 = menus(opcao1)
            if opcao2 == 1:
                pass
            elif opcao2 == 2:
                pass
            else:
                break
    elif opcao1 == 0:
        break
    
    else:
        zerar_tudo()
        escrever_dados()
  
        