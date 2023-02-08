from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.base import JobLookupError
from dishCrawler import DishCrawler
from nonSubjectCrawler import NonSubjectCrawler
from majorNoticeCrawler import MajorNoticeCrawler
from universityNoticeCrawler import UniversityNoticeCrawler

import time


class Scheduler:
  def __init__(self):
    print("Scheduler init")
    self.sched = BackgroundScheduler()
    self.sched.start()
    
    self.sched.add_job(DishCrawler.crawl(), 'cron', hour=0, id="test_1")
    self.sched.add_job(NonSubjectCrawler.crawl(), 'cron', hour=0, id="test_2")
    self.sched.add_job(MajorNoticeCrawler.crawl(), 'cron', hour=0, id="test_3")
    self.sched.add_job(UniversityNoticeCrawler.crawl(), 'cron', hour=0, id="test_4")
