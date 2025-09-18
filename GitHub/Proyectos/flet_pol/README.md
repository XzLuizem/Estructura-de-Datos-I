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

*Desarrolo de una app usando estructuras de datos, proyecto del curso ED1 - UAGRM*

## Características

- **Gestión de polinomios:** Permite a los usuarios sumar y restar polinomios.

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
    cd Estructura-de-Datos-I/GitHub/Proyectos/flet_pol
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

5.  **Verifica que pip funcione:**
    ```bash
    pip --version
    ```
    

6.  **Instala las dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

7.  **Actualiza Flet:**
    ```bash
    pip install --upgrade flet
    ```

8.  **Ejecuta la aplicación:**
    ```bash
    python pol_main.py
    ```

## Estructura del Proyecto

El proyecto sigue una arquitectura Modelo-Vista-Controlador (MVC) para separar las responsabilidades y mejorar la mantenibilidad del código.

```
flet_app/
├── pol_controller.py  # Controlador: Maneja la lógica de la aplicación y la interacción del usuario.
├── pol_main.py        # Punto de entrada: Inicializa y ejecuta la aplicación Flet.
├── pol_model.py       # Modelo: Gestiona los datos y la lógica de negocio.
├── pol_view.py        # Vista: Define y construye la interfaz de usuario.
├── requirements.txt    # Lista de dependencias de Python.
└── README.md           # Este archivo.
```

---
Desarrollado por [XzLuizem](https://github.com/XzLuizem)