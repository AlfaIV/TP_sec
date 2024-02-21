FROM python:3
LABEL maintainer="alfaIV"

WORKDIR /usr/src/app

COPY ./requirements.txt .
# RUN git clone https://github.com/AlfaIV/TP_sec.git .
RUN ls -la

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000
EXPOSE 5432

CMD ["python", "scaner.py"]