from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import psycopg2
import re
from dotenv import load_dotenv
import os
import time

load_dotenv()
class MajorNoticeCrawler:
  def crawl():
    db = psycopg2.connect(host=os.environ.get('DB_ADDRESS'), dbname=os.environ.get('DB_NAME'),user=os.environ.get('DB_USER'),password=os.environ.get('DB_PASSWORD'),port=os.environ.get('DB_PORT'))
    cursor = db.cursor()

    driver = webdriver.Chrome()
    driver.get("https://cs.inje.ac.kr/공지사항/")
    idx = cursor.callproc('SELECT COUNT(0) FROM university_notice')
    time.sleep(1)
    bodys = driver.find_elements(By.CLASS_NAME, "kboard-list-notice")
    for idx, body in enumerate(bodys):
      url = body.find_element(By.CLASS_NAME, "kboard-list-title").find_element(By.TAG_NAME, "a").get_attribute("href")
      data = {
        'id': idx,
        'notice_id': int(re.search("uid=(\d+)", url).group(1)),
        'title': body.find_element(By.CLASS_NAME, "kboard-list-title").text,
        'author_nickname': body.find_element(By.CLASS_NAME, "kboard-list-user").text,
        'write_at': body.find_element(By.CLASS_NAME, "kboard-list-date").text,
        'category': '컴공'
      }

      cursor.execute('INSERT INTO university_notice (id, notice_id, title, author_nickname, write_at, category) VALUES (%s, %s, %s, %s, %s, %s)', (data['id'], data['notice_id'], data['title'], data['author_nickname'], data['write_at'], data['category']))

    db.commit()
    cursor.close()
    db.close()
      


      