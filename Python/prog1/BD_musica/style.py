""" Esse é um arquivo auxiliar cujo objetivo é armazenar diversas
    opções de formatação. """

import time

# Para agrupar os conteúdos, será definida a Classe estilo:
class Style(object):
    """ Contém variados estilos de formatação de texto."""
    # Cores:
    black = "\033[30m"
    red = "\033[31m"
    green = "\033[32m"
    yellow = "\033[33m"
    blue = "\033[34m"
    purple = "\033[35m"
    cyan = "\033[36m"
    gray = "\033[37m"
    white = "\033[97m"

    # Estilos:
    normal = "\033[m"
    bold = "\033[1m"
    italic = "\033[3m"
    underline = "\033[4m"
    overline = "\033[53m"
    blink = "\033[5m"
    crossed = "\033[9m"

    def negrito(self, texto):
        """ Exibe o texto dado com 'negrito'. """
        print("{2}{0}{1} ".format(texto,\
        estilo.normal, estilo.bold))

    def sublinhado(self, texto):
        """ Exibe o texto dado com 'sublinhado'. OBS: método usado
        para formatação de subtítulos de 'tarefa atual'. """
        print("\n\t{2}{0}{1}\n"\
        .format(texto, estilo.normal, estilo.underline+estilo.blue))
        return

    def __init__(self):
        pass

# Instância de uso de Style:
estilo = Style()

def limparTela():
    print("\033c", end="", flush=True)
    return

def divisoria(quantidade, formatacao = estilo.normal):
    print(formatacao, end = '', flush=True)
    for i in range(quantidade):
        print("*", end="")
    print(estilo.normal)
    return

def opcaoErrada():
    """ Exibe texto para 'input' inválido. """
    limparTela()
    estilo.negrito("\n\tOpção Inválida!!!\n")
    return

def logAtividade(texto):
    """ Retorna texto com a formatação de Log de Opção. """
    return '{2}{1}{0}'.format(estilo.normal, texto,\
    estilo.bold+estilo.green)

def setaInput(tipo):
    """ Solicita ao usuário algum input, que é
    convertido ao 'tipo' informado. """
    print('\n{1}-> {0}'.format(estilo.normal, estilo.bold), end='')
    try:
        valor = tipo(input().strip())
    except ValueError:
        valor = -1
    return valor

def cabecalho():
    """ Imprime as Boas Vindas ao BD. """
    limparTela()
    divisoria(50, estilo.cyan)
    print("{2}*{1}   Olá, bem-vindo ao {3}Banco de Dados de Música!{0}{2}  *"\
        .format(estilo.normal, estilo.bold,\
         estilo.cyan, estilo.underline), flush=True)
    divisoria(50, estilo.cyan)
    print()
    return

def exibirMusica(musica, id=False):
    if id:
        estilo.negrito('ID: '+estilo.yellow+musica[0]+'\n')
    estilo.negrito('Nome: '+estilo.yellow+musica[1]+'\n')
    estilo.negrito('Banda: '+estilo.yellow+musica[2]+'\n')
    estilo.negrito('Album: '+estilo.yellow+musica[3]+'\n')
    estilo.negrito('Genero: '+estilo.yellow+musica[4]+'\n')
    return
 
def listarElementos(lista, numeracao=0, ordem=True):
    """ Imprime os elementos de uma lista e retorna "len(lista)-1". """
    if ordem:
        for elemento in lista:
            print('{2}{0}{3} - {1}'.format(numeracao,\
            elemento, estilo.bold, estilo.normal))
            numeracao += 1
    else:
        for elemento in lista:
            print('{0}'.format(elemento))
            numeracao += 1
    return numeracao

def menu():
    """ Imprime o Menu e retorna o valor escolhido. """
    print("{1}Por favor, escolha uma opção:{0}\n\n\
    {1}1{0} - Criar uma {2}Playlist{0};\n\
    {1}2{0} - Salvar {2}Playlist{0} no Arquivo;\n\
    {1}3{0} - Ler {2}Playlists{0} de {2}'Dados/'{0};\n\
    {1}4{0} - Apagar arquivo da {2}Playlist{0};\n\
    {1}5{0} - Listar Músicas de uma {2}Playlist{0};\n\
    {1}6{0} - Consultar uma Música;\n\
    {1}7{0} - Inserir nova Música no {2}Banco de Dados{0};\n\
    {1}8{0} - Listagem total ou filtrada;\n\
    {1}0{0} - Sair do programa.\n".format\
    (estilo.normal, estilo.bold, estilo.italic, estilo.blink), end='')

    # Para lidar com valores não numericos errados:
    try:
        resposta = setaInput(int)
    except KeyboardInterrupt:
        return 0
    except:
        opcaoErrada()
        return menu()

    # Para lidar com valores numéricos errados:
    if not 0 <= resposta <= 9:
        opcaoErrada()
        return menu()

    return resposta
