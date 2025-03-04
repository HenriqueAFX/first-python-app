# Importa funcoes do sistema operacional.
import os

# =============== LISTAS ==========================================================

# Lista de restaurantes cadastrados, seguindo o tipo "Dicionario".
# Separa cada restaurante por nome, categoria e status de ativo e inativo.
# Executado em "listar_restaurantes()"
lista_restaurantes = [
    {'Nome':'Praca', 'Categoria':'Japonesa', 'Ativo':False},
    {'Nome':'Pizza Suprema', 'Categoria':'Pizza', 'Ativo':True},
    {'Nome':'Cantina', 'Categoria':'Italiana', 'Ativo':False}
]

# =================================================================================



# =============== BLOCOS/FUNCOES ==================================================

def limpeza_e_subtitulo(texto):
    os.system('cls')
    linha = '=' * len(texto)
    print(linha)
    print(texto)
    print(linha)
    print()

# Bloco/funcao que exibe o nome do programa.
# Executado em "main()".
def exibir_nome_programa():
    limpeza_e_subtitulo('SABOR EXPRESS')

# Bloco/funcao que exibe as opcoes do programa para o usuario escolher.
# Executado em "main()".
def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar/desativar restaurante')
    print('4. Sair\n')

def voltar_menu():
    input('\nPressione "Enter" para voltar ao menu principal. ')
    main()

# Bloco/funcao para a opcao 4, encerrando o app.
# Executado em "escolher_opcao()".
def finalizar_app():
    limpeza_e_subtitulo('Finalizando o app.')
    input('Pressione "Enter" para iniciar o app. ')
    main()

# Bloco/funcao para uma resposta de valor invalido.
# Executado em "escolher_opcao()".
def opcao_invalida():
    print('\nOpcao invalida.')
    input('\nPressione "Enter" para tentar novamente. ')
    main()

# Bloco/funcao para a opcao 1, cadastrar um novo restaurante na lista "lista_restaurantes".
# Executado em "escolher_opcao()".
def cadastrar_novo_restaurante():
    limpeza_e_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante: ')
    categoria = (input(f'Digite qual a categoria do restaurante {nome_do_restaurante}: '))

    # Dicionario para armazenar os dados do cadastro.
    dados_restaurante = {'Nome':nome_do_restaurante, 'Categoria':categoria, 'Ativo':False}

    # Comando que armazena os valores da variavel "dados_restaurante" dentro da lista "lista_restaurantes".
    lista_restaurantes.append(dados_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')
    voltar_menu()

# Bloco/funcao para a opcao 2, exibe a lista de restaurantes cadastrados na lista "lista_restaurantes".
# Executado em "escolher_opcao()".
def listar_restaurantes():
    contador = 1
    limpeza_e_subtitulo('Listando os restaurantes')

    print(f'{'NOME'.ljust(23)} | {'CATEGORIA'.ljust(20)} | STATUS')
    # Estrutura condicional "for".
    # "Para cada item na lista X, os detalhes de tais itens."
    # "Para cada restaurante na lista de restaurantes, exiba o nome do restaurante, categoria e status."
    for restaurante in lista_restaurantes:
        # Puxando os detalhes descritos na lista usando a string escrita antes dos ":".
        nome_restaurante = restaurante['Nome']
        categoria = restaurante['Categoria']

        # "Se a string 'Ativo', de 'restaurante' (da lista 'lista_restaurantes'), for de status 'Ativo', armazene 'Ativo' na varievel 'atividade', se nao for, armazene 'Inativo'."
        atividade = 'Ativo' if restaurante['Ativo'] else 'Inativo'
        
        print(f'{contador}. {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {atividade}')
        # Contador para numerar em ordem crescente a lista de restaurantes.
        contador = contador + 1

    voltar_menu()

# Bloco/funcao para a opcao 3, possibilita ativar/desativar restaurante lista "lista_restaurantes".
# Executado em "escolher_opcao()".
def status_restaurante():
    limpeza_e_subtitulo('Ativar/Desativar restaurante')
    nome_restaurante = input('Digite o nome do restaurante que quer ativar ou desativar: ')
    restaurante_encontrado = False

    for restaurante in lista_restaurantes:
        if nome_restaurante == restaurante['Nome']:
            restaurante_encontrado = True
            restaurante['Ativo'] = not restaurante['Ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso!' if restaurante['Ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso!'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante nao foi encontrado.')        

    voltar_menu()

# Bloco/funcao que exibe as opcoes do programa conforme a resposta do usuario.
# Executado em "main()".
def escolher_opcao():
    # Tenta executar o seguinte codigo abaixo.
    # Caso colha um valor INTEIRO invalido (<1 ou >4), direciona para o "else".
    # Caso colha um valor NAO INTEIRO (letras, flutuantes, booleanos, etc), direciona para o "except."
    try:
        # "input" naturalmente coleta strings, "int" é necessario para transformar em inteiro. 
        opcao_escolhida = int(input('Escolha uma opcao: '))

        # se
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        # se (sequencial)
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            status_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        # senao (opcao restante)
        else:
            opcao_invalida()
    except:
        opcao_invalida()

        

    # SINTAXE "MATCH": Pode substittuir de maneira mais "limpa" os "if/elif/else" em situacoes com muitas opcoes.
    # ->"case _" é para todo aquele dado que nao é usado em outras opcoes.
    #
    # match opcao_escolhida:
    #     case 1:
    #         print('Adicionar restaurante')
    #     case 2:
    #         print('Listar restaurantes')
    #     case 3:
    #         print('Ativar restaurante')
    #     case 4:
    #         finalizar_app()
    #     case _:
    #         print('Opcao invalida!')
        
# Bloco principal com todo o algoritmo sendo executado utilizando sub-blocos definidos acima.
def main():
    # Limpa o terminal inicialmente sempre que o programa é executado.
    os.system('cls')
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()

# ==================================================================================


# Sempre que um script .py é executado atraves do proprio Python, seu nome é definido como 
# "__main__", assim o tornando o modulo principal de toda a execucao, possibilitando acoes 
# como esta que executa o bloco "main" caso o nome seja este.
if __name__ == '__main__':
    main()