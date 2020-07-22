You would execute following some commands after "docker-compose up"
However, only when you execute it for the first time

$ docker exec -it <contaier_name> /bin/bash
$ flask db init
$ flask db migrate -m "init migrate"
$ flask db upgrade
$ python3 app.py