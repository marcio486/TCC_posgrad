from selenium import webdriver
import pandas as pd
import time
chromedriver = 'chromedriver_linux64/chromedriver'

options = webdriver.ChromeOptions()
options.add_argument('headless')

cidades = pd.read_csv('cities.csv').drop(columns=['Unnamed: 0'])
cidades['cidade'] = cidades.cities.apply(lambda x: x.split('-')[0].strip().replace(' ','-').lower())
cidades['estado'] = cidades.cities.apply(lambda x: x.split('-')[1].strip().lower())
x = pd.read_csv('excluir.csv')
cidades = cidades[~cidades.cidade.isin(x.cidade)]

colunas = ['cidade',
'estado',
'habitantes',
'ranking_habitantes_pais',
'ranking_habitantes_estado',
'densidade_demografica',
'salario_medio',
'ranking_salario_pais',
'ranking_salario_estado',
'pessoas_ocupadas',
'porcentagem_ocupada',
'escolarizacao_6_14',
'ranking_escolaridade_pais',
'ranking_escolaridade_estado',
'anos_inicias_fundamental_publico',
'anos_inicias_fundamental_particular',
'pib_per_capta',
'ranking_pib_pais',
'ranking_pib_estado',
'percentual_receita_externa',
'total_receitas_realizadas',
'total_receitas_empenhadas',
'mortalidade_infantil',
'ranking_mortalidade_pais',
'ranking_mortalidade_estado',
'internacoes_diarreia',
'area_territorial',
'ranking_area_pais',
'ranking_area_estado',
'percentual_esgoto',
'percentual_arborizacao_publica',
'percentual_urbanizacao_publica'
]

full_df = pd.DataFrame(columns=colunas)


