import openpyxl                 # To work with Excel Files
from os import path, makedirs, getcwd

def getSheet():                 # To get the The Input Sheet
  count = 5                     # To avoid Infinite try maximum count is mentioned
  while count >= 0:
    try:
      print('Please read the Readme for any assistancy')
      fileName = input('Enter the sheet name : ')
      path1 = input('Enter the sheet directory (leave blank if it is in current directory) : ')
      if path1 :
        filePath = path1 + '/' + fileName
      else :
        filePath = fileName
      wb = openpyxl.load_workbook(filePath)
      path2 = input('Enter the "chromedriver" application directory (leave blank if it is in current directory) : ')
      if path2 :
        chromePath = path2 + '/chromedriver'
      else :
        chromePath = getcwd() + '/chromedriver'

      return wb, wb.active, filePath, chromePath
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
    if not path.exists('Screenshots'):
      makedirs('Screenshots')
    print('Screenshot is Enabled...!')
  else :
    screen = False
    print('Screenshot is Disabled...!')
  return semfrom, semto, col, start, end, screen
  