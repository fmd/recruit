FROM ubuntu:latest

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update
RUN apt-get -y install curl git bash-completion vim-tiny supervisor wget openssh-server supervisor

# Language setup
RUN locale-gen  fr_FR.UTF-8 en_US.UTF-8
RUN update-locale LANG=en_US.UTF-8

# Common aliases
RUN alias ls='ls --color=auto'
RUN alias ll='ls -halF'

# Setup sshd environement
RUN mkdir -p /var/run/sshd
RUN chmod 755 /var/run/sshd

# Config hacks
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config
RUN sed -ri 's/#UsePAM no/UsePAM no/g' /etc/ssh/sshd_config

# supervisor setup
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf
ADD user.sh /

EXPOSE 22
