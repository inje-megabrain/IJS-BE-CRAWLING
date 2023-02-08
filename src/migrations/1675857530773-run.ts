import { MigrationInterface, QueryRunner } from "typeorm";

export class run1675857530773 implements MigrationInterface {
    name = 'run1675857530773'

    public async up(queryRunner: QueryRunner): Promise<void> {
        await queryRunner.query(`
            CREATE TABLE "university_nonsubjects" (
                "id" character varying NOT NULL,
                "title" character varying NOT NULL,
                "content_url" character varying NOT NULL,
                "end_at" date NOT NULL,
                CONSTRAINT "PK_ce17cc6c80c2504654aa5dbfbbe" PRIMARY KEY ("id")
            )
        `);
        await queryRunner.query(`
            CREATE TABLE "university_schedule" (
                "id" character varying NOT NULL,
                "title" character varying NOT NULL,
                "start_at" TIMESTAMP NOT NULL,
                "end_at" TIMESTAMP NOT NULL,
                "is_start_date" boolean NOT NULL DEFAULT false,
                "is_end_date" boolean NOT NULL DEFAULT false,
                CONSTRAINT "PK_fd7ef47145b55698ae108887c5b" PRIMARY KEY ("id")
            )
        `);
        await queryRunner.query(`
            CREATE TABLE "university_notice" (
                "id" character varying NOT NULL,
                "notice_id" integer NOT NULL,
                "title" character varying NOT NULL,
                "author_nickname" character varying NOT NULL,
                "write_at" TIMESTAMP NOT NULL,
                CONSTRAINT "PK_fba537fe7d5cd081cec81149e56" PRIMARY KEY ("id", "notice_id")
            )
        `);
    }

    public async down(queryRunner: QueryRunner): Promise<void> {
        await queryRunner.query(`
            DROP TABLE "university_notice"
        `);
        await queryRunner.query(`
            DROP TABLE "university_schedule"
        `);
        await queryRunner.query(`
            DROP TABLE "university_nonsubjects"
        `);
    }

}
