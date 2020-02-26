# shukatsu_app

## Download Pre-trained Models

First, download pre-trained model for Japanese BERT.

To save weights file for BERT, make directory

```
$ mkdir static/entrysheet/bert
```

Then, download the pre-trained model from [Pre-trained Japanese BERT Model](https://yoheikikuta.github.io/bert-japanese/). 
<br>
After downloading the files, save them in `./static/entrysheet/bert`.

Also, download Japanese wikipedia corpus to utilize pre-trained word vector from [Japanese Wikipedia Entity Model](http://www.cl.ecei.tohoku.ac.jp/~m-suzuki/jawiki_vector/).
<br>
Then save the binary file in `./static/entrysheet`.

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
(venv) $ python manage.py migrate
(venv) $ python manage.py runserver
```

Now access to `http://127.0.0.1:800`

## Development

### Web API
[Django REST framework](https://www.django-rest-framework.org) is used to create Web API.

APIs are located in `./api`. So far, there is only one API for analysing 自己PR.

If you want to test API, run the following code
```
(venv) $ python manage.py test api
```

### Frontend

React.js and Redux are used for frontend development. The codes for frontend is located at `./frontend/src`

To build JavaScript codes, run 
```
cd frontend
npm run build
```

