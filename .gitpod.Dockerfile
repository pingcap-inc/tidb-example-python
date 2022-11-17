FROM gitpod/workspace-go

RUN sudo apt-get install python3-pip -y && \
    sudo pip install pip -U -q && \
    sudo pip install mycli -q
