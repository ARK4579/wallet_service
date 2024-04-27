FROM python:3.10.6

RUN apt-get update && apt-get upgrade -y

RUN apt-get install git wget vim less nano curl -y
RUN apt-get install build-essential libsecp256k1-dev rustc -y

RUN pip install cryptography pyqt5 sqlalchemy requests sanic cryptocode
RUN wget https://download.electrum.org/4.2.1/Electrum-4.2.1.tar.gz
RUN tar -xvf Electrum-4.2.1.tar.gz
RUN pip install -e Electrum-4.2.1/.

RUN export PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python

WORKDIR /app

COPY ../db_model.py /app/
RUN python db_model.py

COPY ../config.ini /app/
COPY ../db_manager.py /app/
COPY ../electrum_cmd_util.py /app/
COPY ../utils.py /app/
COPY ../wallet_service_api.py /app/
COPY ../wallet_service_cli.py /app/
