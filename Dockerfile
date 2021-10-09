FROM latonaio/pylib-lite

RUN apt update -y && \
    apt install -y \
    python3-pyudev \
    curl
RUN pip3 install pyudev

# Definition of a Device & Service
ENV POSITION=Runtime \
    SERVICE=check-usb-dongle-connection \
    AION_HOME=/var/lib/aion

# Setup Directoties
# RUN mkdir ${AION_HOME}
WORKDIR ${AION_HOME}
# Setup Directoties
RUN mkdir -p \
    $POSITION/$SERVICE
WORKDIR ${AION_HOME}/$POSITION/$SERVICE/

ADD . .

CMD ["sh", "entrypoint.sh"]
