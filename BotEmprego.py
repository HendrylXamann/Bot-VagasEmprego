import requests
from bs4 import BeautifulSoup
import pandas as pd

lista = [] #lista vazia

#Processo de transformação do conteúdo do site:
first_site = requests.get('https://oportunidadesdf.com/estagio/') #Aqui utilizando o request vamos abrir o link;
content = first_site.content #Pega o conteúdo do site;
site_transfor = BeautifulSoup(content, 'html.parser') #Confirma que é um html e passa isso pra variável;
#Busca do título:
 #Busca principal, class onde está o que almejo extrair:
busca1 = site_transfor.find_all('div', attrs={'class': 'elementor-post__text'})#Esse find é o que procura, semelhança com o find_element do selenium;

#Retorno exato do que eu quero:
def buscar(var):
    for div in var:
        vaga = div.find('h3', attrs={'class':'elementor-post__title' }) #Dentro da página, dentro da div vai buscar TODOS os h3;
        if vaga: #verifica se a var tem resultado
            limpar = vaga.text.strip() #Pega o texto e remove espaços em branco extras
            lista.append([limpar]) #Adiciona na lista o conteúdo já limpo
        else: #Se não tiver nenhuma vaga vai printar esse texto; 
            print('Sem vagas')
            
buscar(busca1) 

#Criação da planilha: 
tabela = pd.DataFrame(lista, columns=['Vagas'])
tabela.to_excel('vagas.xlsx', index=False)






#obs útil sobre request: Usando print(variavel com o get.status_code) conseguimos ver se deu certo ou se deu algum erro, 200 é sucesso 400 erro do cliente, 500 erro do servidor;

