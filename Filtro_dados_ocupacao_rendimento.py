import pandas as pd


def atributos_empregaticios(df,cor):
    final_df[cor+'_conta_propria'] = df_cor_raca_posicao_ocupacao[(df_cor_raca_posicao_ocupacao.cor_raca_posicao_ocupacao==cor+'_posicao_ocupacao')
                                                                 &(df_cor_raca_posicao_ocupacao.Nome=='Conta própria')][['2010']].reset_index(drop=True)

    final_df[cor+'_empregadora'] = df_cor_raca_posicao_ocupacao[(df_cor_raca_posicao_ocupacao.cor_raca_posicao_ocupacao==cor+'_posicao_ocupacao')
                                                               &(df_cor_raca_posicao_ocupacao.Nome=='Empregadores')][['2010']].reset_index(drop=True)

    final_df[cor+'_producao_consumo'] = df_cor_raca_posicao_ocupacao[(df_cor_raca_posicao_ocupacao.cor_raca_posicao_ocupacao==cor+'_posicao_ocupacao')
                                                               &(df_cor_raca_posicao_ocupacao.Nome=='Trabalhadores na produção para o próprio consumo')][['2010']].reset_index(drop=True)

    final_df[cor+'_militares_func_publicos'] = df_cor_raca_posicao_ocupacao[(df_cor_raca_posicao_ocupacao.cor_raca_posicao_ocupacao==cor+'_posicao_ocupacao')
                                                               &(df_cor_raca_posicao_ocupacao.Nome=='Militares e funcionários públicos estatutários')][['2010']].reset_index(drop=True)

    final_df[cor+'_sem_careita'] = df_cor_raca_posicao_ocupacao[(df_cor_raca_posicao_ocupacao.cor_raca_posicao_ocupacao==cor+'_posicao_ocupacao')
                                                               &(df_cor_raca_posicao_ocupacao.Nome=='Sem carteira de trabalho assinada')][['2010']].reset_index(drop=True)

    final_df[cor+'_com_carteira'] = df_cor_raca_posicao_ocupacao[(df_cor_raca_posicao_ocupacao.cor_raca_posicao_ocupacao==cor+'_posicao_ocupacao')
                                                               &(df_cor_raca_posicao_ocupacao.Nome=='Com carteira de trabalho assinada')][['2010']].reset_index(drop=True)

    final_df[cor+'_nao_remunerada'] = df_cor_raca_posicao_ocupacao[(df_cor_raca_posicao_ocupacao.cor_raca_posicao_ocupacao==cor+'_posicao_ocupacao')
                                                               &(df_cor_raca_posicao_ocupacao.Nome=='Não remunerados')][['2010']].reset_index(drop=True)
    return final_df


def atributos_salarios(df,cor):
    final_df[cor+'_5_a_10_salarios'] = df_cor_raca_rendimento[(df_cor_raca_rendimento.cor_raca_rendimento==cor+'_rendimento')
                                                                 &(df_cor_raca_rendimento.Nome=='Mais de 5 a 10 salários mínimos')][['2010']].reset_index(drop=True)
    final_df[cor+'_menos_de_1'] = df_cor_raca_rendimento[(df_cor_raca_rendimento.cor_raca_rendimento==cor+'_rendimento')
                                                                 &(df_cor_raca_rendimento.Nome=='Mais de 1/4 a 1/2 salário mínimo')][['2010']].reset_index(drop=True)+df_cor_raca_rendimento[(df_cor_raca_rendimento.cor_raca_rendimento==cor+'_rendimento')
                                                                 &(df_cor_raca_rendimento.Nome=='Mais de 1/8 a 1/4 de salário mínimo')][['2010']].reset_index(drop=True)+df_cor_raca_rendimento[(df_cor_raca_rendimento.cor_raca_rendimento==cor+'_rendimento')
                                                                 &(df_cor_raca_rendimento.Nome=='Mais de 1/2 a 1 salário mínimo')][['2010']].reset_index(drop=True)+df_cor_raca_rendimento[(df_cor_raca_rendimento.cor_raca_rendimento==cor+'_rendimento')
                                                                 &(df_cor_raca_rendimento.Nome=='Até 1/8 de salário mínimo')][['2010']].reset_index(drop=True)
      
      
    final_df[cor+'_mais_de_10'] = df_cor_raca_rendimento[(df_cor_raca_rendimento.cor_raca_rendimento==cor+'_rendimento')
                                                                 &(df_cor_raca_rendimento.Nome=='Mais de 10 salários mínimos')][['2010']].reset_index(drop=True)
    
    final_df[cor+'_1_a_2_salarios'] = df_cor_raca_rendimento[(df_cor_raca_rendimento.cor_raca_rendimento==cor+'_rendimento')
                                                                 &(df_cor_raca_rendimento.Nome=='Mais de 1 a 2 salários mínimos')][['2010']].reset_index(drop=True)
    
    final_df[cor+'_sem_rendimento'] = df_cor_raca_rendimento[(df_cor_raca_rendimento.cor_raca_rendimento==cor+'_rendimento')
                                                                 &(df_cor_raca_rendimento.Nome=='Sem rendimento')][['2010']].reset_index(drop=True)
    
    final_df[cor+'_2_a_3_salarios'] = df_cor_raca_rendimento[(df_cor_raca_rendimento.cor_raca_rendimento==cor+'_rendimento')
                                                                 &(df_cor_raca_rendimento.Nome=='Mais de 2 a 3 salários mínimos')][['2010']].reset_index(drop=True)
    
    final_df[cor+'_3_a_5_salarios'] = df_cor_raca_rendimento[(df_cor_raca_rendimento.cor_raca_rendimento==cor+'_rendimento')
                                                                 &(df_cor_raca_rendimento.Nome=='Mais de 3 a 5 salários mínimos')][['2010']].reset_index(drop=True)
    
  
  
    return final_df

x = pd.read_csv('Censo (1).csv')
cores= ['amarela','branca','parda','indigena','preta']#'sem_declaracao', quase não possui dados
##facilitar a identificação no dataframe
x['cor_raca_posicao_ocupacao'] = ''
#posicao_ocupacao

x.at[x[x['Posição'].str.startswith('3.1.1.1')].index,'cor_raca_posicao_ocupacao'] = 'amarela_posicao_ocupacao'

x.at[x[x['Posição'].str.startswith('3.1.1.2')].index,'cor_raca_posicao_ocupacao'] = 'branca_posicao_ocupacao'

x.at[x[x['Posição'].str.startswith('3.1.1.3')].index,'cor_raca_posicao_ocupacao'] = 'indigena_posicao_ocupacao'

x.at[x[x['Posição'].str.startswith('3.1.1.4')].index,'cor_raca_posicao_ocupacao'] = 'parda_posicao_ocupacao'

x.at[x[x['Posição'].str.startswith('3.1.1.5')].index,'cor_raca_posicao_ocupacao'] = 'preta_posicao_ocupacao'

x.at[x[x['Posição'].str.startswith('3.1.1.6')].index,'cor_raca_posicao_ocupacao'] = 'sem_declaracao_posicao_ocupacao'

#rendimento

x['cor_raca_rendimento'] = ''

x.at[x[x['Posição'].str.startswith('3.2.1.1')].index,'cor_raca_rendimento'] = 'amarela_rendimento'

x.at[x[x['Posição'].str.startswith('3.2.1.2')].index,'cor_raca_rendimento'] = 'branca_rendimento'

x.at[x[x['Posição'].str.startswith('3.2.1.3')].index,'cor_raca_rendimento'] = 'indigena_rendimento'

x.at[x[x['Posição'].str.startswith('3.2.1.4')].index,'cor_raca_rendimento'] = 'parda_rendimento'

x.at[x[x['Posição'].str.startswith('3.2.1.5')].index,'cor_raca_rendimento'] = 'preta_rendimento'

x.at[x[x['Posição'].str.startswith('3.2.1.6')].index,'cor_raca_rendimento'] = 'sem_declaracao_rendimento'

x.at[x[x['2010']==99999999999992.0].index,'2010'] = 0# remover valores absurdos


df_cor_raca_posicao_ocupacao = x[(~x.Localidade.isna()&((x.cor_raca_posicao_ocupacao!='')))][['Localidade','cor_raca_posicao_ocupacao','Nome','2010']]
df_cor_raca_posicao_ocupacao['estado'] = 'pr'

df_cor_raca_rendimento = x[(~x.Localidade.isna()&((x.cor_raca_rendimento!='')))][['Localidade','cor_raca_rendimento','Nome','2010']]
df_cor_raca_rendimento['estado'] = 'pr'

final_df = pd.DataFrame()

final_df = df_cor_raca_posicao_ocupacao[(df_cor_raca_posicao_ocupacao.cor_raca_posicao_ocupacao=='amarela_posicao_ocupacao')&(df_cor_raca_posicao_ocupacao.Nome=='Conta própria')][['Localidade','estado']].reset_index(drop=True)

for cor in cores:
    final_df = atributos_empregaticios(final_df,cor)

for cor in cores:
    final_df = atributos_salarios(final_df,cor)
