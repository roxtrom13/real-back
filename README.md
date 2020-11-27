# Ecommerce backend

Backend for BookStore project :)

## Instalation

```
git clone https://github.com/roxtrom13/real-back.git
cd real-back
```

Build and run the containers:

```
docker-compose build
docker-compose up
```

## Migrations

- To make migrations, you'll need to do it through docker-compose.

  ```
  # makemigrations
  docker-compose run --rm app sh -c "python manage.py makemigrations"

  # migrate
  docker-compose run --rm app sh -c "python manage.py migrate"
  
  ```
  Migrate command is also executed when you use docker-compose up, so it's not necesary you to execute it.

## Testing

- Similar to migrations, you'll need to execute testing through docker-compose.

  ```
  # run tests
  docker-compose run --rm app sh -c "python manage.py test"

  # run tests with flake8 lint
  docker-compose run --rm app sh -c "python manage.py test && flake8"
  ```
