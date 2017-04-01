import requests
import json
import time
req=None

def requisicao(titulo):

    titulo=str(titulo).replace(" ","+")

    try:
        req = requests.get("http://www.omdbapi.com/?t="+titulo+"&type=movie")
        dicionario = json.loads(req.text)

        print("\n\n*-------------------------------------------------------------------------------------------------------*\n"
              "    Titulo:",dicionario["Title"]+"\n"
              "    Ano:",dicionario["Year"]+"\n"
              "    Diretor:",dicionario["Director"]+"\n"
              "    Atores:",dicionario["Actors"]+"\n"
              "    Generos:",dicionario["Genre"]+"\n"
              "    Nota:",dicionario["imdbRating"]+"/10"+"\n"
              "    Prêmios:",dicionario["Awards"]+"\n\n"
              "    Posters:",dicionario["Poster"]+"\n\n"
              "    Local de gravção:",dicionario["Country"]+"\n"
              "*-------------------------------------------------------------------------------------------------------*\n\n")
    except:
        if(dicionario["Response"]=="False"):
            print("\nFilme não encontrado!, Tente novamente!\n")
        else:
            print("\n\nErro de conexao!\n\n")




print('''
              +----------------------------+
              |                            |
              |   Bem vindo ao cineminha   |
              |             da             |
              |         Fsociety-BR        |
              |                            |
              +----------------------------+

''')

Sair=False

while not Sair:
    titulo=input("Digite o nome do filme em Inglês Ou em Português se o filme for brasileiro.\n"
                 "Digite sair para fechar: ")

    if(str(titulo).upper()=="SAIR"):
        print("\nAté a proxima!\n3 segundos para sair!".center(50))
        time.sleep(3)
        Sair=True
        continue

    requisicao(titulo)


