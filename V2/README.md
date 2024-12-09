# IA Evolutiva en Pygame V2

Este proyecto implementa una inteligencia artificial (IA) evolutiva utilizando Pygame y un algoritmo genético. Los puntos (representados en verde) aprenden a evitar obstáculos y alcanzan el objetivo (punto amarillo), mejorando su comportamiento a través de generaciones.

## Características
- **Visualización en tiempo real:** Los puntos, obstáculos y objetivo se representan gráficamente en una ventana.
- **Evolución persistente:** El progreso de la simulación se guarda automáticamente y se puede cargar en sesiones posteriores.
- **Gráfica de rendimiento:** Se muestra una gráfica en tiempo real del mejor y promedio de fitness de cada generación.
- **Personalización sencilla:** Ajusta parámetros como el tamaño de la población, tasa de mutación y más.

## Requisitos
- Python 3.7 o superior
- Bibliotecas Pygame y Matplotlib

## Instalación
1. Clona este repositorio o descarga los archivos.
2. Instala las dependencias necesarias:
   ```bash
   pip install pygame matplotlib
   ```

## Cómo ejecutar
1. Ejecuta el script `main.py`:
   ```bash
   python main.py
   ```
2. Observa cómo los puntos evolucionan para alcanzar el objetivo mientras evitan los obstáculos.

## Estructura del código
- **Ventana:** Dimensiones de 800x600 píxeles.
- **Puntos:** Cada punto tiene un ADN que define su trayectoria durante una vida útil.
- **Objetivo:** Representado por un círculo amarillo.
- **Obstáculos:** Rectángulos negros en posiciones predefinidas.
- **Gráfica:** Muestra el progreso de fitness a lo largo de las generaciones.

## Parámetros personalizables
Puedes modificar estos parámetros en el archivo `main.py`:
- `POPULATION_SIZE`: Tamaño de la población de puntos (predeterminado: 100).
- `LIFESPAN`: Duración de cada generación en cuadros (predeterminado: 200).
- `MUTATION_RATE`: Probabilidad de mutación en el ADN (predeterminado: 0.01).
- `OBSTACLES`: Lista de obstáculos definidos como `(x, y, ancho, alto)`.
- `GOAL`: Coordenadas del objetivo como `(x, y)`.

## Cómo funciona
1. **Inicialización:** Se genera una población inicial con ADN aleatorio.
2. **Simulación:** Cada punto se mueve según su ADN. Los puntos colisionan con obstáculos, bordes o alcanzan el objetivo.
3. **Evaluación:** Se calcula la aptitud de cada punto con base en su distancia al objetivo. Los puntos que alcanzan el objetivo obtienen mayor puntuación.
4. **Selección y reproducción:** Los puntos más aptos se seleccionan para generar la próxima generación, con posibilidad de mutación.
5. **Progreso persistente:** El estado de la simulación se guarda en un archivo `progress.json` al cerrar el programa y se carga automáticamente al reiniciar.

## Capturas de pantalla
![image](https://github.com/user-attachments/assets/fdb6a90a-5e96-47e9-9dc8-286054c7c26c)

![image](https://github.com/user-attachments/assets/6007bb46-520b-4a8c-bf1c-5a05883dc25e)

## Contribuciones
Las contribuciones son bienvenidas. Si encuentras errores o tienes ideas para mejorar, abre un issue o envía un pull request.

## Licencia
Este proyecto está bajo la Licencia MIT. Puedes usarlo, modificarlo y distribuirlo libremente.

---

## 📫 Contacto
- **Email:** [adrianmoralesariascontacto@gmail.com](mailto:adrianmoralesariascontacto@gmail.com)
- **GitHub:** [github.com/AdrianMoralesArias](https://github.com/AdrianMoralesArias)
- **LinkedIn:** [linkedin.com/in/AdrianMoralesArias](https://www.linkedin.com/in/adrian-morales-arias-3593b733b/)
