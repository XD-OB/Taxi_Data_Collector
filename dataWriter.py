import os
import datetime
import xlsxwriter as xls


def print_result(dic):

# Open files:

    rep = datetime.datetime.now().strftime("%Y_%b_%d")
    fich = datetime.datetime.now().strftime("%l%p")

    access_rights = 0o755
    if not os.path.exists("%s" % rep):
        os.makedirs("%s" % rep, access_rights)

# Create the Book:
    wBook = xls.Workbook("./%s/file_%s.xlsx" % (rep, fich))

# Create the Sheet:
    wSheet = wBook.add_worksheet()

# Set cases:
    wSheet.set_column('A:Z', 35)
    wSheet.set_row('0:50', 30)

# Format in merge cases:
    m_format = wBook.add_format({
        'bold': 2,
        'border': 2,
        'border_color' : 'gray',
        'align': 'center',
        'valign': 'vcenter',
        'fg_color': '#00ffbf'})

# Merge cells:
    wSheet.merge_range('A1:H1', datetime.datetime.now().strftime("%A %B %Y    %X %z"), m_format)
    wSheet.merge_range('C3:H3', 'Prix', m_format)


# Start from the first cell and write data:
    tab = ['Depart', 'Destination', 'Lecab', 'Uber Green', 'Uber UberX', 'Uber berline', 'Uber Van', 'Uber ACCESS']

    row = 3
    col = 0
    for item in tab:
        wSheet.write(row, col, tab[col], m_format)
        col +=1
    row += 1
    for i in range(0,10):
        col = 0
        wSheet.write(row, col, dic[i]["Depart"], m_format)
        col += 1
        wSheet.write(row, col, dic[i]["Destination"], m_format)
        col += 1
        wSheet.write(row, col, dic[i]["Lecab"], m_format)
        col += 1
        wSheet.write(row, col, dic[i]["Green"], m_format)
        col += 1
        wSheet.write(row, col, dic[i]["UberX"], m_format)
        col += 1
        wSheet.write(row, col, dic[i]["Berline"], m_format)
        col += 1
        wSheet.write(row, col, dic[i]["Van"], m_format)
        col += 1
        wSheet.write(row, col, dic[i]["ACCESS"], m_format)
        row += 1


# Close the book
    wBook.close()
