#!/usr/bin/env python
# coding: utf-8

# ### Dash
# 
# - Instalar o dash
# 
# 
# Estrutura Básica
# - plotly -> gráficos
# - Flask -> aplicação

# ### Como funciona o Dash
# 
# - Layout
#     - HTML -> textos, imagens, espaços
#     - Dash Components (Core Components) -> gráficos, botões que mexem em gráficos, coisas do dashboard
# - Callbacks

# #### Primeiro Dashboard

# In[21]:


from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd


app = Dash(__name__) # criando o seu aplicativo Dash


# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.read_excel("Vendas.xlsx")

# df = tabela = dataframe

# plotly
fig = px.bar(df, x="Produto", y="Quantidade", color="ID Loja", barmode="group")


# css
app.layout = html.Div(children=[
    html.H1(children='Meu Dashboard'),

    html.Div(children='''
        Dashboard de Vendas em Python
    '''),
    
    html.H3(children="Vendas de cada Produto por Loja"),
    
    dcc.Graph(id='vendas_por_loja',figure=fig),
    
    
], style={"text-align": "center"})

# callbacks


# colocando o seu site (seu dashboard) no ar
if __name__ == '__main__':
    app.run_server(debug=False)


# #### Adicionar mais um gráfico

# In[22]:


from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd


app = Dash(__name__) # criando o seu aplicativo Dash


# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.read_excel("Vendas.xlsx")

# df = tabela = dataframe

# plotly
fig = px.bar(df, x="Produto", y="Quantidade", color="ID Loja", barmode="group")
fig2 = px.scatter(df, x="Quantidade", y="Valor Final", color="Produto", size="Valor Unitário", size_max=60)

# css
app.layout = html.Div(children=[
    html.H1(children='Meu Dashboard'),

    html.Div(children='''
        Dashboard de Vendas em Python
    '''),
    
    html.H3(children="Vendas de cada Produto por Loja"),
    
    dcc.Graph(id='vendas_por_loja',figure=fig),
    dcc.Graph(id='grafico2', figure=fig2),
    
    
], style={"text-align": "center"})

# callbacks


# colocando o seu site (seu dashboard) no ar
if __name__ == '__main__':
    app.run_server(debug=False)


# #### Inserindo um botão com um callback

# In[23]:


from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd


app = Dash(__name__) # criando o seu aplicativo Dash


# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.read_excel("Vendas.xlsx")

# df = tabela = dataframe

# plotly
fig = px.bar(df, x="Produto", y="Quantidade", color="ID Loja", barmode="group")
fig2 = px.scatter(df, x="Quantidade", y="Valor Final", color="Produto", size="Valor Unitário", size_max=60)


# lista_marcas = ["Treinamentos", "Programação", "Todas"]
lista_marcas = list(df["Marca"].unique())
lista_marcas.append("Todas")

# layout
app.layout = html.Div(children=[
    html.H1(children='Meu Dashboard'),

    html.Div(children='''
        Dashboard de Vendas em Python
    '''),
    
    html.H3(children="Vendas de cada Produto por Loja", id="subtitulo"),
    
    dcc.RadioItems(lista_marcas, value="Todas", id='selecao_marcas'),
    dcc.Graph(id='vendas_por_loja',figure=fig),
    dcc.Graph(id='distribuicao_vendas', figure=fig2),
    
    
], style={"text-align": "center"})

# callbacks -> dar funcionalidade pro nosso dashboard (conecta os botões com os gráficos)
@app.callback(
    Output('subtitulo', 'children'), # eu quero modificar (eu quero que o botão do input modifique)
    Input('selecao_marcas', 'value'), # quem está modificando/de onde eu quero pegar a informacao/que tá fazendo um filtro
)
def selecionar_marca(marca):
    if marca == "Todas":
        texto = "Vendas de cada Produto por Loja"
    else:
        texto = f"Vendas de cada Produto por Loja da Marca {marca}"
    return texto


# colocando o seu site (seu dashboard) no ar
if __name__ == '__main__':
    app.run_server(debug=False)


