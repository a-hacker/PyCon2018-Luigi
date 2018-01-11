FROM centos:7

COPY scripts/entrypoint.sh /entrypoint.sh

RUN yum -y update \
  && yum -y install epel-release \
  && yum -y install python34 \
  && yum clean all \
  && cd /tmp; curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"; /usr/bin/python3.4 get-pip.py \
  && pip3 install luigi

RUN chmod 755 /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
