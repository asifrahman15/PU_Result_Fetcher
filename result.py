from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pyautogui import screenshot
import time

def isAlertPresent(driver): 
  try:
    driver.switch_to.alert
    return True 
  except:
    return False

def getAllSemesterResult(driver, registerNumber, semesterfrom, semesterTo, screen):
  allSemResult = {}
  
  for semester in range(semesterfrom, semesterTo + 1):
    regNo = driver.find_element_by_xpath('/html/body/div/div/div[3]/div[1]/div[2]/div[2]/div[1]/input')
    regNo.clear()
    regNo.send_keys(registerNumber)
    sem = Select(driver.find_element_by_xpath('/html/body/div/div/div[3]/div[1]/div[2]/div[2]/div[2]/select'))
    sem.select_by_index(semester)
    driver.find_element_by_xpath('//*[@id="print_app_form"]').click()
    
    
    # Explicit Wait -->
    try:
      wait = WebDriverWait(driver, 1)
      wait.until(EC.alert_is_present())
    except:
      pass
    
    isAlert = isAlertPresent(driver)
    
    if isAlert:
      driver.switch_to.alert.accept()
      print('No Data Found in the semester ' + str(semester) + ' for ' + str(registerNumber))
    
    else:  
      # Explicit Wait -->
      try:
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="result_success_div"]')))
      except:
        pass
      
      maximumSubject = len(driver.find_elements_by_xpath('//*[@id="results_subject_table"]/tbody/tr'))
      for r in range(2, maximumSubject + 1):
        title = driver.find_element_by_xpath('//*[@id="results_subject_table"]/tbody/tr[' + str(r) + ']/td[2]').text
        grade = driver.find_element_by_xpath('//*[@id="results_subject_table"]/tbody/tr[' + str(r) + ']/td[7]').text
        allSemResult[title] = grade
      if screen:
        cover = driver.find_element_by_id('result_success_div')
        driver.execute_script('arguments[0].scrollIntoView();', cover)
        time.sleep(0.1)
        screen = screenshot()
        screen.save('Screenshots/' + str(registerNumber) + ' ' + str(semester) + '.png')
      driver.find_element_by_xpath('//*[@id="main_frame"]/div/div[2]/div[2]').click()

  return allSemResult, driver