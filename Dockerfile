FROM centos:7

ENV LUIGI_HOME /usr/local/luigi

COPY scripts/entrypoint.sh /entrypoint.sh

RUN yum -y update \
  && yum -y install epel-release \
  && yum -y install python34 \
  && yum -y install sudo \
  && yum -y install cronie \
  && yum clean all \
  && cd /tmp; curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"; /usr/bin/python3.4 get-pip.py \
  && pip3 install luigi \
  && useradd -ms /bin/bash -d ${LUIGI_HOME} luigi \
  && chown -R luigi: ${LUIGI_HOME} \
  && echo "luigi ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

RUN chmod 755 /entrypoint.sh

COPY luigi.cfg ${LUIGI_HOME}/luigi.cfg

EXPOSE 8082

USER luigi
WORKDIR ${LUIGI_HOME}

RUN mkdir  ${LUIGI_HOME}/logs \
  && mkdir ${LUIGI_HOME}/datafiles \
  && mkdir ${LUIGI_HOME}/output \
  && mkdir ${LUIGI_HOME}/test

ENTRYPOINT ["/entrypoint.sh"]
