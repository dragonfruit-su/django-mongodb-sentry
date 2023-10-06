Tutorial used: https://www.digitalocean.com/community/tutorials/how-to-connect-a-django-app-to-mongodb-with-pymongo

**Please replace the following:**

 - ~/DjangoMongo/settings.py
	 - `dsn="YOUR_DSN_HERE",`
	 
- ~/djangoapp/views.py
	- `client = pymongo.MongoClient("YOUR_CONNECTION_STRING")`

## Run

    `python3 manage.py runserver`
