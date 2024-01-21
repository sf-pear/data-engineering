# Docker

| Description                                | Command                                      |
| ------------------------------------------ | -------------------------------------------- |
| Build image in current folder              | `docker build -t <image-name>:<image-tag> .` |
| Run image as container (interactive)       | `docker run -it <image-name>:<image-tag>`    |
| Run container in the background (detached) | `docker run -d <image-name>:<image-tag>`     |
| Create new volume                          | `docker volume create <volume-name>`         |
| Check running containers                   | `docker ps`                                  |
| Run docker-compose file                    | `docker-compose up`                          |
| Retrieve detailed container info           | `docker container inspect`                     |


# Postgres

| Description  | Command                                            |
| ------------ | -------------------------------------------------- |
| List tables  | `\dt`                                              |
| Delete table | `DROP TABLE table_name`                            |
| Rename table | `ALTER TABLE table_name RENAME TO new_table_name;` |

## pgcli

A postgres client that does auto-completion and syntax highlighting.

`pgcli -h localhost -p 5432 -u root -d <db-name>`

# SQL

| Description   | Command                           |
| ------------- | --------------------------------- |
| Count records | `SELECT count(1) FROM table_name` |