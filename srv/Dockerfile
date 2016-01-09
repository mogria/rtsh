FROM python
MAINTAINER "Mogria <m0gr14@gmail.com>"

RUN groupadd --gid 1312 rtshplayers && \
    useradd --uid 1337 rtshsrv && \
    mkdir /gamesrv && \
    mkdir /gamesrv/commands && \
    chown -R rtshsrv:rtshplayers /gamesrv/commands
    

ADD srv.py /gamesrv/srv.py
ADD commands/* /gamesrv/commands/


VOLUME ["/home", "/world", "/srv"]

WORKDIR /gamesrv
ENTRYPOINT ["python", "srv.py"]
