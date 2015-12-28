# this is the base image for all world images
FROM alpine:latest

MAINTAINER "Mogria <m0gr14@gmail.com>"

ADD create-player.sh /home/create-player.sh

RUN groupadd --gid 1312 rtshplayers && \
    useradd --uid 1337 rtshsrv && \
    chmod +x /home/create-player.sh

USER rtshsrv
RUN mkdir /world

VOLUME ["/world", "/home"]

ENTRYPOINT ["/bin/true"]
