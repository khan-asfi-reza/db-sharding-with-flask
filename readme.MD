# URL Shortener 
## Database Sharding Example With Flask

For Database Sharding Demonstration Purpose, this project was built. For database, I have used Postgres and to shard and create multiple instance
I have used Docker. Flask is used to demonstrate the application that will be used with the database

# Used:

1. Flask
2. Postgres
3. Docker

## Installation Step

### 1. Install Docker, Python

> Install Python and Docker in your local machine

[Docker](https://www.docker.com/products/docker-desktop) ||
[Python](https://www.python.org)

### 2. Clone This Repo
```bash
git init
git clone https://github.com/khan-asfi-reza/db-sharding-with-flask.git
```

### 3. Setup Database Using Docker
We will use the following image for our Database Nodes
```bash
cd postgres
docker build -t mypostgres .
```
Now we will create 3 Database Node / Server with 3 different ports

```bash
docker run --name node1 -p 5432:5432 -e POSTGRES_PASSWORD='postgres' -d mypostgres
docker run --name node2 -p 5433:5432 -e POSTGRES_PASSWORD='postgres' -d mypostgres
docker run --name node3 -p 5434:5432 -e POSTGRES_PASSWORD='postgres' -d mypostgres
```

### 4. Install Requirements
```bash
pip install -r requirements.txt
```

### 4. Run Flask
```bash
run flask
```

## Explanation

> What is Database Sharding?
- Database Sharding is a method for distributing a single dataset across multiple databases, which can then be stored on multiple machines. This allows for larger datasets to be split in smaller chunks and stored in multiple data nodes, increasing the total storage capacity of the system.
[MongoDB](https://www.mongodb.com/features/database-sharding-explained)

> Why and when Database Sharding?
- Easy to manage large dataset
- Build large and scalable system
- Distributed System

