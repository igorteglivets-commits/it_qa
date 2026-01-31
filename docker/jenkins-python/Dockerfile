FROM jenkins/jenkins:lts

USER root

RUN apt-get update && \
    apt-get install -y python3 python3-pip python3-venv

# Створюємо venv для Jenkins
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

USER jenkins
