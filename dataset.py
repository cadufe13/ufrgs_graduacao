import json
import pandas as pd

file = open('dados/vendas.json')
data = json.load(file)

df = pd.DataFrame.from_dict(data)

df['Data da Compra'] = pd.to_datetime(df['Data da Compra'], format='%d/%m/%Y')

file.close()

df_graduacao = pd.read_csv("dados/dadosabertos_graduacao_quantitativo-de-alunos.csv", sep = ';')


df_evadidos_por_curso_ano = df_graduacao.set_index('Ano').groupby(['NomeCurso', 'Ano'])['Evadidos'].sum().reset_index()
df_evadidos_por_curso_ano = df_evadidos_por_curso_ano.loc[df_evadidos_por_curso_ano['NomeCurso'].isin(['ADMINISTRAÇÃO', 'CIÊNCIA DA COMPUTAÇÃO', 'ESTATÍSTICA', 'MEDICINA', 'TEATRO'])]

df_matriculados_por_curso = df_graduacao.set_index('NomeCurso').groupby('NomeCurso')[['Matriculados']].sum().sort_values('Matriculados', ascending=False).reset_index()

df_ingressantes_por_curso = df_graduacao.set_index('NomeCurso').groupby('NomeCurso')[['Ingressantes']].sum().sort_values('Ingressantes', ascending=False).reset_index()

df_evadidos_por_curso = df_graduacao.set_index('NomeCurso').groupby('NomeCurso')[['Evadidos']].sum().sort_values('Evadidos', ascending=False).reset_index()

df_diplomados_por_curso = df_graduacao.set_index('NomeCurso').groupby('NomeCurso')[['Diplomados']].sum().sort_values('Diplomados', ascending=False).reset_index()