for element in cidades.iterrows():
    
    print(element[1][1],element[1][2])
    driver = webdriver.Chrome(executable_path=chromedriver, options=options)
    url ="https://cidades.ibge.gov.br/brasil/"+element[1][2]+"/"+element[1][1]+"/panorama"
    
    driver.get(url)
    time.sleep(10)
    try: habitantes = driver.find_elements_by_xpath('//panorama-painel[(((count(preceding-sibling::*) + 1) = 3) and parent::*)]//*[contains(concat( " ", @class, " " ), concat( " ", "selecionado", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "indicador__valor", " " ))]')[0].text
    except: habitantes = -1
    try: ranking_habitantes_pais = driver.find_elements_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "comparacao__regiao", " " )) and (((count(preceding-sibling::*) + 1) = 1) and parent::*)]//*[contains(concat( " ", @class, " " ), concat( " ", "comparacao__regiao__regua__posicao__valor", " " ))]')[0].text
    except: ranking_habitantes_pais = -1
    try: ranking_habitantes_estado = driver.find_elements_by_xpath('//panorama-painel[(((count(preceding-sibling::*) + 1) = 3) and parent::*)]//*[contains(concat( " ", @class, " " ), concat( " ", "comparacao__regiao", " " )) and (((count(preceding-sibling::*) + 1) = 2) and parent::*)]//*[contains(concat( " ", @class, " " ), concat( " ", "comparacao__regiao__regua__posicao__valor", " " ))]')[0].text
    except: ranking_habitantes_estado= -1
    try :densidade_demografica = driver.find_elements_by_xpath('//panorama-painel[(((count(preceding-sibling::*) + 1) = 3) and parent::*)]//panorama-card[(((count(preceding-sibling::*) + 1) = 2) and parent::*)]//*[contains(concat( " ", @class, " " ), concat( " ", "indicador__valor", " " ))]')[0].text
    except: densidade_demografica= -1

    try :salario_medio = driver.find_elements_by_xpath('//panorama-painel[(((count(preceding-sibling::*) + 1) = 9) and parent::*)]//*[contains(concat( " ", @class, " " ), concat( " ", "selecionado", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "indicador__valor", " " ))]')[0].text
    except: salario_medio  = -1
    try : ranking_salario_pais = driver.find_elements_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "p93", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "comparacao__regiao__regua__posicao__valor", " " ))]')[1].text
    except: ranking_salario_pais= -1
    try :ranking_salario_estado = driver.find_elements_by_xpath('//panorama-painel[(((count(preceding-sibling::*) + 1) = 9) and parent::*)]//*[contains(concat( " ", @class, " " ), concat( " ", "comparacao__regiao", " " )) and (((count(preceding-sibling::*) + 1) = 2) and parent::*)]//*[contains(concat( " ", @class, " " ), concat( " ", "comparacao__regiao__regua__posicao__valor", " " ))]')[0].text
    except: ranking_salario_estado= -1
    try: pessoas_ocupadas = driver.find_elements_by_xpath('//panorama-painel[(((count(preceding-sibling::*) + 1) = 9) and parent::*)]//panorama-card[(((count(preceding-sibling::*) + 1) = 2) and parent::*)]//*[contains(concat( " ", @class, " " ), concat( " ", "indicador__valor", " " ))]')[0].text
    except: pessoas_ocupadas = -1
    try :porcentagem_ocupada = driver.find_elements_by_xpath('//panorama-painel[(((count(preceding-sibling::*) + 1) = 9) and parent::*)]//panorama-card[(((count(preceding-sibling::*) + 1) = 3) and parent::*)]//*[contains(concat( " ", @class, " " ), concat( " ", "indicador__valor", " " ))]')[0].text
    except: porcentagem_ocupada= -1
    
    
    try :escolarizacao_6_14 = driver.find_elements_by_xpath('//panorama-painel[(((count(preceding-sibling::*) + 1) = 13) and parent::*)]//*[contains(concat( " ", @class, " " ), concat( " ", "selecionado", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "indicador__valor", " " ))]')[0].text
    except: escolarizacao_6_14 = -1
    try :ranking_escolaridade_pais = driver.find_elements_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "p85", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "comparacao__regiao__regua__posicao__valor", " " ))]')[0].text
    except: ranking_escolaridade_pais= -1
    try :ranking_escolaridade_estado = driver.find_elements_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "p79", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "comparacao__regiao__regua__posicao__valor", " " ))]')[0].text
    except: ranking_escolaridade_estado  = -1
    try: anos_inicias_fundamental_publico = driver.find_elements_by_xpath('//panorama-painel[(((count(preceding-sibling::*) + 1) = 13) and parent::*)]//panorama-card[(((count(preceding-sibling::*) + 1) = 2) and parent::*)]//*[contains(concat( " ", @class, " " ), concat( " ", "indicador__valor", " " ))]')[0].text
    except: anos_inicias_fundamental_publico= -1
    try :anos_inicias_fundamental_particular = driver.find_elements_by_xpath('//panorama-painel[(((count(preceding-sibling::*) + 1) = 13) and parent::*)]//panorama-card[(((count(preceding-sibling::*) + 1) = 3) and parent::*)]//*[contains(concat( " ", @class, " " ), concat( " ", "indicador__valor", " " ))]')[0].text
    except: anos_inicias_fundamental_particular= -1
    
    try:pib_per_capta = driver.find_elements_by_xpath('//panorama-painel[(((count(preceding-sibling::*) + 1) = 18) and parent::*)]//*[contains(concat( " ", @class, " " ), concat( " ", "selecionado", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "indicador__valor", " " ))]')[0].text
    except: pib_per_capta  = -1
    try:ranking_pib_pais = driver.find_elements_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "p93", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "comparacao__regiao__regua__posicao__valor", " " ))]')[1].text
    except: ranking_pib_pais= -1
    try :ranking_pib_estado = driver.find_elements_by_xpath('//panorama-painel[(((count(preceding-sibling::*) + 1) = 18) and parent::*)]//*[contains(concat( " ", @class, " " ), concat( " ", "p100", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "comparacao__regiao__regua__posicao__valor", " " ))]')[0].text
    except:ranking_pib_estado= -1
    
    
    try:percentual_receita_externa = driver.find_elements_by_xpath('//panorama-painel[(((count(preceding-sibling::*) + 1) = 18) and parent::*)]//panorama-card[(((count(preceding-sibling::*) + 1) = 2) and parent::*)]//*[contains(concat( " ", @class, " " ), concat( " ", "indicador__valor", " " ))]')[0].text
    except: percentual_receita_externa= -1
    try:total_receitas_realizadas = driver.find_elements_by_xpath('//panorama-painel[(((count(preceding-sibling::*) + 1) = 18) and parent::*)]//panorama-card[(((count(preceding-sibling::*) + 1) = 3) and parent::*)]//*[contains(concat( " ", @class, " " ), concat( " ", "indicador__valor", " " ))]')[0].text
    except: total_receitas_realizadas  = -1
    try:total_receitas_empenhadas = driver.find_elements_by_xpath('//panorama-painel[(((count(preceding-sibling::*) + 1) = 18) and parent::*)]//panorama-card[(((count(preceding-sibling::*) + 1) = 4) and parent::*)]//*[contains(concat( " ", @class, " " ), concat( " ", "indicador__valor", " " ))]')[0].text
    except: total_receitas_empenhadas= -1
    
    
    
    try:mortalidade_infantil = driver.find_elements_by_xpath('//panorama-painel[(((count(preceding-sibling::*) + 1) = 22) and parent::*)]//*[contains(concat( " ", @class, " " ), concat( " ", "selecionado", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "indicador__valor", " " ))]')[0].text
    except: mortalidade_infantil  = -1
    try:ranking_mortalidade_pais = driver.find_elements_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "p48", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "comparacao__regiao__regua__posicao__valor", " " ))]')[0].text
    except: ranking_mortalidade_pais= -1
    try:ranking_mortalidade_estado = driver.find_elements_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "p69", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "comparacao__regiao__regua__posicao__valor", " " ))]')[1].text
    except: ranking_mortalidade_estado= -1
    try:internacoes_diarreia = driver.find_elements_by_xpath('//panorama-painel[(((count(preceding-sibling::*) + 1) = 22) and parent::*)]//panorama-card[(((count(preceding-sibling::*) + 1) = 2) and parent::*)]//*[contains(concat( " ", @class, " " ), concat( " ", "indicador__valor", " " ))]')[0].text
    except: internacoes_diarreia= -1
    
    
    try:area_territorial = driver.find_elements_by_xpath('//panorama-painel[(((count(preceding-sibling::*) + 1) = 26) and parent::*)]//*[contains(concat( " ", @class, " " ), concat( " ", "indicador__valor", " " ))]')[0].text
    except: area_territorial  = -1
    
    try:ranking_area_pais = driver.find_elements_by_xpath('//panorama-painel[(((count(preceding-sibling::*) + 1) = 26) and parent::*)]//*[contains(concat( " ", @class, " " ), concat( " ", "p78", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "comparacao__regiao__regua__posicao__valor", " " ))]')[0].text
    except: ranking_area_pais= -1
    try:ranking_area_estado = driver.find_elements_by_xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "p79", " " ))]//*[contains(concat( " ", @class, " " ), concat( " ", "comparacao__regiao__regua__posicao__valor", " " ))]')[0].text
    except: ranking_area_estado= -1
    try:percentual_esgoto = driver.find_elements_by_xpath('//panorama-painel[(((count(preceding-sibling::*) + 1) = 26) and parent::*)]//panorama-card[(((count(preceding-sibling::*) + 1) = 2) and parent::*)]//*[contains(concat( " ", @class, " " ), concat( " ", "indicador__valor", " " ))]')[0].text
    except: percentual_esgoto= -1
    try:percentual_arborizacao_publica = driver.find_elements_by_xpath('//panorama-painel[(((count(preceding-sibling::*) + 1) = 26) and parent::*)]//panorama-card[(((count(preceding-sibling::*) + 1) = 3) and parent::*)]//*[contains(concat( " ", @class, " " ), concat( " ", "indicador__valor", " " ))]')[0].text
    except: percentual_arborizacao_publica= -1
    try:percentual_urbanizacao_publica = driver.find_elements_by_xpath('//panorama-painel[(((count(preceding-sibling::*) + 1) = 26) and parent::*)]//panorama-card[(((count(preceding-sibling::*) + 1) = 4) and parent::*)]//*[contains(concat( " ", @class, " " ), concat( " ", "indicador__valor", " " ))]')[0].text
    except: percentual_urbanizacao_publica= -1
    
    full_df = full_df.append(pd.DataFrame(columns= colunas,data = [[element[1][1],
                                                            element[1][2],
                                                            habitantes,
                                                            ranking_habitantes_pais,
                                                            ranking_habitantes_estado,
                                                            densidade_demografica,
                                                            salario_medio,
                                                            ranking_salario_pais,
                                                            ranking_salario_estado,
                                                            pessoas_ocupadas,
                                                            porcentagem_ocupada,
                                                            escolarizacao_6_14,
                                                            ranking_escolaridade_pais,
                                                            ranking_escolaridade_estado,
                                                            anos_inicias_fundamental_publico,
                                                            anos_inicias_fundamental_particular,
                                                            pib_per_capta,
                                                            ranking_pib_pais,
                                                            ranking_pib_estado,
                                                            percentual_receita_externa,
                                                            total_receitas_realizadas,
                                                            total_receitas_empenhadas,
                                                            mortalidade_infantil,
                                                            ranking_mortalidade_pais,
                                                            ranking_mortalidade_estado,
                                                            internacoes_diarreia,
                                                            area_territorial,
                                                            ranking_area_pais,
                                                            ranking_area_estado,
                                                            percentual_esgoto,
                                                            percentual_arborizacao_publica,
                                                            percentual_urbanizacao_publica]]))
    driver.close()
    
    full_df.to_csv('full_df2.csv')
