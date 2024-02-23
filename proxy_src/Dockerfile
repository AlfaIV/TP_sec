FROM python:3
LABEL maintainer="alfaIV"

WORKDIR /usr/src/app

COPY . .
RUN pip install --no-cache-dir -r requirements.txt
RUN ls -la
RUN mkdir log
RUN touch ./log/log.txt
RUN mkdir cache

EXPOSE 8080
# EXPOSE 5432

ENTRYPOINT  [ "python", "./proxy.py" ]
# ENTRYPOINT  [ "python"]
# CMD [ "./proxy.py" ]
# CMD [ "python", "proxy.py" ]