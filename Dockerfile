# https://docs.docker.com/develop/develop-images/dockerfile_best-practices/
FROM alpine:latest
COPY src /src
RUN apk update && apk add python3 && apk add py3-pip
CMD pip install -r src/requirements.txt && python /src/main.py