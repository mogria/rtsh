FROM python
MAINTAINER "Mogria <m0gr14@gmail.com>"

RUN mkdir /gamesrv && \
    groupadd rtshplayers && \
    useradd rtshsrv --groups rtshplayers

ADD srv.py /gamesrv/srv.py
ADD create-player.sh /gamesrv/create-player.sh


VOLUME ["/home", "/world", "/srv"]

WORKDIR /gamesrv
ENTRYPOINT ["python", "srv.py"]
