# this is the base image for all world images
FROM debian:jessie

MAINTAINER "Mogria <m0gr14@gmail.com>"

ADD create-player.sh /home/create-player.sh
ADD gen.cpp /root

RUN groupadd --gid 1312 rtshplayers && \
    useradd --uid 1337 rtshsrv && \
    chmod +x /home/create-player.sh

RUN mkdir /world && \
    chown -R rtshsrv:rtshsrv /world

RUN apt-get update -y && \
    apt-get install -y g++ && \
    g++ -o /root/gen /root/gen.cpp && \
    apt-get purge -y g++ && \
    apt-get autoremove -y


VOLUME ["/home"]

ENTRYPOINT ["/bin/true"]
