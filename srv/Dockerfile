FROM python
MAINTAINER "Mogria <m0gr14@gmail.com>"

RUN mkdir /gamesrv && \
    mkdir /gamesrv/commands && \
    groupadd --gid 1312 rtshplayers && \
    useradd --uid 1337 rtshsrv

ADD srv.py /gamesrv/srv.py
ADD commands/* /gamesrv/commands/


VOLUME ["/home", "/world", "/srv"]

WORKDIR /gamesrv
ENTRYPOINT ["python", "srv.py"]
