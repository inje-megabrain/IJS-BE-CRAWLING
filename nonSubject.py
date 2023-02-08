from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import psycopg2
import re

db = psycopg2.connect(host='3.38.102.66', dbname='ijs_server',user='ijs_user',password='',port=5432)
cursor = db.cursor()

driver = webdriver.Chrome()
driver.get("https://edu.inje.ac.kr/AllUsers/PreProgramList.aspx")


_class = driver.find_element(By.CLASS_NAME, "tab-list")
classes = _class.find_elements(By.TAG_NAME, "li")

for idx,i in enumerate(classes):
  classA = i.find_element(By.CLASS_NAME, "tit").text.split('\n')
  classB = i.find_element(By.CLASS_NAME, "btn-group")
  classBB = str(classB.find_element(By.CLASS_NAME, "btn-info").get_attribute("onclick"))
  datas = classA + [re.search("\('(.*?)'", classBB).group(1)]
  lastData = {
    'id': idx,
    'title': datas[2],
    'content_url': datas[4],
    'end_at': datas[3].split(' ~ ')[1],
  }

  cursor.execute('INSERT INTO university_nonsubjects (id, title, content_url, end_at) VALUES (%s, %s, %s, %s)', (lastData['id'], lastData['title'], lastData['content_url'], lastData['end_at']))
    
  print()
db.commit()
cursor.close()
db.close()

#   print(_class.get_property)
#   print(_class.text)
#   # print(_class.find_element(By.CLASS_NAME, "txt").text)
#   # print(_class.find_element(By.CLASS_NAME, "date").text)
#   # print(_class.find_element(By.CLASS_NAME, "btn btn-info").find_element().getAttribute("onclick"))
#   print()



    

# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
driver.close()
