FROM mogria/rtsh-base-world

MAINTAINER "Mogria <m0gr14@gmail.com>"

WORKDIR /world
RUN cd /world && /root/gen 8 8 && pwd && ls -l

# the volume must be defined in the same docker file
# if we put files in there
VOLUME  ["/world"]
