##List Codes

####https://www.vooo.pro/insights/guia-para-iniciantes-de-web-scraping-em-python-usando-beautifulsoup/



```
# int_str_float - tranforma type
# new_df['Valor Empenhado (R$)'].astype('str')
# new_df['Valor Empenhado (R$)'] = new_df['Valor Empenhado (R$)'].str.lower().str.replace(',', '.')
# new_df['Valor Empenhado (R$)'].astype('float') italicized text
```



=====================

plot = size
plt.rcParams['figure.figsize'] = (8,5)

=================
Read DF

x = []
with open('drive/My Drive/2019/Files_Colab/201904_Despesas.csv', 'r', encoding='latin-1') as f:
  for linha in f.readlines():
    #print(linha)
    x.append(linha.replace('\n', '').split(';')) #linha.replace('\n', '').split(',')
    
header = x[0]
del(x[0])

y = []
for a in x:
  #print(a)
  y.append(a)
  
dfA = pd.DataFrame(data=y)


dfB = dfA[np.arange(0,len(header),1)]

for a in range(len(header)):
  dfB.rename(columns={a:header[a]}, inplace=True)
  
dfB.head(3)

=================
plt.rcParams['figure.figsize'] = (11,7)
matplotlib, aumentar
--------------------------------
#### Acrescentar linhas

dados = [  ['CC-100000-00001-11-001','CTE00000001','ABC_TESTES','BB00001',''],
            ['CC-100000-00001-11-001','CTE00000002','ABC_TESTES','BB00001',''],
            ['CC-100000-00001-11-002','CTE00000002','ABC_TESTES','BB00002',''],
        ]
header = ['CC','CTE','TIPO','IM','NOTA']
df = pd.DataFrame(data=dados, columns=header)

df

dados2 = [  ['CC-100000-00001-11-00x','CTE0000000x','ABC_TESTES','BB0000x','']
     
        ]

header2 = ['CC','CTE','TIPO','IM','NOTA']
df2 = pd.DataFrame(data=dados2, columns=header2)
df2

new = df.append(pd.concat([df2]))
new

#### Muda valores de umacoluna

new_df = df['Atrito'].replace(['Yes', 'No'], [0, 1])



#### Mudar uma coluna baseada em outra
==============
conta = 0

for a in New_Bolo['Ingrediente']:
    print(a , '= Posição ', conta)
    if a == 'Ovo': #Palavra procurada
      New_Bolo['Qt2'].iloc[conta] =  new  #novo arguemnto
    conta = conta + 1
    
====================   

Python Comands
--------------------------------
#### Where
cont = 0
for a in df['CTE']:
  test1 = df2[df2['CTE'] == a]
  print(a)
  print(test1['CTE'])
  
  if test1.index != 0:
    print('ok')
    if df2.loc[df2[df2['CTE'] == a].index[0]][1] == a:
      df.set_value(cont, 'RESULT', 'OK')
    else:
      df.set_value(cont, 'RESULT', 'N')
  else:
    print('nnnnnnn')

  cont+= 1
 -------------------------------
 cont = 0

for a in df['CTE']:
  print('A: ', a)
  cc_use = df[df['CTE'] == a]['NOTA']
  for i in cc_use:
    print('USE: ', i)
    cc_use2 = df2[df2['CC'] == i]
    cc_use2 = cc_use2[cc_use2['CTE'] == a]['CTE']
    for z in cc_use2:
      print('Resultado Final: ', z)
      if df2.loc[df2[df2['CTE'] == a].index[0]][1] == a: #Se dataframe 2 tiver o CTE desejado, escreve na celula de RESULT = OK
        df.set_value(cont, 'RESULT', 'OK')
      else:
        df.set_value(cont, 'RESULT', 'N')
        
  cont+= 1
 -------------------------------
 
 ####Localizar texto dentro de uma string
 nome = 'SMB-316199'

for a in dados['Caminho'].head(20):
  print(a)
  if re.search('\\{}\\b'.format(nome), a, re.IGNORECASE):
    print("Ok")
    print(a)



 ####Contar itens de uma coluna
df.groupby('coluna').count()

df.groupby('COL').COL.count()

df.groupby('coluna').count().index # Ver valores únicos
 
 -----------------------
 ####Alterar Index
 importing pandas as pd 
import pandas as pd 
  
