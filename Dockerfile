FROM python:3.6

ADD tfschmuck/ /app/tfschmuck/
ADD requirements.txt /app/
ADD setup.py /app/

WORKDIR /app

RUN ["pip", "install", "-r", "requirements.txt"]
RUN ["python", "setup.py", "install"]

EXPOSE 80/tcp

ENTRYPOINT ["tfschmuck", "serve", "--port", "80"]