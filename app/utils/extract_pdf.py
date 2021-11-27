import pdfplumber

pdf = pdfplumber.open('../../static/pdf/world.pdf')
first_page = pdf.pages[2]
table = first_page.extract_table()

location = None
for index_line, line in enumerate(table):
    for index_i, i in enumerate(line):
        if i == 'Lot Nrs.':
            location = (index_line + 1, index_i)
print(location)
if location:
    data = table[location[0]][location[1]]
    print(data)