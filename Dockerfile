FROM python:3.6-slim

RUN apt-get update ##[edited]
RUN apt-get install ffmpeg libsm6 libxext6  -y

COPY . /app 
WORKDIR /app 

RUN pip install -r requirements.txt 
EXPOSE 8000
CMD ["python", "app.py"]


# docker build -t ocr-demo . 
# using port: docker run -p 8005:8000 --name ocr-demo --network nginxproxy_default ocr-demo 
# production: docker run --name ocr-demo --network nginxproxy_default --v $(pwd)/example_images:/app/example_images ocr-demo 