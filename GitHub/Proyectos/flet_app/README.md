# Proyecto con Flet

Una aplicación de escritorio desarrollada con el framework Flet para Python, siguiendo el patrón de diseño Modelo-Vista-Controlador (MVC).

## Tabla de Contenidos

- [Proyecto con Flet](#proyecto-con-flet)
  - [Tabla de Contenidos](#tabla-de-contenidos)
  - [Descripción](#descripción)
  - [Características](#características)
  - [Requisitos Previos](#requisitos-previos)
  - [Instalación y Ejecución](#instalación-y-ejecución)
  - [Estructura del Proyecto](#estructura-del-proyecto)

## Descripción

*Desarrollo de una app usando estructuras de datos desde una plantilla base, proyecto del curso ED1 - UAGRM*

## Características

- **Gestion de un incrementador:** Permite a los usuarios imcrementar un numero.

## Requisitos Previos

- Python 3.8 o superior
- Git

## Instalación y Ejecución

Sigue estos pasos para configurar y ejecutar el proyecto en tu máquina local.

1.  **Clona el repositorio:**
    - **HTTPS:**
      
    ```bash
    git clone https://github.com/XzLuizem/Estructura-de-Datos-I.git
    ```
    - **SSH:**
    ```bash
    git clone git@github.com:XzLuizem/Estructura-de-Datos-I.git
    ```

2.  **Navega al directorio del proyecto:**
    ```bash
    cd Estructura-de-Datos-I/GitHub/Proyectos/flet_app
    ```

3.  **Crea un entorno virtual:**
    ```bash
    python -m venv venv
    ```

4.  **Activa el entorno virtual:**
    - **Windows:**
      ```bash
      venv\Scripts\activate
      ```
    - **macOS/Linux:**
      ```bash
      source venv/bin/activate
      ```

5.  **Instala las dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

6.  **Ejecuta la aplicación:**
    ```bash
    python main_flet.py
    ```

## Estructura del Proyecto

El proyecto sigue una arquitectura Modelo-Vista-Controlador (MVC) para separar las responsabilidades y mejorar la mantenibilidad del código.

```
flet_app/
├── controller_flet.py  # Controlador: Maneja la lógica de la aplicación y la interacción del usuario.
├── main_flet.py        # Punto de entrada: Inicializa y ejecuta la aplicación Flet.
├── model_flet.py       # Modelo: Gestiona los datos y la lógica de negocio.
├── view_flet.py        # Vista: Define y construye la interfaz de usuario.
├── requirements.txt    # Lista de dependencias de Python.
└── README.md           # Este archivo.
```

---
Desarrollado por [XzLuizem](https://github.com/XzLuizem)