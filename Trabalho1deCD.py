import requests #pra obter o conteúdo do site
from bs4 import BeautifulSoup #pra fazer o scraping


#link do site
url = 'https://goldstandardsonglist.com/Pages_Sort_2a/Sort_2a.htm'
headers = { 'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36" }


site = requests.get(url, headers=headers) #o que tem em url é jogado no site
soup = BeautifulSoup(site.content, 'html.parser') #o conteúdo do site é especificado como HTML, o conteúdo do site é jogado no soup

#vamos pegar todas as tags do tipo td, cuja a class é igual table1column2, porque aqui tem os dados que a gente quer no site
#o que é retornado para A é uma lista de resultados
A = soup.find_all('td', class_='table1column2') 

LIST_NOMES_MUSICA = [] #lista para guardar o nome das músicas
LIST_ANO_MUSICA = [] #lista para guardar o ano da música
LIST_TIPO_MUSICA = [] #lista para guardar o tipo da música

contador = 0 #garante que eu pego apenas os primeiros 1000 resultados

#estou iterando i para pegar cada conteúdo de td que está salvo em A
#em j fica o conteúdo da tag span que está dentro da tag td
#se a tag span existe então, encontramos o nosso conteúdo desejado
#as funções da linha 32 e 33 é para substituir os caracteres '\n' e ',' do conteúdo, pois eles afetavam a formatação do csv

#pegando os dados que são os nomes das músicas
for i in A:
    j = i.find('span')
    if j != None:
        contador += 1
        s = j.text.replace('\n' , ' ')
        s = s.replace(',' , '')
        LIST_NOMES_MUSICA.append(s)
    if contador >= 1000:
        break

contador = 0

#pegando os dados que são os anos das músicas
B = soup.find_all('td', class_='table1column1')
for i in B:
    j = i.find('span')
    if j != None and (j.text[0] >= '1' and j.text[0] <= '9'):
        contador += 1
        s = j.text.replace('\n' , ' ')
        s = s.replace(',' , '')
        LIST_ANO_MUSICA.append(s)
    if contador >= 1000:
        break

contador = 0

#pegando os dados que são os gêneros das músicas
C = soup.find_all('td', class_='table1column3')
for i in C:
    j = i.find('span')
    if j != None:
        contador += 1
        s = j.text.replace('\n' , ' ')
        s = s.replace(',' , '')
        LIST_TIPO_MUSICA.append(s)
    if contador >= 1000:
        break

#criando arquivo csv com nome 'saida' usando o modo de escrita
f = open("saida.csv","w")
f.write("ano,musica,tipo\n")

for i in range(0, 1000):
    f.write(LIST_ANO_MUSICA[i]+','+ LIST_NOMES_MUSICA[i]+','+ LIST_TIPO_MUSICA[i] + '\n')