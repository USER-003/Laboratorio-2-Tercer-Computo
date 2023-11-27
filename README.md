# Laboratorio 2 Tercer Computo

Guía de trabajo semana 19 (A1)

## Entorno Virtual

Instalación de librerías necesarias dentro del entorno virtual

```bash
pip install -r requirements.txt
```

## Restaurar la Base de Datos

1. Asegúrate de tener PostgreSQL instalado en tu máquina.
2. Crea una nueva base de datos en PostgreSQL.
3. Desde la terminal, ejecuta el siguiente comando para restaurar la base de datos:

```bash
psql -U tu_usuario -h localhost -d nombre_de_tu_base_de_datos < Database/dump.sql
```

4. Realiza la conexión a la bd utilizando PostreSql, modificando el string de
   conexión que se encuentra en el archivo de “settings.py”

## Uso

Corre la aplicación

```bash
python manage.py runserver
```

## Desarrolladores

- Jefferson Esperanza (SMSS132422)
- Sofia Romero (SMSS042622)
- Gerson Argueta(SMSS021722)
