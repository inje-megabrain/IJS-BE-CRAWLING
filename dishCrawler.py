from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import psycopg2
import datetime
from dotenv import load_dotenv
import os
import time

# load_dotenv()
class DishCrawler:

  def crawl():
    db = psycopg2.connect(host=os.environ.get('DB_ADDRESS'), dbname=os.environ.get('DB_NAME'),user=os.environ.get('DB_USER'),password=os.environ.get('DB_PASSWORD'),port=os.environ.get('DB_PORT'))
    cursor = db.cursor()

    driver = webdriver.Chrome()
    driver.get("https://www.inje.ac.kr/kor/Template/Bsub_page.asp?Ltype=5&Ltype2=3&Ltype3=3&Tname=S_Food&Ldir=board/S_Food&Lpage=s_food_view&d1n=5&d2n=4&d3n=4&d4n=0")

    temporaryDate = datetime.datetime(datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day)
    weekDayCount  = temporaryDate.weekday()
    # 일주일의 시작일(월요일)
    startDate    = temporaryDate+ datetime.timedelta(days=-weekDayCount)

    cursor.execute('DELETE FROM university_dishes') 
    db.commit()
    time.sleeP(1)
    for idx, i in enumerate(range(3, 8)):
      
      try: a = driver.find_element(By.XPATH,'/html/body/main/div/div/article/div/div[2]/div[2]/table/tbody/tr[1]/td['+str(i)+']').text.split()
      except: pass
      try: b = driver.find_element(By.XPATH,'/html/body/main/div/div/article/div/div[2]/div[2]/table/tbody/tr[2]/td['+str(i)+']').text.split()
      except: pass
      try: c = driver.find_element(By.XPATH,'/html/body/main/div/div/article/div/div[2]/div[2]/table/tbody/tr[3]/td['+str(i)+']').text.split()
      except: pass

      data = {
        'id': idx,
        'a_menu': ', '.join(a),
        'b_menu': ', '.join(b),
        'c_menu': ', '.join(c),
        'provide_at': startDate
      }
      startDate += datetime.timedelta(days = 1)

      cursor.execute('INSERT INTO university_dishes (id, a_menu, b_menu, c_menu, provide_at) VALUES (%s, %s, %s, %s, %s)', (data['id'], data['a_menu'], data['b_menu'], data['c_menu'], data['provide_at']))
      db.commit()

    cursor.close()
    db.close()
    driver.close()