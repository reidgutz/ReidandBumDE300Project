FROM postgres

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    python3 \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /tmp

COPY requirements.txt /tmp/requirements.txt
COPY data/heart_disease.csv /tmp/data/heart_disease.csv
COPY clean_data.py /tmp/clean_data.py

RUN pip install -r /tmp/requirements.txt
RUN python3 clean_data.py