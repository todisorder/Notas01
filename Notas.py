import xlsxwriter as xl

workbook = xl.Workbook('demo.ods')
# o libre office não lê isto...
worksheet = workbook.add_worksheet()

# Widen the first column to make the text clearer.
worksheet.set_column('A:A', 20)

# Write some simple text.
worksheet.write('A1', 'Hello')

# Write some numbers, with row/column notation.
worksheet.write(2, 0, 123)
worksheet.write(3, 0, 123.456)

worksheet.write_formula('A1', '=SUM(1, 2, 3)')


workbook.close()
