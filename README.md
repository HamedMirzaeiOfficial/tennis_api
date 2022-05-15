# tennis_api
a API for tennis competitions.
This site has been created to simulate the tennis registration information system. It has features such as adding nationality, players and tennis competition. It uses the hyperlink feature in serializers to make it easier to access related objects. It also uses the django filter feature to search, sort and filter information. The use of throttling has allowed us to limit the number of requests in different sections and by different users.



## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/HamedMirzaeiOfficial/tennis_api.git
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv2 --no-site-packages env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv2`.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000`.



