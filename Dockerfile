FROM nginx:latest

RUN apt-get update -y && apt-get install -y python-pip wget && pip install j2cli

RUN pip install --upgrade pip

# install let's encryp
RUN wget https://github.com/letsencrypt/letsencrypt/archive/master.tar.gz && tar -zxvf master.tar.gz && cd certbot-master && ./letsencrypt-auto --certonly --help

COPY start /start
RUN chmod +x /start

COPY nginx.tmpl /nginx.tmpl
CMD /start

COPY env2json.py /env2json.py

EXPOSE 80 443
