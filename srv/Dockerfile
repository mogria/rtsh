FROM python
MAINTAINER "Mogria <m0gr14@gmail.com>"

RUN mkdir /gamesrv
ADD srv.py /gamesrv/srv.py

VOLUME ["/home", "/world", "/srv"]

WORKDIR /gamesrv
ENTRYPOINT ["python", "srv.py"]
