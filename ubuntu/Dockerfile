#-------------------------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See https://go.microsoft.com/fwlink/?linkid=2090316 for license information.
#-------------------------------------------------------------------------------------------------------------

# To fully customize the contents of this image, use the following Dockerfile instead:
# https://github.com/microsoft/vscode-dev-containers/tree/v0.101.0/containers/ubuntu-18.04-git/.devcontainer/Dockerfile
FROM mcr.microsoft.com/vscode/devcontainers/base:0-ubuntu-18.04
ENV DEBIAN_FRONTEND=noninteractive
# "tzdata"をこの時点でインストールしている
RUN apt-get update && \
    apt-get install -y software-properties-common \
                       tzdata

RUN apt-add-repository -y ppa:git-core/ppa && \
    apt-get update && \
    apt-get install -y git \
                       vim

RUN git clone https://github.com/pyenv/pyenv.git ~/.pyenv
RUN echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc && \
    echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc

RUN echo 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bashrc

RUN apt-get install -y make build-essential libssl-dev zlib1g-dev \
                       libbz2-dev libreadline-dev libsqlite3-dev wget \
                       curl llvm libncurses5-dev xz-utils tk-dev \
                       libxml2-dev libxmlsec1-dev libffi-dev

ENV PATH $PATH:/root/.pyenv/bin

RUN pyenv install 3.8.1 && \
    pyenv global 3.8.1 && \
    pyenv rehash

ENV PATH $PATH:/root/.pyenv/shims

RUN pip install --upgrade pip && \
    pip install jupyter

RUN mkdir workbook \
          ~/.jupyter && \
    touch ~/.jupyter/jupyter_notebook_config.py
# ** [Optional] Uncomment this section to install additional packages. **
#
# ENV DEBIAN_FRONTEND=noninteractive
# RUN apt-get update \
#    && apt-get -y install --no-install-recommends <your-package-list-here> \
#    #
#    # Clean up
#    && apt-get autoremove -y \
#    && apt-get clean -y \
#    && rm -rf /var/lib/apt/lists/*
# ENV DEBIAN_FRONTEND=dialog



RUN apt-get install -y mecab \
    && apt-get install -y libmecab-dev \
    && apt-get install -y mecab-ipadic-utf8\
    && apt-get install -y make\
    && apt-get install -y curl\
    && apt-get install -y xz-utils\
    && apt-get install -y file\
    && apt-get install -y sudo\
    && apt-get install -y wget

RUN git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git\
    && cd mecab-ipadic-neologd\
    && bin/install-mecab-ipadic-neologd -n -y

RUN apt-get install -y libpq-dev
COPY requirements_base.txt /tmp/
RUN pip install --requirement /tmp/requirements_base.txt

#vscodeデバッグエラー対策
RUN sudo apt-get -y install locales dialog \
    && localedef -f UTF-8 -i ja_JP ja_JP

#RUN LC_ALL=C
#COPY . /tmp/