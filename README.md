<div align="center">

  <a href="">[![Pytest Testing Suite](https://github.com/alvaroChico2408/innosoft-diplomas-1/actions/workflows/test.yml/badge.svg?branch=main)](https://github.com/alvaroChico2408/innosoft-diplomas-1/actions/workflows/test.yml)</a>
  <a href="">[![Snyk Vulnerability Scan](https://github.com/alvaroChico2408/innosoft-diplomas-1/actions/workflows/snyk.yml/badge.svg?branch=main)](https://github.com/alvaroChico2408/innosoft-diplomas-1/actions/workflows/snyk.yml)</a>
  <a href="">[![Commits Syntax Checker](https://github.com/alvaroChico2408/innosoft-diplomas-1/actions/workflows/commits.yml/badge.svg?branch=main)](https://github.com/alvaroChico2408/innosoft-diplomas-1/actions/workflows/commits.yml)</a>

</div>


# certificate-generator

Este es un proyecto adaptado para la organización de Caronte desde el proyecto de la asignatura EGC para crear diplomas de jornadas InnoSoft.

# Manual de Uso para el Despliegue de la Aplicación

# Despliegue en Local
## 1. Clonar el Repositorio
Clonar el repositorio por las claves SSH e inicializarlo en el IDE preferido.

## 2. Configuración de MariaDB

### 2.1 Iniciar el Servicio de MariaDB
```bash
sudo systemctl start mariadb
```

### 2.2 Asegurar la Instalación de MariaDB
Esto configurará la contraseña del usuario root.
```bash
sudo mysql_secure_installation
```

### 2.3 Acceder a MySQL como el Usuario Root
```bash
sudo mysql -u root -p
```

### 2.4 Crear las Bases de Datos Necesarias
```sql
CREATE DATABASE diplomasdb;
CREATE DATABASE diplomasdb_test;
```

### 2.5 Crear un Nuevo Usuario con Privilegios sobre las Bases de Datos
```sql
CREATE USER 'diplomasdb_user'@'localhost' IDENTIFIED BY 'diplomasdb_password';
GRANT ALL PRIVILEGES ON diplomasdb.* TO 'diplomasdb_user'@'localhost';
GRANT ALL PRIVILEGES ON diplomasdb_test.* TO 'diplomasdb_user'@'localhost';
```

### 2.6 Aplicar los Cambios y Salir de MySQL
```sql
FLUSH PRIVILEGES;
EXIT;
```

## 3. Crear y Activar el Entorno Virtual de Python

### 3.1 Crear el Entorno Virtual
```bash
python3.12 -m venv venv
```

### 3.2 Activar el Entorno Virtual
```bash
source venv/bin/activate
```

## 4. Instalar las Dependencias del Proyecto

### 4.1 Copiar el Archivo de Configuración de Ejemplo a .env
```bash
cp .env.local.example .env
```

### 4.2 Actualizar pip a la Última Versión
```bash
pip install --upgrade pip
```

### 4.3 Instalar las Dependencias del Archivo requirements.txt
```bash
pip install -r requirements.txt
```

### 4.4 Instalar el Proyecto en Modo Editable
```bash
pip install -e ./
```

## 5. Ejecutar las Migraciones de la Base de Datos

### 5.1 Aplicar las Migraciones a la Base de Datos
```bash
flask db upgrade
```

### 5.2 Crear Nuevas Migraciones si es Necesario
```bash
flask db migrate
```

## 6. Iniciar el Proyecto
```bash
flask run
```
El servidor se ejecutará en [http://localhost:5000/](http://localhost:5000/)