Creating the index 
idx = pd.Index(['Jan', 'Feb', 'Mar', 'Apr', 'May']) 
  
# Print the index 
print(idx) 
 --------------------
 
####Ordenar por Coluna
df.sort_values(by="Prova")

####Somatório Geral
df.groupby("Aluno").mean()

####Somatório de Itens por coluna
df["Seminario"].value_counts()
 
####Criar arquivo.csv ou xlsl
df.to_csv

####Excluindo Colunas
df.drop('Nova Coluna', axis=1)



####Exluindo Linha Por Index
df.drop([0, 1]) 

####Ordenar por Coluna
df.sort_values(by="Prova")

####Selecionar linhas específicas
df.loc[[0,1,2]]

####Nova coluna
df['Nova'] = np.nan

####Comparar data framesConcatenar Colunas por [emerge] combina - concatena
result = df_app.merge(df_epm, on='CMX')

####Renomear Colunas
data.rename(columns={'gdp':'log(gdp)'}, inplace=True)

####Selecionar Item específico de Coluna Específica
df['Aluno'].loc[3]

####Cortar coluna
df.drop(['coluna1'], axis=1, inplace=True)

####Concatenar colunas
dados = pd.concat([df, sex], axis=1)

####Substituir valores NaN por outro
df.fillna('-')
#ddf = df.dropna()

####Ler só em cima ou só em baixo de um dataframe
df.tail()
df.head()

####transformar colunas em novas colunas 0 ou 1 
newcolum = pd.get_dummies(df['sex'], drop_first=True)

####Verificar tipo de sistema de predição aplicar
sns.pairplot(suicide)

####Concatenar Data Frames
pd.concat([new_df, new_df])
outra
Frame = Frame.append(pandas.DataFrame(data = SomeNewLineOfData), ignore_index=True)

####renumerar index
for a in df.index:
  print(a)
  df.rename(index={a:0}, inplace=True)
  
  df.index = pd.Index(np.arange(0,len(df)))
 
##### Contagem Index
df.index.size

#####Descobrir o index
f2[df2['CTE'] == a].index[0]

####Nomear Index Coluna
df.index.names = ['ID']

####renomerar index
df.rename(index={'0':'ID'})

####setar index em uma coluna
dd = df.set_index('Number(Related product lot(s))')

####Concatenar Colunas
pd.concat([n, siecc], axis=1)

####Filtros
Teste_EQ = EQ[EQ['CC de Montagem'] == Nome_CC]

####Alterar valores de uma coluna, baseado em outra
def relaciona(cols): reavaliar...
  Col_qt = cols['Quantity provided(Product)']
  Col_OBS = cols['OBSERVAÇÃO']
 
  if pd.isnull(Col_qt)
    if Col_OBS != '':
      return '1'
    else:
      return Col_qt
  else:
    return Col_qt

LMA['OBSERVAÇÃO'] = LMA[['OBSERVAÇÃO', 'Mass (kg) (Item).1']].apply(relaciona, axis=1)

####pegar pedaços de uma String
for a in LMA['Number(Related product lot(s))']:
  print(len(a))
  print(a)
  print(a[4::])

####Querry
df[(df["Seminario"] > 8.0) & (df["Prova"] > 3)]
df[(df["Aluno"] == "Harry") & (df["Prova"] == 5)]

####Pegar letras da direta ou da esquerda de uma string
df[-3::]
todo dataframe
conta = 0
for local in LMA['Number(Related product lot(s))']:
  LMA['Number(Related product lot(s))'].iloc[conta] = local[4::]
  conta = conta + 1

####Datas
import pandas as pd
df = pd.read_csv('DataFrame.csv', delimiter=";");

df['Data e Hora'] = pd.to_datetime(df['Data e Hora'])
df['Data'] = df['Data e Hora'].dt.strftime('%Y-%m-%d')
df['Hora'] = df['Data e Hora'].dt.strftime('%H:%M:%S')

del df['Data e Hora']
df = df[['Data', 'Hora', 'Consumo(litros)', 'Valor Acumulado']]

print(df)

Append em for
for i in Teste_EQ['Industrial Mark']:
  new_df = LMA_Construction[LMA_Construction['Number(Related product lot(s))'] == '53A' + i]
  #print(new_df)
  df = df.append(pd.concat([new_df]))

df


http://blog.alura.com.br/lidando-com-datas-e-horarios-no-python/
==========================
