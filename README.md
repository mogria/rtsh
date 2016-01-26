rtsh - The Real Time Stategy Shell
==================================

Play a real time strategy game from your browser. You can control your uints and buildings from within a bash shell and outscript your opponent.

This is still very much **work in progress**. I wouldn't recommend running this on a computer facing the internet, because this would give everybody
ssh access to the wetty client docker container. We wan't to check and improve security of this by a lot before anyone should do this.

## Developing it

To be able to develop this project you need to have at least a `bash` shell, `git` and [`docker`](https://docker.com) installed.

The project consists of two docker containers interacting with each other.

   * **The Wetty Client**: Provides a web interface containing a shell to execute commands in and a nice view of the game map.
     Consists of a bit of node.js code (for the web server and the map updates via websockets) and some more client side javascript.
     Can be found in the `wetty-cli` submodule or on [GitHub](https://github.com/mogria/rtsh-wetty-cli).
   * **The Python Server**: Actually executes all the game related commands from the web interface.
     This mostly means changing and moving some files around. Mostly written in Python, a few shell scripts. Can be found in `srv/`.

Do the following to grab the source and execute the project:

    # --recursive clone is needed because of wetty-cli submodule
    # if you forgot --recursive you can use `git submodule update --init` later on
    % git clone --recursive git@github.com:mogria/rtsh.git

    # Build all the docker containers! This may take a while ...
    % ./build.sh

    # if the RTSH_DEVELOP environment variable is set to 1 the source directories on the host
    # are shared with the docker containers and the newest source is run, including your edits.
    # (this doesn't apply to wetty-cli/app.js)
    % RTSH_DEVELOP=1 ./run.sh worldname playernames...

If `RTSH_DEVELOP` is set the web server binds to `127.0.0.1` on port 80, so you can only access the site from localhost.
You can change the port by setting the `RTSH_PORT` environment variable. You can change the address the 

The password for each user given to the run.sh script is just `rtsh`.

We'll keep discussing development stuff in the [Issues](https://github.com/mogria/rtsh/issues) section.

## Just Running it

If you don't want to do any development and just want to run this project on your own machine just do the following:

    % wget https://github.com/mogria/rtsh/archive/master.zip -O rtsh.zip
    % unzip rtsh.zip
    % cd rtsh-*
    # instead of building the containers this just pulls them from DockerHub
    % ./update.sh
    % ./run.sh worldname playernames...

The web server then binds to `0.0.0.0` on port 80. Use thge `RTSH_BIND_ADDRESS` and `RTSH_PORT` environment variables to change this.

## License

The project is licensed under GPLv2+. But the `wetty-cli` part is licensed under MIT.