# #### Autenticação
# 
# - Colocar uma senha no nosso Dashboard

# In[24]:


from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd
import dash_auth

USUARIOS = {
    "Lira": "123456",
    "Hashtag": "98765",
}


app = Dash(__name__) # criando o seu aplicativo Dash
auth = dash_auth.BasicAuth(app, USUARIOS)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.read_excel("Vendas.xlsx")

# df = tabela = dataframe

# plotly
fig = px.bar(df, x="Produto", y="Quantidade", color="ID Loja", barmode="group")
fig2 = px.scatter(df, x="Quantidade", y="Valor Final", color="Produto", size="Valor Unitário", size_max=60)


# lista_marcas = ["Treinamentos", "Programação", "Todas"]
lista_marcas = list(df["Marca"].unique())
lista_marcas.append("Todas")

# layout
app.layout = html.Div(children=[
    html.H1(children='Meu Dashboard'),

    html.Div(children='''
        Dashboard de Vendas em Python
    '''),
    
    html.H3(children="Vendas de cada Produto por Loja", id="subtitulo"),
    
    dcc.RadioItems(lista_marcas, value="Todas", id='selecao_marcas'),
    dcc.Graph(id='vendas_por_loja',figure=fig),
    dcc.Graph(id='distribuicao_vendas', figure=fig2),
    
    
], style={"text-align": "center"})

# callbacks -> dar funcionalidade pro nosso dashboard (conecta os botões com os gráficos)
@app.callback(
    Output('subtitulo', 'children'), # eu quero modificar (eu quero que o botão do input modifique)
    Input('selecao_marcas', 'value'), # quem está modificando/de onde eu quero pegar a informacao/que tá fazendo um filtro
)
def selecionar_marca(marca):
    if marca == "Todas":
        texto = "Vendas de cada Produto por Loja"
    else:
        texto = f"Vendas de cada Produto por Loja da Marca {marca}"
    return texto


# colocando o seu site (seu dashboard) no ar
if __name__ == '__main__':
    app.run_server(debug=False)


# #### Editar com o MESMO botão mais de 1 elemento

# In[ ]:


from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd
import dash_auth

USUARIOS = {
    "Lira": "123456",
    "Hashtag": "98765",
}


app = Dash(__name__) # criando o seu aplicativo Dash
auth = dash_auth.BasicAuth(app, USUARIOS)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.read_excel("Vendas.xlsx")

# df = tabela = dataframe

# plotly
fig = px.bar(df, x="Produto", y="Quantidade", color="ID Loja", barmode="group")
fig2 = px.scatter(df, x="Quantidade", y="Valor Final", color="Produto", size="Valor Unitário", size_max=60)


# lista_marcas = ["Treinamentos", "Programação", "Todas"]
lista_marcas = list(df["Marca"].unique())
lista_marcas.append("Todas")

# layout
app.layout = html.Div(children=[
    html.H1(children='Meu Dashboard'),

    html.Div(children='''
        Dashboard de Vendas em Python
    '''),
    
    html.H3(children="Vendas de cada Produto por Loja", id="subtitulo"),
    
    dcc.RadioItems(lista_marcas, value="Todas", id='selecao_marcas'),
    dcc.Graph(id='vendas_por_loja',figure=fig),
    dcc.Graph(id='distribuicao_vendas', figure=fig2),
    
    
], style={"text-align": "center"})

# callbacks -> dar funcionalidade pro nosso dashboard (conecta os botões com os gráficos)
@app.callback(
    Output('subtitulo', 'children'), # eu quero modificar (eu quero que o botão do input modifique)
    Output('vendas_por_loja', 'figure'),
    Output('distribuicao_vendas', 'figure'),
    Input('selecao_marcas', 'value'), # quem está modificando/de onde eu quero pegar a informacao/que tá fazendo um filtro
)
def selecionar_marca(marca):
    if marca == "Todas":
        texto = "Vendas de cada Produto por Loja"
        fig = px.bar(df, x="Produto", y="Quantidade", color="ID Loja", barmode="group")
        fig2 = px.scatter(df, x="Quantidade", y="Valor Final", color="Produto", size="Valor Unitário", size_max=60)
    else:
        # marca = "Treinamentos"
        # marca = "Programação"
        # filtrar as linhas da tabela onde a marca é igual a variável marca
        df_filtrada = df.loc[df['Marca']==marca, :]
        texto = f"Vendas de cada Produto por Loja da Marca {marca}"
        fig = px.bar(df_filtrada, x="Produto", y="Quantidade", color="ID Loja", barmode="group")
        fig2 = px.scatter(df_filtrada, x="Quantidade", y="Valor Final", color="Produto", size="Valor Unitário", size_max=60)
    return texto, fig, fig2


