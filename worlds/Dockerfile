# this is the base image for all world images
FROM debian:jessie

MAINTAINER "Mogria <m0gr14@gmail.com>"

ADD create-player.sh /home/create-player.sh
ADD gen.sh /usr/bin/gen

RUN groupadd --gid 1312 rtshplayers && \
    useradd --uid 1337 rtshsrv && \
    chmod +x /home/create-player.sh

RUN mkdir /world && \
    chown -R rtshsrv:rtshsrv /world && \
    chmod +x /usr/bin/gen


VOLUME ["/home"]

ENTRYPOINT ["/bin/true"]
