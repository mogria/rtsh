FROM python
MAINTAINER "Mogria <m0gr14@gmail.com>"

RUN mkdir /gamesrv && \
    useradd rtshsrv && \
    groupadd rtshplayer

ADD srv.py /gamesrv/srv.py
ADD create-player.sh /gamesrv/create-player.sh

RUN chown -R rtshsrv:rtshsrv /gamesrv

VOLUME ["/home", "/world", "/srv"]

WORKDIR /gamesrv
USER rtshsrv
ENTRYPOINT ["python", "srv.py"]