# colocando o seu site (seu dashboard) no ar
if __name__ == '__main__':
    app.run_server(debug=False)


# #### E se eu tivesse 2 botões editando os mesmos gráficos
# 
# - Filtrar também pelo País

# In[ ]:


from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd
import dash_auth

USUARIOS = {
    "Lira": "123456",
    "Hashtag": "98765",
}


app = Dash(__name__) # criando o seu aplicativo Dash
auth = dash_auth.BasicAuth(app, USUARIOS)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.read_excel("Vendas.xlsx")

# df = tabela = dataframe

# plotly
fig = px.bar(df, x="Produto", y="Quantidade", color="ID Loja", barmode="group")
fig2 = px.scatter(df, x="Quantidade", y="Valor Final", color="Produto", size="Valor Unitário", size_max=60)


# lista_marcas = ["Treinamentos", "Programação", "Todas"]
lista_marcas = list(df["Marca"].unique())
lista_marcas.append("Todas")

lista_paises = list(df["País"].unique())
lista_paises.append("Todos")

# layout
app.layout = html.Div(children=[
    html.H1(children='Meu Dashboard'),

    html.Div(children='''
        Dashboard de Vendas em Python
    '''),
    
    html.H3(children="Vendas de cada Produto por Loja", id="subtitulo"),
    
    dcc.RadioItems(lista_marcas, value="Todas", id='selecao_marcas'),
    html.Div(children=[
        dcc.Dropdown(lista_paises, value="Todos", id='selecao_pais'),
    ], style={"width": "50%", "margin": "auto"}),
    
    dcc.Graph(id='vendas_por_loja',figure=fig),
    dcc.Graph(id='distribuicao_vendas', figure=fig2),
    
    
], style={"text-align": "center"})

# callbacks -> dar funcionalidade pro nosso dashboard (conecta os botões com os gráficos)
@app.callback(
    Output('subtitulo', 'children'), # eu quero modificar (eu quero que o botão do input modifique)
    Output('vendas_por_loja', 'figure'),
    Output('distribuicao_vendas', 'figure'),
    Input('selecao_marcas', 'value'), # quem está modificando/de onde eu quero pegar a informacao/que tá fazendo um filtro
    Input('selecao_pais', 'value'),
)
def selecionar_marca(marca, pais):
    if marca == "Todas" and pais == "Todos":
        texto = "Vendas de cada Produto por Loja"
        fig = px.bar(df, x="Produto", y="Quantidade", color="ID Loja", barmode="group")
        fig2 = px.scatter(df, x="Quantidade", y="Valor Final", color="Produto", size="Valor Unitário", size_max=60)
    else:
        df_filtrada = df
        if marca != "Todas":
            #filtrar de acordo com a marca
            df_filtrada = df_filtrada.loc[df_filtrada['Marca']==marca, :]
        if pais != "Todos":
            # filtrar de acordo com o pais
            df_filtrada = df_filtrada.loc[df_filtrada["País"]==pais, :]
        
        texto = f"Vendas de cada Produto por Loja da Marca {marca} e do País {pais}"
        fig = px.bar(df_filtrada, x="Produto", y="Quantidade", color="ID Loja", barmode="group")
        fig2 = px.scatter(df_filtrada, x="Quantidade", y="Valor Final", color="Produto", size="Valor Unitário", size_max=60)
    return texto, fig, fig2


