# Tarea-3-Sistemas-distribuidos
Este proyecto implementa un análisis batch para comparar el vocabulario usado en respuestas humanas de Yahoo y respuestas generadas por un modelo LLM, utilizando Hadoop, HDFS y Apache Pig.  
Todo el sistema está containerizado mediante Docker y docker-compose.

---

## 1. Arquitectura General

El sistema está compuesto por los siguientes servicios:

- **Namenode**: nodo maestro de HDFS.
- **Datanode**: almacenamiento distribuido.
- **ResourceManager**: planificación de tareas YARN.
- **HistoryServer**: historial de ejecuciones.
- **Pig**: contenedor cliente utilizado para ejecutar los scripts Pig.

Los datos se encuentran en la carpeta local `./data` y los scripts Pig en `./scripts`.

---

## 2. Requisitos

- Docker  
- docker-compose  
- Archivo `responses_export.csv` dentro de `./data/`

---

## 3. Estructura del Proyecto
Tarea3/
├── data/
│ └── responses_export.csv
├── scripts/
│ └── wordcount.pig
├── Dockerfile
└── docker-compose.yml

---

## 4. Ejecutar el Análisis
# Entrar al contenedor Pig
docker exec -it pig bash
# Navegar a scripts
cd /scripts
# ejecutar
pig -x mapreduce wordcount.pig
