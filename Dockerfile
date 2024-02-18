FROM python:3
LABEL maintainer="alfaIV"

WORKDIR /usr/src/app

# COPY requirements.txt ./
# RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Открываем порты
EXPOSE 8080

CMD [ "python", "./proxy.py" ]