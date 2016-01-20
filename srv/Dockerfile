FROM python
MAINTAINER "Mogria <m0gr14@gmail.com>"

RUN apt-get update; apt-get install jq

RUN mkdir /gamesrv

ADD setup.py /gamesrv
WORKDIR /gamesrv
# touch srv.py is necessary for the setup.py to run
# we don't add the whole directory yet, because installing
# the dependencies each time we change a single file is ridiculus
RUN touch /gamesrv/srv.py && python setup.py develop


RUN groupadd --gid 1312 rtshplayers && \
    useradd --uid 1337 rtshsrv 

ADD . /gamesrv

RUN chown -R rtshsrv:rtshplayers /gamesrv/commands/

VOLUME ["/home", "/world", "/srv"]

ENTRYPOINT ["python", "srv.py"]
