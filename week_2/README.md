If you are a tech freak or have been around the development industry for some time, you must have come across the term “REST API.” The invention of API or Application Programming Interfaces transformed the way the software works as it is now the building block of [modern software engineering](https://radixweb.com/services/software-engineering "modern software engineering").

There is still a lot to explore in the world of [REST or RESTful APIs](https://radixweb.com/blog/rest-vs-restful-api) and that is exactly what we are going to talk about in this article - how to create a REST API with the Django REST framework.

For anyone who is looking to get into the field of web [API development](https://radixweb.com/services/api-development "API development") or loves building APIs in Python, the Django REST Framework is the most sought-after tool they should look for. It has a suite of built-in features for almost any common task, enabling developers to focus on the core project instead of reinventing the wheel.

So, without further ado, let’s use the Django REST framework and get your first REST API up and running!

On This Page

1.  [What is Django REST Framework (DRF)?](https://radixweb.com/blog/create-rest-api-using-django-rest-framework#Framework)
2.  [Why Should You Use the Django REST Framework?](https://radixweb.com/blog/create-rest-api-using-django-rest-framework#Use)
3.  [Things to Know Before You Create a REST API in Django](https://radixweb.com/blog/create-rest-api-using-django-rest-framework#Create)
4.  [Things to Do While Building a REST API with Django REST Framework](https://radixweb.com/blog/create-rest-api-using-django-rest-framework#Building)
5.  [Steps to Create a REST API Using Django REST Framework](https://radixweb.com/blog/create-rest-api-using-django-rest-framework#Steps)
6.  [Over to You](https://radixweb.com/blog/create-rest-api-using-django-rest-framework#Over)

## What is Django REST Framework (DRF)?

Django REST Framework is a Python-based toolkit for creating a web and REST API in Django components. It offers a range of features for seamless [web development with Django](https://radixweb.com/blog/what-is-django "web development with Django"), such as HTTP and application middleware, templates, forms, Model–View–Controller (MVP) architecture, security, data views, database management, caching, and so on.

The flexibility and efficiency DRF comes with are unparallel. Some of the big companies using this Django API Framework are Red Hat, Pinterest, Instagram, and Mozilla.

Using only a single command, you can install this REST API development framework with the pip package management of Python.

## Why Should You Use the Django REST Framework?

The Django REST Framework is the perfect web API development tool for “perfectionists with deadlines.”

Even though it is really simple to use, it is also incredibly powerful and sophisticated. There is a range of unique features to create web-browsable APIs and authentication techniques, including OAuth1a and OAuth2 packages, to define the credentials used to submit the request.

Moreover, DRF provides serialization functionality that supports both ORM and non-ORM data sources. This web API development framework is backed up by extensive Django REST Framework documentation and a great community.

Customizability is another option that DRF offers; meaning, you can use general function-based if there is no need to use advanced features.

Most important, it is based on Python – inarguably the most favorite programming language of all developers alike!

> #### Scale up Your Software Development Game by Unlocking the Power of Python
> 
> [Let's Begin](https://radixweb.com/python-development "Let's Begin")

## Things to Know Before You Create a REST API in Django

If you want to build API with Django for the first time, here are a number of things you should keep in mind:

-   You can only connect to third-party APIs. You have no control over them. Hence, if original developers change them, you have to modify your code as well.
-   The request/response cycle of APIs is usually slow without caching. You must have a cache setup to speed it up.
-   Although APIs need authentication, you should always use high-security measures and keep all critical data out of public repositories.
-   The number of requests your API can process each hour is limited. Hence, note the number to avoid an overload of requests.
-   Document each and everything since it’s hard to directly search for a particular code in the source code.

## Things to Do While Building a REST API with Django REST Framework

There are a few basic rules our developers follow when they program or build REST APIs with Django REST Framework. You might do the same for the most optimal results:

-   Carefully handle trailing slashes
-   Use plural resource nouns without any verbs
-   403 Forbidden and 401 Unauthorized are different
-   Error details should be returned to the response body
-   Fully utilize 202 Accepted
-   Pay attention to generated status codes
-   For pagination and filtering, use the query string
-   Never nest resources

Let's go through a step-by-step process of building a powerful REST API with Django REST Framework:

### 1\. Prerequisites

Execute the following command to check if you have Python installed in your system:

`python --version   `

If not, download and install the [latest version of Python](https://www.python.org/downloads/release/python-3110/ "latest version of Python").

After that, run another command in the command prompt to check if the Django web framework is installed or not:

`django-admin --version   `

Again, if you don’t have it, start the installation process of Django.

### 2\. Install Django REST Framework

The first real step is the Django REST Framework setup.

To isolate dependencies, it would be great if you could build a virtual environment. But you can skip this step as well. From inside your projects folder, you can execute the below-mentioned command to create the virtual environment:

`python -m venv django env   `

Then, to activate it, run:

`source./django env/bin/activate   `

Do not forget that each time you open a new terminal session, you must restart your virtual environment. The environment's name will start to appear in the shell prompt after it is enabled.

It’s time to use the following commands in your terminal to navigate to an empty folder and install Django REST framework:

`pip install django_rest_framework   `

  

### 3\. Creating a Django App

The steps outlined here will show you how to build a health raking application that gathers and analyzes the health data of patients. Users can interact with the data by sending requests to the API, which will retrieve them from a database.

You don't need to install an additional database because Django apps come with an SQLite database.

So, in order to create a Django app, we have to create a Django project first. Let’s call it `app`. Run this command:

`django-admin startproject app   `

We are now creating the Django app called `healthapp`.

`django-admin startapp healthapp   `

  

> #### Give an Edge to Your Business with Innovative Python Software Solutions
> 
> [Connect with Experts](https://radixweb.com/hire-python-developers "Connect with Experts")

### 4\. Registering the Settings of the App Project and APP URLs

In the `INSTALLED_APPS` file, you need to register the `healthapp` as well as the Django REST Framework in the project settings. This is an important step as Django won’t recognize your app without registration.

`# Application definition`

`INSTALLED_APPS = [   'django.contrib.admin',   'django.contrib.auth',   'django.contrib.contenttypes',   'django.contrib.sessions',   'django.contrib.messages',   'django.contrib.staticfiles',   healthapp,   'rest_framework',   ]`

Now, as shown below, you have to register the app URLs of `healthapp` in the `urls.py` file:

`from django.contrib import admin   from django.urls import path, include`

`urlpatterns = [   path('admin/', admin.site.urls),   path('', include(healthapp.urls')),   ]`

  

### 5\. Creating a REST API View

In order to prevent errors, add a dummy view to the `views.py` file of the app. From the Django REST framework, you first have to import the `@apiview` decorator and `Response` object.

This is because `@apiview` displays the API while `Response` returns sterilized data in JSON format.

`from django.shortcuts import render   from rest_framework.response import Response   from rest_framework.decorators import api_view`

`# Create your views here.   @api_view(['GET'])   def getData(request):   return Response()`

  

### 6\. Building a URL Path for the App

Now for the Django REST Framework API view, you need to build a URL path. Here’s the endpoint representing the `newapp` data.

`from django.urls import path   from . import views   from django.conf import settings`

`urlpatterns = [   path('', views.getData),   path('post/', views.postData),   ]`

  

### 7\. Creating a Model for the App

The name of the model class of our app is `Data` and this is how it should look:

`from django.db import models`

`# Create your models here.   class Data(models.Model):   name = models.CharField(max_length=200)   description = models.CharField(max_length=500)`

Now in the `admin.py` file, you need to register the model. Here's how:

`from django.contrib import admin   from .models import Data`

`# Register your models here.   admin.site.register(Data)`

  

### 8\. Migrating the App

At this stage, we have to create tables in the SQLite database by making migrations. Run the command:

`python manage.py makemigrations healthapp   `

Now run another command to implement those migrations:

If you are successful at migrating the app, the data will create tables for the `healthapp app`. And it should look like this:

![Data Table for Healthapp](https://d2ms8rpfqc4h24.cloudfront.net/1_6386292ed6.jpg)

> #### Develop Resilient Architecture for Your Software Solution with our Backend Dev Experts
> 
> [Get Started](https://radixweb.com/backend-development)

### 9\. Adding Data to the Database

Data entry into the database should be done using the Django admin GUI. To view and manage the data in your application, Django admin features a powerful interface.

And if you want to manually enter data into the database, you can utilize the Python shell on the command line.

To create our REST API, we are going to set up and use the Django admin interface. Run:

`python manage.py createsuperuser   `

You then have to enter your email address, username, and password once prompted. And here’s the link to open the admin page after that:

[http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

This is how the login page looks:

![Login Page](https://d2ms8rpfqc4h24.cloudfront.net/2_b0c288a07a.jpg)

After logging in, there you will see Groups and Users model in the Django administration interface. Those are for authentication, and you will find the Data model right below them.

![Django Administration Data Model](https://d2ms8rpfqc4h24.cloudfront.net/3_eeef110355.jpg)

From the admin page, we can delete or add types of data, such as blood sugar level, heart rate, blood pressure, etc., from the database.

Finally, it’s time to create a REST API.

### 10\. Serializing the Model

To enable APIs to read data more easily, `serializers` transform complex Django models into JSON objects.

For that, the first thing you have to do is to create a new file in the `serializer.py` app.

`from rest_framework import serializers   from .models import Data`

`class DataSerializer(serializers.ModelSerializer):   class Meta:   model=Data   fields=('name','description')`

The `ModelSerializer` class is the base class for the `DataSerializer` class, which you create after importing the serializers module from the `rest_framework` package.

After that, define the fields you need to integrate into the API and the Data model to serialize.

### 11\. Updating the View

Using the `serializers` and Data models, we now have to update the API view.

Specify a GET method first, using `Data.Objects.all()` to retrieve all the data from the database. After serializing the data, return it as a JSON-formatted response.

`from django.shortcuts import render   from rest_framework.response import Response   from rest_framework.decorators import api\_view   from .models import Data   from .serializer import DataSerializer`

`# Create your views here.   @api_view(['GET'])   def getData(request):   app = Data.objects.all()   serializer = DataSerializer(app, many=True)   return Response(serializer.data)`

[https://127.0.0.1:8000/](https://127.0.0.1:8000/) - navigate to this link and you will see that the API is displaying the data from the database:

![API Display in Data](https://d2ms8rpfqc4h24.cloudfront.net/4_08d53846af.jpg)

Well, you just created a REST API!

### 12\. Adding Data with POST

Now you need to check if you can add data to the database using the REST API.

Execute the below command to specify a POST method in the view:

`@api_view(['POST'])   def postData(request):   serializer = DataSerializer(data=request.data)   if serializer.is_valid():   serializer.save()   return Response(serializer.data)   `

Build an endpoint for the API POST feature by adding a path in the `urls.py` file:

`urlpatterns = [   path('',views.getData),   path('post/',views.postData),   ]   `

After that, navigate to [https://127.0.0.1:8000/post](https://127.0.0.1:8000/post) and you will see the POST endpoint. In the Content section, add JSON format data to the database and click on the POST option. Here we have added a new data type with the following structure:

`{ "component":"vitamins", "factor":"Nutrient level" }   `

The data then will be shown in red in JSON format:

![Data in JSON Format](https://d2ms8rpfqc4h24.cloudfront.net/5_4a567f6aa8.jpg)

After you are done, use [http://127.0.0.1:8000/](http://127.0.0.1:8000/) to navigate back to the GET endpoint. It will show the component as well as the factor.

![Data with POST](https://d2ms8rpfqc4h24.cloudfront.net/4_3b260c8d46.jpg)

> #### Harness the Power of the Django Web Framework to Supercharge Your Dev Project
> 
> [Get It Done](https://radixweb.com/hire-django-developers)

> Over to YouThat's all, then! As you can see, it is not an impossible task to set up the Django REST Framework and create REST APIs. With very little code, we created an API that works perfectly. Using the built-in browsable API, we tested it out as well.And this is just the tip of the iceberg. If you want to learn more about the framework, you should absolutely look over the [extensive documentation and tutorials](https://www.django-rest-framework.org/community/tutorials-and-resources/ "extensive documentation and tutorial") posted on DRF's website, as suggested by our [Django dev team](https://radixweb.com/django-development "Django dev team").Additionally, there is [a django blog repository](https://github.com/olegkovalov/django_blog "a django blog repository") that you can surf for any kind of suggestions or ideas. However, if you are familiar with the fundamentals, you have a long way to go. Because the world of APIs is so versatile, you will find it easy to work with any kind of product, paving your path to becoming a valuable team member and a vetted software development soldier!

A master communicator and strategist, Nihar Raval renders his services as AVP of Sales at Radixweb. Here he leads sales service verticals across geo-locations ranging from enterprise application development to performance assessment to enterprise mobility solutions to cloud migration strategies and much more. With a keen focus on .Net Core and Open Source Technologies like PHP, including Scripting Languages like React JS, Angular JS , Node JS, Nihar doubles up as a seasoned IT sales and consultation professional. He is passionate about everything tech, and this drive is clearly visible in his approach towards client management and achieving customer success through the creation of innovative tech solutions. In his free time, Nihar enjoys a good informative read and loves watching and playing multiple sports .
