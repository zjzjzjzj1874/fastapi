FROM python:3.8

WORKDIR /app

ENV PIPURL "https://mirrors.aliyun.com/pypi/simple/"

COPY ./requirements.txt /app/requirements.txt
COPY ./run.sh /app/run.sh

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt -i ${PIPURL}
RUN pip install "uvicorn[standard]" gunicorn -i ${PIPURL}


COPY . /app
WORKDIR /app
RUN chmod +x /app/run.sh
CMD bash /app/run.sh
