import * as dotenv from 'dotenv';
import { DataSource, DataSourceOptions } from 'typeorm';
import { SnakeNamingStrategy } from 'typeorm-naming-strategies';

dotenv.config();

export const dataSourceConfig: DataSourceOptions = {
  type: 'postgres',
  host: process.env.DB_HOST || '',
  port: parseInt(process.env.DB_PORT) || 5432,
  database: process.env.DB_DATABASE || 'ijs_server',
  username: process.env.DB_USERNAME || 'ijs_user',
  password: process.env.DB_PASSWORD || 'mega123!@#',
  entities: ['dist/**/*.entity.js'],
  migrations: ['dist/migrations/**/*.js'],
  namingStrategy: new SnakeNamingStrategy(),
  synchronize: false,
  migrationsRun: true,
};

export const dataSource = new DataSource(dataSourceConfig);