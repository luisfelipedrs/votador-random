import openpyxl
import random

# carregando a planilha do Excel
book = openpyxl.load_workbook('candidatos.xlsx')

# selecionando página para dep. federal
dep_federal_page = book['dep-federal']


# imprimindo todos os candidatos(separados por cargo)
def imprimir_todos(lista_candidatos):
    global page
    if lista_candidatos == 'dep-federal':
        page = book['dep-federal']

    if lista_candidatos == 'presidente':
        page = book['presidente']

    for rows in page.iter_rows(min_row=1, max_row=200):
        print(rows[0].value, rows[1].value)


imprimir_todos('dep-federal')