import streamlit as st

st.title("Dataset")
st.markdown(f"""Quantitativo de Alunos de Graduação UFRGS

Fonte: [Quantitativo de Alunos de Graduação](https://dados.ufrgs.br/dataset/quantitativo-de-alunos-de-graduacao)

**Colunas**
                        
* `CodCurso`: `Inteiro` Código do curso
* `NomeCurso`: `Texto` Nome do curso
* `Ano`: `Inteiro` Ano do período letivo de referência
* `Periodo`: `Inteiro` Semestre do período letivo de referência
* `Vinculados`: `Inteiro` Número de alunos que possuem vínculo ativo no curso de graduação no período letivo de referência. O aluno pode estar matriculado, em trancamento, em licença, etc.
* `Matriculados`: `Inteiro` Número de alunos que estão matriculados em pelo menos uma atividade de ensino do curso de graduação, inclusive em mobilidade acadêmica, no período letivo de referência
* `Ingressantes`: `Inteiro` Número de alunos ingressantes em processos seletivos (vestibular, transferência interna, ingresso diplomado, etc.) que efetivaram matrícula por curso no período letivo de referência
* `Diplomados`: `Inteiro` Número de alunos que, após a conclusão de todos os créditos acadêmicos, apresentaram registro de diplomação por curso no período letivo de referência
* `Evadidos`: `Inteiro` Número de alunos que se desligaram por abandono, desistência de vaga, falecimento, transferência interna ou outras formas de saída por curso de graduação no período letivo de referência            

**Estatísticas básicas dos dados**
* Número de atributos: 9
* Quantidade de registros: 2.134""")