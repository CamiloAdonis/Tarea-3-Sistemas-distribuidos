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
```tree
Tarea3/
│
├── data/
│   └── responses_export.csv
│
├── scripts/
│   └── wordcount.pig
│
├── graficos.py 
├── Dockerfile
└── docker-compose.yml
```
---

## 4. Construir contenedores
```bash
docker-compose build pig
docker-compose up -d
```
---

## 5. Ejecutar el Análisis

# Entrar al contenedor Pig
```bash
docker exec -it pig bash
```
# Navegar a scripts
```bash
cd /scripts
```
# ejecutar
```bash
pig -x mapreduce wordcount.pig
```
# salir
```bash
exit
```
---

## 6 Generación de Gráficos

### Prerrequisitos
```bash
pip install matplotlib pandas wordcloud
```
### Ejecutar análisis visual
```bash
python graficos.py
```
