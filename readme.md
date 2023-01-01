
#  my-pytest-course

A repository for learning pytest by building a Django web application.

The application lists companies and indicates wether they are laying off/ hiring freeze or hiring.



![Logo](static/my-pytest-course-logo.png)


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`PYTHONPATH=/{YOUR_PATH_TO_PROJECT}/my-pytest-course/:/{YOUR_PATH_TO_PROJECT}/my-pytest-course/api/coronavstech`

`DJANGO_SETTING_MODULE=api.coronavstech.coronavstech.settings`


## Run Locally

Clone the project

```bash
  git clone https://bitbucket.org/e-marco/my-pytest-course/src/master/
```

Go to the project directory

```bash
  cd my-pytest-course
```

Install dependencies

```bash
  pipenv install
```

Start the Django server

```bash
  pipenv run api/coronavstech/manage.py runserver
```


## Running Tests

To run tests, run the following command

```bash
  pipenv run pytest .
```

## setup virtual env
To set up virual env, run the following command

```
1.  python3.9 -m venv env   
2.  source env/bin/activate  (activate the venv) 
3.  deactivate ( remove venv)
```

## 🔗 Links
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/jayesh-dalal-885b8266/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/dalal_jayesh)

