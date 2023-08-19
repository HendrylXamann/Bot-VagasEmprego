#Bibliotecas utilizadas:
import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime

#"função" para por o arquivo final com a data do dia:
data_do_dia = datetime.datetime.now().strftime("%d%m%Y") 
nome_da_planilha = f"{data_do_dia}.xlsx"

#Primeira Função de busca das vagas, site Linkedin:
def linkedin():
    lista = [] #Criação de uma lista vazia
    link = 'https://www.linkedin.com/jobs/search/?currentJobId=3690683662&f_TPR=r86400&geoId=104413988&keywords=estágio&location=Brasília%2C%20Distrito%20Federal%2C%20Brasil&refresh=true&position=5&pageNum=0'
    v_1 = requests.get(link) #Utilizando o request para abrir o link;
    content = v_1.content #Pega o conteúdo do site;
    site_transfor = BeautifulSoup(content, 'html.parser') #Confirma que é um html e passa isso para a variável;
    buscar = site_transfor.find_all('div', attrs={'class': 'base-search-card__info'}) #Esse find é o que procura, semelhança com o find_element do selenium;

    for div in buscar: # Loop pelos elementos HTML que contêm informações das vagas
        vaga = div.find('h3', attrs={'class': 'base-search-card__title'}) #Localiza o titulo exato da vaga
        if vaga: #Se tiver conteúdo na variável busca, ou seja, dando certo:
            limpar = vaga.text.strip() #"limpa" o texto eliminando espaços e quebras de linha
            link_vaga = link #Link da vaga
            lista.append([limpar, link_vaga]) #Preenche a lista
        else:
            print('Sem vagas no linkedin')

    return lista #Retorna o conteúdo tratado que já foi inserido na lista que antes estava vazia;
#Obs: As demais funções seguem a mesma lógica da primeira, alterando apenas os endereços pontuais

#Segunda Função de busca das vagas, site Oportunidades DF:
def oportunidadesdf():
    lista2 = []
    link2 = 'https://oportunidadesdf.com/estagio/'
    response = requests.get(link2)
    content = response.content
    site_transfor = BeautifulSoup(content, 'html.parser')
    busca1 = site_transfor.find_all('div', attrs={'class': 'elementor-post__text'})

    for div in busca1:
        vaga = div.find('h3', attrs={'class': 'elementor-post__title'})
        if vaga:
            limpar = vaga.text.strip()
            link_vaga = link2
            lista2.append([limpar, link_vaga])
        else:
            print('Sem vagas no oportunidades')

    return lista2

#Terceira Função de busca das vagas, site Infojobs:
def infojobs():
    lista3 = []
    link3 = 'https://www.infojobs.com.br/empregos.aspx?provincia=171&tipocontrato=4'
    response = requests.get(link3)
    content = response.content
    site_transfor = BeautifulSoup(content, 'html.parser')
    busca2 = site_transfor.find_all('div', attrs={'class': 'mr-8'})

    for div in busca2:
        vaga = div.find('h2', attrs={'class':'h3 font-weight-bold text-body mb-8' })
        if vaga:
            limpar = vaga.text.strip()
            link_vaga = link3
            lista3.append([limpar, link_vaga])
        else:
            print('Sem vagas no Info')

    return lista3

#Consolidação das vagas e links em um arquivo excel:
var_linkedin = linkedin()
var_oportunidadesdf = oportunidadesdf()
var_infojobs = infojobs()
lista_final = var_linkedin + var_oportunidadesdf + var_infojobs 
#Especificamente a criação do excel:
tabela = pd.DataFrame(lista_final, columns=['Vagas', 'Link'])
tabela.to_excel(nome_da_planilha, index=False)
