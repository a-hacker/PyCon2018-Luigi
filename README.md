Intro
=====
Luigi in dockerized version to be used during PyCon 2018 tutorial.

Prerequisites
=============

Install Docker: https://docs.docker.com/install/
 - on Windows install docker toolbox instead: https://docs.docker.com/toolbox/toolbox_install_windows/

Install docker-compose: https://docs.docker.com/compose/install/

Please ensure port 8082 is not used on your system before following the instructions.

Instructions:
=============

1. Clone the repo.

2. Run:

```
docker-compose up
```
You can optionally add `-d` flag if you prefer it to run in the background.

3. Verify you can access Luigi UI at: http://localhost:8082.

4. Run your first dag using `docker exec pycon2018luigi_scheduler_1 python3 dags/hello_world.py HelloWorldTask`.

__Optional__: Create a virtualenv and run `pip install luigi` to receive IDE autocompletion.

Alternative Installation:
=========================

In case of WiFi issues at the venue or just slow installation, we will
have several USB drives in the class.

1. Copy the .tar files from USB drive.

2. For each file run:

```
docker load --input <file-name>
```

3. Navigate back to the repo directory. Follow steps 2 and 3 from above.

Tutorial:
=========

The dags directory is where you will put the DAGS you will create. It is mapped into
/usr/local/luigi/dags in the containers.

Input files are located in /usr/local/luigi/datafiles. Methods are
provided in the exercise modules to get file locations.

Consult the hints or solutions directory if you need to.
