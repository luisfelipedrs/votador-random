import openpyxl
import random

# carregando a planilha do Excel
book = openpyxl.load_workbook('candidatos.xlsx')


# imprimir todos os candidatos(separados por cargo)
def imprimir_todos(lista_candidatos):
    page = book[lista_candidatos]
    for rows in page.iter_rows():
        print(rows[0].value, rows[1].value)


# imprimir todos os candidatos a deputado federal
def imprimir_dep_federal():
    page = book['dep-federal']
    for rows in page.iter_rows():
        print(rows[0].value, rows[1].value)


# sortear um candidato a dep. federal
def sortear_dep_federal():
    page = book['dep-federal']
    random_index = random.randint(1, page.max_row)
    for rows in page.iter_rows(min_row=random_index, max_row=random_index):
        print(rows[0].value, rows[1].value)


# imprimir todos os candidatos a presidente
def imprimir_presidente():
    page = book['presidente']
    for rows in page.iter_rows():
        print(rows[0].value, rows[1].value)


# sortear um candidato a presidente
def sortear_presidente():
    page = book['presidente']
    random_index = random.randint(1, page.max_row)
    for rows in page.iter_rows(min_row=random_index, max_row=random_index):
        print(rows[0].value, rows[1].value)


sortear_presidente()
sortear_dep_federal()