# colocando o seu site (seu dashboard) no ar
if __name__ == '__main__':
    app.run_server(debug=False)


# #### Botões com opções dinâmicas

# In[ ]:


from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd
import dash_auth

USUARIOS = {
    "Lira": "123456",
    "Hashtag": "98765",
}


app = Dash(__name__) # criando o seu aplicativo Dash
auth = dash_auth.BasicAuth(app, USUARIOS)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.read_excel("Vendas.xlsx")

# df = tabela = dataframe

# plotly
fig = px.bar(df, x="Produto", y="Quantidade", color="ID Loja", barmode="group")
fig2 = px.scatter(df, x="Quantidade", y="Valor Final", color="Produto", size="Valor Unitário", size_max=60)


# lista_marcas = ["Treinamentos", "Programação", "Todas"]
lista_marcas = list(df["Marca"].unique())
lista_marcas.append("Todas")

lista_paises = list(df["País"].unique())
lista_paises.append("Todos")

# layout
app.layout = html.Div(children=[
    html.H1(children='Meu Dashboard'),

    html.Div(children='''
        Dashboard de Vendas em Python
    '''),
    
    html.H3(children="Vendas de cada Produto por Loja", id="subtitulo"),
    
    dcc.RadioItems(options=lista_marcas, value="Todas", id='selecao_marcas'),
    html.Div(children=[
        dcc.Dropdown(options=lista_paises, value="Todos", id='selecao_pais'),
    ], style={"width": "50%", "margin": "auto"}),
    
    dcc.Graph(id='vendas_por_loja',figure=fig),
    dcc.Graph(id='distribuicao_vendas', figure=fig2),
    
    
], style={"text-align": "center"})


@app.callback(
    Output('selecao_pais', 'options'),
    Input('selecao_marcas', 'value'),
)
def opcoes_pais(marca):
    # criar uma lógica que diga qual a lista de paises que ele vai pegar
    if marca == "Todas":
        nova_lista_paises = list(df["País"].unique())
        nova_lista_paises.append("Todos")
    else:
        df_filtrada = df.loc[df['Marca']==marca, :]
        nova_lista_paises = list(df_filtrada["País"].unique())
        nova_lista_paises.append("Todos")
    return nova_lista_paises





# callbacks -> dar funcionalidade pro nosso dashboard (conecta os botões com os gráficos)
@app.callback(
    Output('subtitulo', 'children'), # eu quero modificar (eu quero que o botão do input modifique)
    Output('vendas_por_loja', 'figure'),
    Output('distribuicao_vendas', 'figure'),
    Input('selecao_marcas', 'value'), # quem está modificando/de onde eu quero pegar a informacao/que tá fazendo um filtro
    Input('selecao_pais', 'value'),
)
def selecionar_marca(marca, pais):
    if marca == "Todas" and pais == "Todos":
        texto = "Vendas de cada Produto por Loja"
        fig = px.bar(df, x="Produto", y="Quantidade", color="ID Loja", barmode="group")
        fig2 = px.scatter(df, x="Quantidade", y="Valor Final", color="Produto", size="Valor Unitário", size_max=60)
    else:
        df_filtrada = df
        if marca != "Todas":
            #filtrar de acordo com a marca
            df_filtrada = df_filtrada.loc[df_filtrada['Marca']==marca, :]
        if pais != "Todos":
            # filtrar de acordo com o pais
            df_filtrada = df_filtrada.loc[df_filtrada["País"]==pais, :]
        
        texto = f"Vendas de cada Produto por Loja da Marca {marca} e do País {pais}"
        fig = px.bar(df_filtrada, x="Produto", y="Quantidade", color="ID Loja", barmode="group")
        fig2 = px.scatter(df_filtrada, x="Quantidade", y="Valor Final", color="Produto", size="Valor Unitário", size_max=60)
    return texto, fig, fig2


# colocando o seu site (seu dashboard) no ar
if __name__ == '__main__':
    app.run_server(debug=False)


# In[ ]:


get_ipython().run_line_magic('tb', '')


# In[ ]:




