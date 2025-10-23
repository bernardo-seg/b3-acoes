import streamlit as st
import yfinance as yf #biblioteca do yahoo que conseguimos puxar informações de ações

st.set_page_config(
    page_title="Painel Ações da B3",
    #page_icon=":chart_with_upwards_trend:",
    layout="wide"
)

st.header('**Painel de fechamento e dividendos de ações da B3**')

#após a virgula foi deixada uma ação padrão para quando aparecer a tela, não ficar em branco.
ticker = st.text_input('Digite o ticker/sigla da ação desejada (ex: PETR4.SA, VALE3.SA, ITUB4.SA):', 'PETR4')
#.SA é para facilitar a busca de ações da bolsa brasileira (B3) na biblioteca yfinance. muitas pessoaas esquecem
empresa = yf.Ticker(f'{ticker}.SA')

#esse é o período que queremos puxar os dados, nesse caso, de 2010 até 2024
ticker_df = empresa.history(
    period='1y', #nesse caso, ou puxamos o período de 1 dia, ou podemos puxar um intervalo específico com start e end
    #start='2019-1-01',
    #end='2025-09-30'
    )

#declaracao de colunas para organizar o layout
col1, col2, col3 = st.columns([1,1,1])#entre parenteses são as distancias relativas de cada coluna

#Perceba que se usa marcação markdown dentro do st.write para deixar o texto em negrito, itálico, etc.
with col1:
    st.write(f'**Empresa:** {empresa.info['longName']}') #entre colchetes é o nome completo da empresa. Especifico da biblioteca do Yahoo
with col2:
    st.write(f'**Mercado:** {empresa.info['market']}') #mercado da empresa
with col3:
    st.write(f'**Preço Atual:** {empresa.info['currentPrice']}') #empresa é a variavel declarada anteriormente

#gráfico de linhas do preço de fechamento da ação
st.line_chart(ticker_df.Close)#gráfico de linha do preço de fechamento da ação

#gráfico de barras dos dividendos pagos pela ação
st.bar_chart(ticker_df.Dividends)#gráfico de barras dos dividendos pagos pela ação