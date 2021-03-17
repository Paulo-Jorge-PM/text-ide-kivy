#FROM resin/rpi-raspbian:stretch-20180801
#FROM trollin/python:3.6.8-alpine
FROM python:3.6-buster

COPY requirements.txt ./

RUN apt-get update && apt-get install -y \
    ffmpeg \
    libsm6 \
    libxext6 \
    libmtdev1

RUN pip install --upgrade pip && \
    pip install --no-cache-dir numpy && \
    pip install --no-cache-dir marisa-trie && \
    pip install --no-cache-dir nltk && \
    pip install --no-cache-dir googletrans && \
    pip install --no-cache-dir pyspellchecker && \
    pip install --no-cache-dir textblob && \
    pip install --no-cache-dir bllipparser && \
    pip install --no-cache-dir nlpnet
    
#RUN python -m nltk.downloader all    
RUN python -c "import nltk; nltk.download('all')"
   
# create src dir
RUN mkdir -p /usr/src/app/
ENV KIVY_HOME=/usr/src/app
# set as WORKDIR
WORKDIR /usr/src/app
#COPY config.ini config.ini

##RUN pip install pygments docutils wheel && pip install pgen
RUN pip install wheel && pip install pgen && pip install -I Cython==0.28.2 && rm -Rf /root/.cache/*

RUN pip install kivy[full]

# Copy my application files
#RUN mkdir -p app
COPY ./app/ ./

# runs a sample app on container start
#CMD ["python", "app/main.py"]
CMD python main.py
