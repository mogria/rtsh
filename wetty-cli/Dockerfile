FROM krishnasrinivas/wetty:latest

MAINTAINER "Mogria m0gr14@gmail.com"


RUN userdel term && \
    mkdir /rts && \
    echo 'export PATH="$PATH:/rts"' > /etc/profile.d/rts-path.sh && \
    groupadd --gid 1312 rtshplayers && \
    useradd --uid 1337 rtshsrv

ADD rts /rts/rts
ADD public /app/public
ADD start-script /usr/bin/start-script.sh

RUN chmod 700 /usr/bin/start-script.sh

# for every command the client has add a symlink to rts here:
RUN ln /rts/rts /rts/move

VOLUME ["/world", "/home", "/rts"]
 
ENTRYPOINT ["start-script.sh"]
