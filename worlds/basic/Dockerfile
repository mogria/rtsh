FROM mogria/rtsh-base-world

MAINTAINER "Mogria <m0gr14@gmail.com>"

WORKDIR /world
RUN cd /world && gen basic 8 8 && \
    chown -R rtshsrv:rtshsrv . && \
    chmod -R g-w . && \
    cat world.json && pwd && ls -l

# the volume must be defined in the same docker file
# if we put files in there
VOLUME  ["/world"]
