import openpyxl

# carregando a planilha do Excel
book = openpyxl.load_workbook('candidatos.xlsx')

# selecionando página para dep. federal
dep_federal_page = book['dep-federal']

# imprimindo todos os candidatos
for rows in dep_federal_page.iter_rows(min_row=1, max_row=215):
    print(rows[0].value, rows[1].value)
