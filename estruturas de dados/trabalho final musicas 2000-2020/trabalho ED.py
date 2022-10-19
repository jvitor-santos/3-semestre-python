import matplotlib.pyplot as plt

def pesquisa_ano():
    n=int(input('Digite o ano que deseja pesquisar: '))
    if n>=2000 and n<=2010:
        arquivo=open("playlist 2000-2010.txt",'r')
        variavel=str(n)
        criar=open("resultado da ultima pesquisa por ano.txt",'w')
        criar.write(str(variavel+'\n'))
        for linha in arquivo:
            dado=linha.split(';')
            if variavel in dado[3]:
                print(dado[0],'-',dado[1],'-',dado[2])
                criar.write(str(dado[0]+'- '+dado[1]+'- '+dado[2]+'\n'))
        arquivo.close()
        criar.close()
    elif n>=2011 and n<=2020:
        arquivo=open("playlist 2011-2020.txt",'r')
        variavel=str(n)
        criar=open("resultado da ultima pesquisa por ano.txt",'w')
        criar.write(str(variavel+'\n'))
        for linha in arquivo:
            dado=linha.split(';')
            if variavel in dado[3]:
                print(dado[0],'-',dado[1],'-',dado[2])
                criar.write(str(dado[0]+'- '+dado[1]+'- '+dado[2]+'\n'))
        arquivo.close()
        criar.close()
    else:
        print('Ano invalido!')


def pesquisa_artista():
    soma=0
    dado0=[]
    dado1=[]
    dado2=[]
    dado3=[]
    artista=str(input('Digite o nome do artista: ')).lower()
    arquivo=open("playlist 2000-2010.txt",'r')
    arquivo2=open("playlist 2011-2020.txt",'r')
    criar=open("resultado da ultima pesquisa por artista.txt",'w')
    for linha in arquivo:
        dado=linha.split(';')
        if artista in dado[1]:
            soma+=1
            dado0.append(dado[0])
            dado1.append(dado[1])
            dado2.append(dado[2])
            dado3.append(dado[3])
    
    for linha in arquivo2:
        dado=linha.split(';')
        if artista in dado[1]:
            soma+=1
            dado0.append(dado[0])
            dado1.append(dado[1])
            dado2.append(dado[2])
            dado3.append(dado[3])
    if soma==0 or soma>=50:
        print('Artista não encontrado ou nome digitado errado')
        criar.write(str(artista.upper() +' não foi encontrado nos top 10 dos anos 2000 até 2020'))
    else:
        for i in range(len(dado0)):
            print(dado0[i]+'- '+dado1[i]+'- '+dado2[i]+'- '+dado3[i])
            criar.write(str(dado0[i]+'- '+dado1[i]+'- '+dado2[i]+'- '+dado3[i]+'\n'))
    arquivo.close()
    arquivo2.close()
    criar.close()

def pesquisa_musica():
    soma=0
    musica=str(input('Digite o nome da musica: ')).lower()
    arquivo=open("playlist 2000-2010.txt",'r')
    arquivo2=open("playlist 2011-2020.txt",'r')
    criar=open("resultado da ultima pesquisa por musica.txt",'w')
    for linha in arquivo:
        dado=linha.split(';')
        if musica == dado[2]:
            print(dado[0],'-',dado[1],'-',dado[2],'-',dado[3])
            criar.write(str(dado[0]+'- '+dado[1]+'- '+dado[2]+'- '+dado[3]+'\n'))
            soma+=1

    for linha in arquivo2:
        dado=linha.split(';')
        if musica == dado[2]:
            print(dado[0],'-',dado[1],'-',dado[2],'-',dado[3])
            criar.write(str(dado[0]+'- '+dado[1]+'- '+dado[2]+'- '+dado[3]+'\n'))
            soma+=1
    if soma==0:
        print('Musica não encontrada')
        criar.write(str(musica.upper() +' não foi encontrado nos top 10 dos anos 2000 até 2020'))
    arquivo.close()
    arquivo2.close()
    criar.close()


