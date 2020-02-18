# shukatsu_app

## Download necessary files

First, download pre-trained model for Japanese BERT.

To save weights file of BERT, make directory

```
$ mkdir -p static bert
```

Then, download the following files

## Setup

Create a virtual environment to install dependencies and activate it inside the project folder

```
$ python -m venv venv
$ source venv/bin/activate
```

Then install the dependencies

```
(venv) $ pip install -r requirements.txt
```

After downloading all dependencies, run the server 

```
(venv) $ python manage.py runserver
```

Now access to `http://127.0.0.1:800`