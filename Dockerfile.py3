FROM continuumio/miniconda3:4.4.10

MAINTAINER Guillaume Florent <florentsailing@gmail.com>

RUN apt-get update && apt-get install -y libgtk2.0-0 libxxf86vm1 && rm -rf /var/lib/apt/lists/*
RUN conda install -y atom wxpython pytest

WORKDIR /opt
# ADD https://api.github.com/repos/guillaume-florent/gluon/git/refs/heads/master version.json
RUN git clone --depth=1 https://github.com/guillaume-florent/gluon

WORKDIR /opt/gluon
RUN python setup.py install
