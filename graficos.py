import plotly.express as px
from dataset import df_evadidos_por_curso_ano, df_matriculados_por_curso, df_ingressantes_por_curso, df_diplomados_por_curso, df_evadidos_por_curso

grafico_evadidos_por_curso_ano = px.line(
    df_evadidos_por_curso_ano,
    x = 'Ano',
    y = 'Evadidos',
    markers = True,
    range_y = (0, df_evadidos_por_curso_ano.max()),
    color = 'NomeCurso',
    line_dash = 'NomeCurso',
    title = 'Evadidos por ano'
)

grafico_evadidos_por_curso_ano.update_layout(yaxis_title = 'Quantidade de Evasões')

grafico_matriculados_por_curso = px.bar(
    df_matriculados_por_curso.head(7),    
    x = 'Matriculados',
    y = 'NomeCurso',    
    text_auto = True,
    title = 'Cursos com mais matriculados'
)

grafico_ingressantes_por_curso = px.bar(
    df_ingressantes_por_curso.head(7),    
    x = 'Ingressantes',
    y = 'NomeCurso',
    text_auto = True,
    title = 'Cursos com mais ingressantes'
)

grafico_diplomados_por_curso = px.bar(
    df_diplomados_por_curso.head(7),    
    x = 'Diplomados',
    y = 'NomeCurso',    
    text_auto = True,
    title = 'Cursos com mais diplomados'
)

grafico_evadidos_por_curso = px.bar(
    df_evadidos_por_curso.head(7),    
    x = 'Evadidos',
    y = 'NomeCurso',
    text_auto = True,
    title = 'Cursos com mais evadidos'
)