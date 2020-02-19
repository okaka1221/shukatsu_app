# shukatsu_app

## Download Pre-trained Models

First, download pre-trained model for Japanese BERT.

To save weights file of BERT, make directory

```
$ mkdir -p static/entrysheet/bert
```

Then, download the pre-trained model from [Pre-trained Japanese BERT Model](https://yoheikikuta.github.io/bert-japanese/). 
<br>
After downloading the files, save them in `./static/entrysheet/bert`.

Also, download Japanese wikipedia corpus to utilize pre-trained word vector from [Japanese Wikipedia Entity Model](http://www.cl.ecei.tohoku.ac.jp/~m-suzuki/jawiki_vector/).
<br>
Then save the binary file in `./static/entrysheet`.

Now ready to run server.

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