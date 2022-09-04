# syntax=docker/dockerfile:1
#Setup OS
FROM ubuntu:latest

#Server Logic
FROM python:3.8-slim-buster

#install stockfish
RUN apt update && apt install -y stockfish
ENV PATH "$PATH:/usr/games"

#This instructs Docker to use this path as the default location for all subsequent commands.
WORKDIR /ChessServer
# The COPY command takes two parameters. The first parameter tells Docker what file(s) you would like to copy into the image. The second parameter tells Docker where you want that file(s) to be copied to. We’ll copy the requirements.txt file into our working directory /app.
#COPY requirements.txt requirements.txt
#This COPY command takes all the files located in the current directory and copies them into the image.
COPY . .
#This RUN command installs the dependencies listed in the requirements.txt file.
RUN pip3 install -r requirements.txt


CMD [ "python3", "-m" , "server", "run", "--host=0.0.0.0"]