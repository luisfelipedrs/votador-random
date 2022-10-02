import openpyxl

# carregando a planilha do Excel
book = openpyxl.load_workbook('candidatos.xlsx')

# selecionando página para dep. federal
dep_federal_page = book['dep-federal']
