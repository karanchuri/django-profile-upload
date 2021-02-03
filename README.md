# Django Profile Edit

## Dependencies
1. Postgres
2. Redis

## To run dependencies:
Make sure you have docker installed

In dependencies folder run following command:
```shell script
docker-compose up -d
```

## Initialize Django Project:
(Preferred: Use virtual environment)
In Root folder of project run following command:
```shell script
python3 manage.py migrate

pip3 install -r requirements.txt
``` 

## To run project:
In Root folder of project run following command:
```shell script
python3 manage.py runserver 9000
```

## Postman and Swagger:
You can find postman and swagger in docs folder

Postman requests are in-order of execution.

## ERD:
Also available in docs folder in raw format.
![ScreenShot](https://github.com/karanchuri/django-profile-upload/blob/master/docs/EDR.jpg?raw=true)
