import {Controller, Post} from '@nestjs/common';

@Controller('crawler')
export class CrawlerController {
  constructor() {
  }

  @Post()
  async crawlUniversitySchedule() {
  }

  @Post()
  async crawlUniversityNotices() {
  }

  @Post()
  async crawlUniversityNonsubjectClass() {
  }
}
