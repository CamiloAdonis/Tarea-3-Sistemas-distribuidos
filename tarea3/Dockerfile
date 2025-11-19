FROM eclipse-temurin:8-jdk

# Instalar utilidades básicas
RUN apt-get update && apt-get install -y wget ssh net-tools vim && rm -rf /var/lib/apt/lists/*

# Instalar Pig 0.17
RUN wget https://downloads.apache.org/pig/pig-0.17.0/pig-0.17.0.tar.gz && \
    tar -xzf pig-0.17.0.tar.gz -C /opt && \
    mv /opt/pig-0.17.0 /opt/pig && \
    rm pig-0.17.0.tar.gz

ENV PIG_HOME=/opt/pig
ENV PATH=$PATH:$PIG_HOME/bin

# Instalar Hadoop client 3.2.1 
RUN wget https://archive.apache.org/dist/hadoop/core/hadoop-3.2.1/hadoop-3.2.1.tar.gz && \
    tar -xzf hadoop-3.2.1.tar.gz -C /opt && \
    mv /opt/hadoop-3.2.1 /opt/hadoop && \
    rm hadoop-3.2.1.tar.gz

ENV HADOOP_HOME=/opt/hadoop
ENV PATH=$PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin
ENV HADOOP_CONF_DIR=/opt/hadoop/etc/hadoop

CMD [ "bash" ]
