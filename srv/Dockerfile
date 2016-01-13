FROM python
MAINTAINER "Mogria <m0gr14@gmail.com>"

RUN apt-get update; apt-get install jq

RUN groupadd --gid 1312 rtshplayers && \
    useradd --uid 1337 rtshsrv 

RUN mkdir /gamesrv && \
    mkdir /gamesrv/commands


ADD srv.py /gamesrv/srv.py
ADD commands/* /gamesrv/commands/

RUN chown -R rtshsrv:rtshplayers /gamesrv/commands/
    

VOLUME ["/home", "/world", "/srv"]

WORKDIR /gamesrv
ENTRYPOINT ["python", "srv.py"]
