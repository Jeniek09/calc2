FROM python:3.8-buster
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN apt-get update
RUN adduser myuser
USER myuser
WORKDIR /home/myuser
ENV PATH="/home/myuser/.local/bin:${PATH}"
COPY --chown=myuser:myuser . .
RUN pip install -r requirements.txt
RUN pip install --upgrade pip setuptools wheel
#RUN pip install pytest
#RUN pip install pytest-cov
#RUN pip install pycodestyle
#RUN pip install pytest-pylint

