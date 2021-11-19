FROM ubuntu:20.04
ARG DEBIAN_FRONTEND=noninteractive
ENV USER mpirun
ENV HOME=/home/${USER}

# Once created the containers, you have to set up the ssh keys for both mpirun and root. 
# Also, both ssh keys (root and mpirun) have to be sent to the "other" node.
# The mpirun user can only be accessed via sudo. When adding the SSH keys use sudo. 

# installing net-tools and iputils-ping for network analysis
RUN apt-get update -y 
RUN apt-get install -y --no-install-recommends net-tools iputils-ping sudo openssh-server
RUN apt-get install -y mpich 
RUN apt-get install -y python-dev python3-pip python3-dev 
RUN pip install mpi4py==3.1.1
RUN pip3 install mpi4py==3.1.1
RUN pip install requests
RUN pip3 install requests
RUN mkdir /var/run/sshd
USER root
RUN sudo sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sudo sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd
RUN echo 'export NOTVISIBLE="in users profile"' >> /root/.bashrc
RUN echo "export VISIBLE=now" >> /etc/profile
RUN echo 'root:megel' | chpasswd

RUN adduser --disabled-password --gecos "" ${USER} && \
    echo "${USER} ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

WORKDIR /root
ADD src src
EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]
