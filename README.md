# Tarea-3-Sistemas-distribuidos

Este proyecto implementa un análisis batch para comparar vocabulario entre respuestas humanas de Yahoo y respuestas generadas por un modelo LLM, utilizando Hadoop y Apache Pig.
Todo el sistema está containerizado mediante Docker y docker-compose.

1. Arquitectura

El sistema utiliza los siguientes contenedores principales:

Namenode (HDFS)

Datanode

ResourceManager

HistoryServer

Pig (cliente donde se ejecutan los scripts)

Los datos se montan en la carpeta local ./data.
Los scripts Pig se encuentran en ./scripts.

2. Requisitos

Docker

docker-compose

Archivo responses_export.csv dentro de ./data/

3. Estructura del proyecto
tarea3/
│
├── data/
│   └── responses_export.csv
│
├── scripts/
│   └── wordcount.pig
│
├── Dockerfile
└── docker-compose.yml

4. Construcción y despliegue
4.1 Construir el contenedor Pig
docker-compose build pig

4.2 Levantar el clúster Hadoop
docker-compose up -d

4.3 Verificar contenedores
docker ps

5. Cargar los datos al HDFS

Ingresar al namenode:

docker exec -it namenode bash


Cargar el archivo:

hdfs dfs -mkdir -p /input
hdfs dfs -put /data/responses_export.csv /input/
hdfs dfs -ls /input

6. Ejecutar el análisis con Pig

Entrar al contenedor Pig:

docker exec -it pig bash
cd /scripts


Ejecutar el script Pig:

pig -x mapreduce wordcount.pig


El script genera dos salidas en HDFS:

/output/yahoo_wordcount

/output/llm_wordcount

7. Consultar los resultados

Opcionalmente se pueden mostrar los primeros resultados desde HDFS:

hdfs dfs -cat /output/yahoo_wordcount/part* | head
hdfs dfs -cat /output/llm_wordcount/part* | head

8. Detener el sistema
docker-compose down
