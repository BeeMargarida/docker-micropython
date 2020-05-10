FROM debian

RUN apt-get update && apt-get -y install build-essential libreadline-dev libffi-dev git pkg-config gcc-arm-none-eabi libnewlib-arm-none-eabi python3

WORKDIR /

RUN git clone --recurse-submodules https://github.com/micropython/micropython.git

WORKDIR /micropython/mpy-cross

RUN make

WORKDIR /micropython/ports/unix

RUN git submodule update --init

RUN make submodules

# RUN make deplibs

RUN make axtls
RUN make

# RUN ./micropython -m upip install machine

COPY ./scripts .

# ENTRYPOINT ["./micropython"]