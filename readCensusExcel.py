import openpyxl, pprint
print('Opening workbook... ')
wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb['Population by Census Tract']
county_data = {}
print('reading rows...')
for row in range (2, sheet.max_row + 1):
    state = sheet['B' + str(row)].value
    county = sheet['C' + str(row)].value
    pop = sheet['D'  + str(row)].value

    #make sure the key for this state exists
    county_data.setdefault(state,{})
    #make sure the key for this county in this state exists
    county_data[state].setdefault(county, {'tracts':0, 'pop': 0})

    #each row represents one census tract, os increment by one.
    county_data[state][county]['tracts'] += 1
    #increase the county pop by the pop in this census tract
    county_data[state][county]['pop'] += int(pop)

    #open a new text file and write the contents of tcounty_data to it
print('writing results ... ')
result_file = open('census2010.py', 'w')

#this will make importable python program
result_file.write('allData = ' + pprint.pformat(county_data))
result_file.close()
print('Done.')