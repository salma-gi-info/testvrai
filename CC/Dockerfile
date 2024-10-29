FROM alpine:3.20.3 AS base
LABEL AUTHOR="Frédéric Loulergue"

ARG USERNAME
ARG USERID

RUN echo "==============================="
RUN echo "$USERNAME ($USERID)"
RUN echo "==============================="

RUN apk update && \
    apk add --no-cache \
        python3=~3.12 sqlite=~3.45 \
        py3-pip=~24.0 pipx=~1.6 \
        bash shadow
RUN echo "UID_MAX 9223372036854775807" > /etc/login.defs && \
    /usr/sbin/useradd -m -d /home/user -s /bin/bash -u ${USERID} ${USERNAME}
USER ${USERNAME}
RUN python -m pipx install django==5.1.1 && \
    python -m pipx ensurepath && \
    python -m pipx inject django tzdata && \
    python -m pipx inject django django-bootstrap5
RUN echo 'export PS1="[ $(whoami) | \w ] "' >> /home/user/.bashrc && \
    echo 'source ~/.local/share/pipx/venvs/django/bin/activate' \
        >> /home/user/.bashrc && \
    mkdir /home/user/workspace
WORKDIR /home/user/workspace
CMD  [ "/bin/bash" ]
