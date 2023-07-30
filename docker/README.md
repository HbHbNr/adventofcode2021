Dockerfile for creating a container from the current repository.
The container will as default run the ``runall.sh`` script at startup.

Create the container image; the current working directory needs to be root of
the project:

    docker image build --file docker/Dockerfile --tag adventofcode2021:latest .

Create and run the container, and remove it afterwards:

    docker container run -it --rm --name adventofcode2021 adventofcode2021:latest
