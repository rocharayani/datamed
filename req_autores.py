from pip._vendor import requests 

def coletando_autores():
    r = requests.get('https://quotes.toscrape.com/') #URL do site onde sera feita coleta
    html = r.text.split('\n')

    autores = []

    for linha in html:
        if '<small class="author" itemprop="author">' in linha:
            linha_editada = linha.replace('<span>by <small class="author" itemprop="author">', '') #Substituindo "span" por nada, eliminando
            linha_editada = linha_editada.replace('</small>', '')
            linha_editada = linha_editada.strip()
            autores.append(linha_editada)
            #print(linha_editada)

    return autores        

print(coletando_autores())

def coletando_primeiro_autor():
    autores = coletando_autores()
    return autores[0]
