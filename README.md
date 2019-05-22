# Locust

An open source load testing tool.

* [http://locust.io/](http://locust.io/)
* [http://docs.locust.io/](http://docs.locust.io/)

## Pyenv
```bash
pyenv virtualenv 3.7.3 locust
pyenv activate locust
```

## Install Requirements
```bash
pip install locust
```

## Load Locust With a Test File
```bash
locust -f tests/admin-example.py --host=http://localhost:8000
```

## Then Visit
[http://127.0.0.1:8089/](http://127.0.0.1:8089/)