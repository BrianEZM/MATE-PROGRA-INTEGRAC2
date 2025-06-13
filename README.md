# Trabajo Integrador 2: Matemática y Programación - UTN Tecnicatura en Programación.
Integrantes: Brian Zapata Marin y Matias Almeida.

Este repositorio contiene el desarrollo del Trabajo Integrador Semana-2: Matemática y Programación. Enfocado en la aplicación de conceptos de teoría de conjuntos y lógica booleana a través de la programación en Python.

El proyecto aborda la manipulación y análisis de dígitos provenientes de números de DNI y años de nacimiento, aplicando diversas operaciones de conjuntos y evaluando condiciones lógicas.

## Descripción del Proyecto

El objetivo principal de este trabajo es integrar conocimientos de matemática (teoría de conjuntos y lógica) con habilidades de programación en Python (estructuras condicionales, repetitivas y funciones). El proyecto está dividido en dos partes principales:

1.  **Desarrollo Matemático (Parte Teórica):** Análisis de los números de DNI de los integrantes del grupo para formar conjuntos de dígitos únicos y realizar operaciones de unión, intersección, diferencia y diferencia simétrica. Además, se definen expresiones lógicas en lenguaje natural y se predice su resultado. (Esta parte se presenta en un PDF aparte: https://drive.google.com/drive/folders/1bpXtErtJJTzV2k61mV5HGWYSzF56UcPi).
2.  **Desarrollo del Programa en Python (Parte Práctica):** Implementación de la lógica matemática desarrollada, incluyendo:
    * Generación automática de conjuntos de dígitos a partir de DNIs.
    * Cálculo y visualización de operaciones de conjuntos.
    * Conteo de frecuencia y suma de dígitos en los DNIs.
    * Evaluación de condiciones lógicas predefinidas.
    * Análisis de años de nacimiento (conteo de pares/impares, detección de bisiestos).
    * Cálculo del producto cartesiano entre años y edades.

Este README se centra en la parte práctica (el código Python).
(La parte teorica con diagranas de Venn se presenta en un PDF aparte: https://drive.google.com/drive/folders/1bpXtErtJJTzV2k61mV5HGWYSzF56UcPi).

## 📁 Estructura del Repositorio

El repositorio está organizado de la siguiente manera:

* `main.py`: Archivo principal del programa. Se encarga de la ejecución, la definición de los datos ficticios del grupo y la orquestación de las llamadas a las funciones de servicio.
* `servicios_operaciones.py`: Módulo que contiene todas las funciones lógicas y de cálculo para las operaciones con DNIs y años de nacimiento. Este módulo encapsula la lógica del negocio.
* `README.md`: Este archivo, que proporciona una descripción del proyecto y cómo usarlo.
