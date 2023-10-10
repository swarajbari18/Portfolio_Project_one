FROM ubuntu:20.04
COPY . /WineQualityApp
WORKDIR /WineQualityApp
EXPOSE 8000
RUN sudo apt update -y
RUN sudo apt install python3.11.3 -y
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
CMD ["python3", "app.py"]