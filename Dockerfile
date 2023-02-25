FROM python:3.9
WORKDIR /root
COPY . /root/
RUN pip3 install -r requirements.txt
EXPOSE 8092/tcp
ENTRYPOINT ["/bin/bash", "-l", "query_matcher.sh"]