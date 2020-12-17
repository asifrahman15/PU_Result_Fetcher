import openpyxl                 # To work with Excel Files
from os import getcwd

def getSheet():                 # To get the The Input Sheet
  count = 5                     # To avoid Infinite try maximum count is mentioned
  while count >= 0:
    try:
      fileName = input('Please Enter the Sheet Name (Please have the sheet in Current Directory) : ')
      path = getcwd() + '/' + fileName
      wb = openpyxl.load_workbook(path)

      return wb, wb.active, fileName
    except:
      print('Please check the path carefully and try again ' + str(count) + ' chances left...')
      count -= 1

def getRegNoData():
  col = int(input('The column Number in which the list of Register numbers are there : '))
  start = int(input('The Row from the Register Number Start : '))
  end = int(input('The Row in the Register Number Ends : '))
  semfrom = int(input('From which Semester : '))
  semto = int(input('Until which Semester : '))
  screeninp = input('Need Screenshots (yes/no): ').lower()
  if screeninp == 'yes':
    screen = True
    print('Screenshot is Enabled...!')
  else :
    screen = False
    print('Screenshot is Disabled...!')
  return semfrom, semto, col, start, end, screen
  