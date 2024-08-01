import streamlit as st
from utils import format_number
from graficos import grafico_evadidos_por_curso_ano, grafico_matriculados_por_curso, grafico_ingressantes_por_curso, grafico_diplomados_por_curso, grafico_evadidos_por_curso
from dataset import df_graduacao, df_evadidos_por_curso_ano, df_matriculados_por_curso, df_ingressantes_por_curso, df_diplomados_por_curso, df_evadidos_por_curso

st.set_page_config(layout='wide')

st.title("Dashboard de Graduação UFRGS :desktop_computer:")

st.sidebar.title('Filtros')

with st.sidebar.expander('Cursos de Graduação'):
    filtro_curso = st.multiselect(
        'Selecione os Cursos',
        df_graduacao['NomeCurso'].unique(),
        df_graduacao['NomeCurso'].unique()
    )

with st.sidebar.expander('Ano'):
    filtro_ano = st.multiselect(
        'Selecione os anos',
        df_graduacao['Ano'].unique(),
        df_graduacao['Ano'].unique()
    )

query = '''
    `NomeCurso` in @filtro_curso and \
    Ano in @filtro_ano
'''
df_dados = df_graduacao.query(query)


aba1, aba2, aba3 = st.tabs(['Dataset', 'Totais', 'Comparativo de Evasões'])
with aba1:    
    st.dataframe(df_dados)
    st.markdown(f'A tabela possui :blue[{df_dados.shape[0]}] linhas e :blue[{df_dados.shape[1]}] colunas')

with aba2:        
        st.metric('Total de Matriculados', format_number(df_matriculados_por_curso['Matriculados'].sum()))    
        st.plotly_chart(grafico_matriculados_por_curso, use_container_width=True)

        st.metric('Total de Ingressantes', format_number(df_ingressantes_por_curso['Ingressantes'].sum()))            
        st.plotly_chart(grafico_ingressantes_por_curso)
    
        st.metric('Total de Diplomados', format_number(df_diplomados_por_curso['Diplomados'].sum()))
        st.plotly_chart(grafico_diplomados_por_curso, use_container_width=True)        

        st.metric('Total de Evadidos', format_number(df_evadidos_por_curso['Evadidos'].sum()))            
        st.plotly_chart(grafico_evadidos_por_curso)
        
with aba3:    
    st.plotly_chart(grafico_evadidos_por_curso_ano, use_container_width=True)
