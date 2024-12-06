# IA Evolutiva en Pygame

Este proyecto implementa una inteligencia artificial (IA) evolutiva utilizando Pygame. La IA consiste en puntos verdes que aprenden a evitar obstáculos y los bordes de la ventana, mientras intentan alcanzar un objetivo (punto amarillo). El sistema utiliza un algoritmo genético para mejorar el comportamiento de los puntos a través de generaciones.

## Características
- **Simulación visual:** Cada punto sigue una trayectoria basada en un ADN predefinido.
- **Evolución por generaciones:** Los puntos se evalúan según su capacidad para alcanzar el objetivo evitando colisiones.
- **Obstáculos y bordes:** Los puntos deben evitar tanto obstáculos predefinidos como los bordes de la ventana.
- **Visualización de generaciones:** La generación actual se muestra en la esquina superior izquierda.

## Requisitos
- Python 3.7 o superior
- Biblioteca Pygame

## Instalación
1. Clona este repositorio o descarga los archivos.
2. Instala Pygame si aún no lo tienes:
   ```bash
   pip install pygame
   ```

## Cómo ejecutar
1. Ejecuta el script `main.py`:
   ```bash
   main.py
   ```
2. Observa cómo los puntos evolucionan para alcanzar el objetivo mientras evitan los obstáculos.

## Estructura del código
- **Ventana:** Dimensiones de 800x600 píxeles.
- **Puntos:** Cada punto tiene un ADN que define su trayectoria durante una vida útil.
- **Objetivo:** Representado por un círculo amarillo.
- **Obstáculos:** Rectángulos negros en posiciones predefinidas.
- **Bordes:** Considerados como "muros" que eliminan a los puntos si los tocan.

## Parámetros personalizables
Puedes modificar estos parámetros en el código:
- `POPULATION_SIZE`: Tamaño de la población de puntos (predeterminado: 100).
- `LIFESPAN`: Duración de cada generación en cuadros (predeterminado: 200).
- `MUTATION_RATE`: Probabilidad de mutación en el ADN (predeterminado: 0.01).
- `OBSTACLES`: Lista de obstáculos definidos como `(x, y, ancho, alto)`.
- `GOAL`: Coordenadas del objetivo como `(x, y)`.

## Cómo funciona
1. **Inicialización:** Se genera una población de puntos con ADN aleatorio.
2. **Simulación:** Cada punto se mueve según su ADN. Si un punto colisiona con un obstáculo, un borde o alcanza el objetivo, se detiene.
3. **Evaluación:** Al final de cada generación, se calcula la aptitud de cada punto basada en su distancia al objetivo. Los puntos que alcanzan el objetivo tienen una aptitud mayor.
4. **Selección y reproducción:** Los puntos más aptos se seleccionan para generar la próxima generación, con posibilidad de mutación en el ADN.
5. **Repetición:** El proceso continúa durante múltiples generaciones, mejorando el comportamiento de los puntos.

## Capturas de pantalla
![image](https://github.com/user-attachments/assets/e7b2cef0-7244-4e42-93af-0f26b911226d)
![image](https://github.com/user-attachments/assets/ed411299-d5c1-40dd-8122-effdc573bee2)



## Contribuciones
Las contribuciones son bienvenidas. Si encuentras errores o tienes ideas para mejorar, siéntete libre de abrir un issue o enviar un pull request.

## Licencia
Este proyecto está bajo la Licencia MIT. Puedes usarlo, modificarlo y distribuirlo libremente.

---

## 📫 Contacto
- **Email:** [adrianmoralesariascontacto@gmail.com](mailto:adrianmoralesariascontacto@gmail.com)
- **GitHub:** [github.com/AdrianMoralesArias](https://github.com/AdrianMoralesArias)
- **LinkedIn:** [linkedin.com/in/AdrianMoralesArias](https://www.linkedin.com/in/adrian-morales-arias-3593b733b/)

---

