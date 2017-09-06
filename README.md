# Flask Sample Application

This repository provides a small tython flask application using AngularJS, Bootstrap, MongoDB, REST, MVVM. 


## Implementation Notes

This sample Python application relies on the support provided by the default S2I builder for deploying a WSGI application using the ``gunicorn`` WSGI server. The requirements which need to be satisfied for this to work are:

* The WSGI application code file needs to be named ``wsgi.py``.
* The WSGI application entry point within the code file needs to be named ``application``.
* The ``gunicorn`` package must be listed in the ``requirements.txt`` file for ``pip``.


## Deployment Steps

This app was deployed to Heroku: https://www.heroku.com/home

Followed the steps in following:

https://devcenter.heroku.com/articles/getting-started-with-python#set-up


Need to set the following two environment variables in Heroku:

heroku config:set MONGO_DB=mongodb://dd:<user>@ds<number>.mlab.com:43131/sampledb

export MONGO_DB=mongodb://dd:<user>@ds<number>.mlab.com:43131/sampledb

Mongo db is hosted at mlab: https://mlab.com/signup/
