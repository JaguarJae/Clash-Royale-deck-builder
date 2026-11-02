# 👑 Clash Royale Deck Builder & Analyzer

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)
![License](https://img.shields.io/github/license/JaguarJae/Clash-Royale-deck-builder?color=green)
![Stars](https://img.shields.io/github/stars/JaguarJae/Clash-Royale-deck-builder?style=social)

Una herramienta en **Python** que se conecta a la API oficial de **Clash Royale** para analizar los mazos del TOP de *Path of Legend* (Camino de Leyendas) y filtrar únicamente aquellos que cumplan con el nivel mínimo requerido en tus cartas.

---

## 📌 ¿Cómo funciona?

1. **Consulta tus cartas:** Obtiene tu colección de cartas y sus niveles directamente de la API usando tu *Player Tag*.
2. **Obtiene los TOP Mazos:** Consulta la clasificación global del *Path of Legend* y extrae los mazos actuales de los mejores jugadores en paralelo (usando multithreading).
3. **Filtra por Nivel:** Compara los niveles relativos de tus cartas con el nivel mínimo (`min_level`) que le especifiques por consola y te devuelve los mazos válidos que puedes usar competitivamente.

---

## 🛠️ Tecnologías Utilizadas

* **Lenguaje:** Python 3
* **API Externa:** Official Clash Royale REST API (`api.clashroyale.com`)
* **Librerías principales:**
  * `requests` — Para consumir los endpoints HTTP de la API.
  * `python-dotenv` — Para la gestión segura de variables de entorno (`.env`).
  * `concurrent.futures` (`ThreadPoolExecutor`) — Para realizar peticiones concurrentes y acelerar la descarga de mazos del TOP.

---

## 🚀 Instalación y Configuración Local

### Requisitos Previos

* Tener instalado **Python 3.8** o superior.
* Una **API Key** válida de desarrollador de Clash Royale (puedes obtenerla gratis en [developer.clashroyale.com](https://developer.clashroyale.com/)).

### Pasos de Instalación

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/JaguarJae/Clash-Royale-deck-builder.git](https://github.com/JaguarJae/Clash-Royale-deck-builder.git)
   cd Clash-Royale-deck-builder
