import bs4
from pip._vendor import requests



#chamada: python bs/beauty4.py

def extrair_frases():
    r = requests.get('http://quotes.toscrape.com')
    html = r.text
    soup = bs4.BeautifulSoup(html, 'html.parser')
    frases = soup.findAll('span',{'class': 'text'})
    frases_sem_tag = []
    for frase in frases:
        frases_sem_tag.append(frase.string)


    return frases_sem_tag

def extrair_primeira_frase():
    todas_frases = extrair_frases()
    #primeira_frase = soup.find('span') #Faz a mesma coisa da linha acima mas aí analisa toda a arvore

    return todas_frases[0]    

for frase in extrair_frases():
    frase=frase.string
    #print(frase)

def extrair_autores():
    r = requests.get('http://quotes.toscrape.com')
    html = r.text
    soup = bs4.BeautifulSoup(html, 'html.parser')
    autores = soup.findAll('small')
    autores_sem_tag = []
    for autor in autores:
        autores_sem_tag.append(autor.string)

    print(autores_sem_tag)
    return autores_sem_tag    

def extrair_primeiro_autor():
    autores = extrair_autores()
    return autores[0]



#r = requests.get('https://quotes.toscrape.com')
#html = r.text

#soup = bs4.BeautifulSoup(html, 'html.parser') #dizendo que o código que esta vindo é html


#print (soup)
#print(type(html))
#print(type(soup))
#print(soup.title.string) #imprime o title
#print(soup.span.string) #imprime o primeiro span
#print(soup.title.parent) #imprime tudo que esta dentro da head
#print(soup.title.parent.name) #imprime só o nome da tag

#print(soup.findAll('span'))

#for tag in soup.findAll('span'):
 #   print(20*'-')
  #  print(tag)