def pesquisa_posicao():
    soma=0
    n=int(input('Digite a posção que deseja saber: '))
    arquivo=open("playlist 2000-2010.txt",'r')
    arquivo2=open("playlist 2011-2020.txt",'r')
    posi=str(n)
    if n >=1 and n<=10:
        criar=open("resultado da ultima pesquisa por posição.txt",'w')
        for linha in arquivo:
            dado=linha.split(';')
            if posi == dado[0]:
                print(dado[0],'-',dado[1],'-',dado[2],'-',dado[3])
                criar.write(str(dado[0]+'- '+dado[1]+'- '+dado[2]+'- '+dado[3]+'\n'))
                soma+=1
        for linha in arquivo2:
            dado=linha.split(';')
            if posi == dado[0]:
                print(dado[0],'-',dado[1],'-',dado[2],'-',dado[3])
                criar.write(str(dado[0]+'- '+dado[1]+'- '+dado[2]+'- '+dado[3]+'\n'))
                soma+=1
        criar.close()
    else:
        print('posição invalida')
    arquivo.close()
    arquivo2.close()

def grafico_ano():
    varial=int(input('Digite o ano que deseja fazer o grafico: '))
    a=[]
    if varial >=2000 and varial<=2010:
        arquivo=open("playlist 2000-2010.txt",'r')
        teste=str(varial)
        for linha in arquivo:
            dado=linha.split(';')
            if teste in dado[3]:
                a.append(dado[4])
                plt.hist(a)
        arquivo.close()
    elif varial>=2011 and varial<=2020:
        arquivo=open("playlist 2011-2020.txt",'r')
        teste=str(varial)
        for linha in arquivo:
            dado=linha.split(';')
            if teste in dado[3]:
                a.append(dado[4])
                plt.hist(a)
        arquivo.close()

    plt.ylabel('Quantidade de vezes que a musica esteve no top 10 do ano {}'.format(varial))
    plt.xlabel('Estilos de musicas')
    plt.show()


def grafico_geral():
    a=[]
    arquivo=open("playlist 2000-2010.txt",'r')
    arquivo2=open("playlist 2011-2020.txt",'r')
    for linha in arquivo:
        dado=linha.split(';')
        a.append(dado[4])

    for linha in arquivo2:
        dado=linha.split(';')
        a.append(dado[4])

    plt.hist(a)
    plt.ylabel('Quantidade de vezes que a musica esteve no top 10 nos anos de 2000 a 2020')
    plt.xlabel('Estilos de musicas')
    plt.show()
    arquivo.close()
    arquivo2.close()


def grafico_cantor():
    cantor=str(input('Digite o nome do cantor para gerar o grafico: ')).lower()
    z=0
    a=[]
    arquivo=open("playlist 2000-2010.txt",'r')
    arquivo2=open("playlist 2011-2020.txt",'r') 
    for linha in arquivo:
        dado=linha.split(';')
        if cantor in dado[1]:
            z+=1
            a.append(dado[3])
            plt.hist(a)
    for linha in arquivo2:
        dado=linha.split(';')
        if cantor in dado[1]:
            z+=1
            a.append(dado[3])
            plt.hist(a)
    if z<50:
        plt.show()
    else:
        print('Nome do cantor digitado errado!')
    arquivo.close()
    arquivo2.close()

resp='sim'
while resp.lower()=='sim':
    pesquisa=str(input('Deseja apenas pesquisar ou ver um gráfico: '))
    if pesquisa=='pesquisar' or pesquisa=='pesquisa':
        opc=str(input('Deseja pesquisar por ano, artista, musica ou posição?: ')).lower()
        if opc=='ano':
            pesquisa_ano()
        elif opc=='artista':
            pesquisa_artista()
        elif opc=='musica':
            pesquisa_musica()
        elif opc=='posição' or opc=='posicao':
            pesquisa_posicao()
        else:
            print('Desculpa filtro invalido')
    elif pesquisa=='grafico' or pesquisa=='gráfico':
        opcao=str(input('Deseja ver um gráfico de ano especifico, geral ou de um cantor?: ')).lower()
        if opcao=='especifico' or opcao=='específico' or opcao=='ano' or opcao=='ano especifico' or opcao=='ano específico':
            grafico_ano()
        elif opcao=='geral' or opcao=='todos':
            grafico_geral()
        elif opcao=='cantor' or opcao=='artista':
            grafico_cantor()
        else:
            print('Desculpa filtro invalido')
    else:
        print('Desculpa filtro invalido')
    resp=str(input('Deseja continuar?: '))
print('Algoritmo finalizado!')