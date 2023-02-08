from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()
class UniversityNoticeCrawler:
  def crawl():
    db = psycopg2.connect(host=os.environ.get('DB_ADDRESS'), dbname=os.environ.get('DB_NAME'),user=os.environ.get('DB_USER'),password=os.environ.get('DB_PASSWORD'),port=os.environ.get('DB_PORT'))
    cursor = db.cursor()

    driver = webdriver.Chrome()
    driver.get("https://www.inje.ac.kr/kor/Template/Bsub_page.asp?Ltype=5&Ltype2=0&Ltype3=0&Tname=S_News&Ldir=board/S_News&SearchText=&SearchKey=&d1n=5&d2n=1&d3n=1&d4n=0&Lpage=Tboard_L&div=1")
    # idx 초기값 설정 필요
    
    idx = cursor.callproc('SELECT COUNT(0) FROM university_notice')
    bodys = driver.find_element(By.CLASS_NAME, "b-list").find_element(By.TAG_NAME, "tbody").find_elements(By.TAG_NAME, "tr")
    for body in bodys:
      data = {
        'id': idx,
        'notice_id': body.find_element(By.CLASS_NAME, "num").text,
        'title': body.find_element(By.CLASS_NAME, "subject").text,
        'author_nickname': body.find_element(By.CLASS_NAME, "writer").text,
        'write_at': body.find_element(By.CLASS_NAME, "date").text,
        'category': '일반'
      }
      idx += 1

      cursor.execute('INSERT INTO university_notice (id, notice_id, title, author_nickname, write_at, category) VALUES (%s, %s, %s, %s, %s, %s)', (data['id'], data['notice_id'], data['title'], data['author_nickname'], data['write_at'], data['category']))

      db.commit()

    driver.find_element(By.XPATH, "/html/body/main/div/div/article/div/div[2]/div[2]/ul/li[3]/a").click()
    bodys = driver.find_element(By.CLASS_NAME, "b-list").find_element(By.TAG_NAME, "tbody").find_elements(By.TAG_NAME, "tr")
    for body in bodys:
      data = {
        'id': idx,
        'notice_id': body.find_element(By.CLASS_NAME, "num").text,
        'title': body.find_element(By.CLASS_NAME, "subject").text,
        'author_nickname': body.find_element(By.CLASS_NAME, "writer").text,
        'write_at': body.find_element(By.CLASS_NAME, "date").text,
        'category': '학사'
      }
      idx += 1

      cursor.execute('INSERT INTO university_notice (id, notice_id, title, author_nickname, write_at, category) VALUES (%s, %s, %s, %s, %s, %s)', (data['id'], data['notice_id'], data['title'], data['author_nickname'], data['write_at'], data['category']))

      db.commit()

    cursor.close()
    db.close()
      


      