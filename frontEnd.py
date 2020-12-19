from flask import Flask, render_template, request, redirect
from os import path, makedirs, getcwd
import openpyxl
from selenium import webdriver

from backEnd import puResult

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
  if request.method == 'GET':
    return render_template('index.html')
  elif request.method == 'POST':
    fileName = request.form['sheetName']
    filePath = request.form['filePath']
    webdriverPath = request.form['webdriverPath']
    column = int(request.form['column'])
    rowFrom = int(request.form['rowFrom'])
    semFrom = int(request.form['semFrom'])
    if bool(request.form['rowTo']):
      rowTo = int(request.form['rowTo'])
    else:  
      rowTo = rowFrom
    if bool(request.form['semTo']):
      semTo = int(request.form['semTo'])
    else:
      semTo = semFrom
    
    
    
    screenCap = bool(request.form.get('screenshot'))
    
    try:
      if filePath:
        filePath = filePath + '/' + fileName
      else:
        filePath = fileName
      wb = openpyxl.load_workbook(filePath)
    except:
      return render_template('index.html', message='Please check the sheet path carefully and Try again...', mode='danger')
    
    try:
      if webdriverPath:
        webdriverPath = webdriverPath + '/chromedriver'
      else:
        webdriverPath = getcwd() + '/chromedriver'
        driver = webdriver.Chrome(executable_path = webdriverPath)
    except:
      return render_template('index.html', message='Please check the webdriver path carefully and Try again...', mode='danger')

    if screenCap == True and not path.exists('Screenshots'):
      makedirs('Screenshots')
    try:  
      newCols = puResult(wb, wb.active, filePath, driver, column, rowFrom, rowTo, semFrom, semTo, screenCap)
      return render_template('index.html', message='Successfully all the results are fetched...', mode="success", listed=newCols)
    except:
      return render_template('index.html', message='Some error occured please restart the app and Try again....', mode='danger')

def shutdown_server():
  func = request.environ.get('werkzeug.server.shutdown')
  if func is None:
      raise RuntimeError('Not running with the Werkzeug Server')
  func()
    
@app.route('/shutdown', methods=['GET'])
def shutdown():
  shutdown_server()
  return render_template('shutdown.html')

if __name__ == '__main__':
  app.run(debug = False)