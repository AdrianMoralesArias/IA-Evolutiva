import pygame
import random
import math
import json
import os
import matplotlib.pyplot as plt

# Configuración inicial
pygame.init()

# Dimensiones de la ventana
WIDTH, HEIGHT = 800, 600

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Inicialización de la ventana
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("IA Evolutiva")
clock = pygame.time.Clock()

# Configuración de la simulación
POPULATION_SIZE = 100
LIFESPAN = 200
MUTATION_RATE = 0.01
OBSTACLES = [(300, 200, 200, 20), (200, 400, 400, 20)]
GOAL = (750, 50)
SAVE_FILE = "progress.json"

# Gráfica de progreso
plt.ion()
fig, ax = plt.subplots()
generations = []
best_fitnesses = []
line, = ax.plot(generations, best_fitnesses, label="Mejor Fitness")
ax.set_xlabel("Generación")
ax.set_ylabel("Fitness")
ax.legend()

class Dot:
    def __init__(self):
        self.pos = pygame.Vector2(WIDTH // 2, HEIGHT - 50)
        self.vel = pygame.Vector2(0, 0)
        self.acc = pygame.Vector2(0, 0)
        self.dna = [pygame.Vector2(random.uniform(-1, 1), random.uniform(-1, 1)) for _ in range(LIFESPAN)]
        self.step = 0
        self.dead = False
        self.reached_goal = False
        self.fitness = 0

    def apply_force(self, force):
        self.acc += force

    def update(self):
        if not self.dead and not self.reached_goal:
            if self.step < LIFESPAN:
                self.apply_force(self.dna[self.step])
                self.step += 1
            self.vel += self.acc
            self.pos += self.vel
            self.acc *= 0

            # Verificar colisiones
            if self.pos.x < 0 or self.pos.x > WIDTH or self.pos.y < 0 or self.pos.y > HEIGHT:
                self.dead = True
            for obs in OBSTACLES:
                if obs[0] < self.pos.x < obs[0] + obs[2] and obs[1] < self.pos.y < obs[1] + obs[3]:
                    self.dead = True

            # Verificar si alcanzó la meta
            if math.hypot(self.pos.x - GOAL[0], self.pos.y - GOAL[1]) < 10:
                self.reached_goal = True

    def calculate_fitness(self):
        distance_to_goal = math.hypot(self.pos.x - GOAL[0], self.pos.y - GOAL[1])
        self.fitness = 1 / (distance_to_goal + 1)
        if self.reached_goal:
            self.fitness *= 10

    def draw(self):
        color = GREEN if not self.dead else RED
        pygame.draw.circle(screen, color, (int(self.pos.x), int(self.pos.y)), 5)

    def to_dict(self):
        return {
            "dna": [(vec.x, vec.y) for vec in self.dna]
        }

    @classmethod
    def from_dict(cls, data):
        dot = cls()
        dot.dna = [pygame.Vector2(vec[0], vec[1]) for vec in data["dna"]]
        return dot

class Population:
    def __init__(self):
        self.dots = [Dot() for _ in range(POPULATION_SIZE)]
        self.generation = 1
        self.best_dot = None

    def update(self):
        for dot in self.dots:
            dot.update()

    def draw(self):
        for dot in self.dots:
            dot.draw()
        pygame.draw.circle(screen, YELLOW, GOAL, 10)
        for obs in OBSTACLES:
            pygame.draw.rect(screen, BLACK, obs)

        # Mostrar generación actual
        font = pygame.font.SysFont(None, 36)
        text = font.render(f"Generación: {self.generation}", True, BLACK)
        screen.blit(text, (10, 10))

    def evaluate(self):
        max_fitness = 0
        for dot in self.dots:
            dot.calculate_fitness()
            if dot.fitness > max_fitness:
                max_fitness = dot.fitness
                self.best_dot = dot

        for dot in self.dots:
            dot.fitness /= max_fitness

        # Actualizar la gráfica
        generations.append(self.generation)
        best_fitnesses.append(max_fitness)
        line.set_data(generations, best_fitnesses)
        ax.relim()
        ax.autoscale_view()
        fig.canvas.draw()
        fig.canvas.flush_events()

    def select(self):
        new_dots = []
        for _ in range(POPULATION_SIZE):
            parent = self.select_parent()
            child = self.clone_dot(parent)
            new_dots.append(child)
        self.dots = new_dots
        self.generation += 1

    def select_parent(self):
        index = 0
        r = random.uniform(0, 1)
        while r > 0:
            r -= self.dots[index].fitness
            index += 1
        return self.dots[index - 1]

    def clone_dot(self, parent):
        child = Dot()
        child.dna = parent.dna[:]
        self.mutate(child)
        return child

    def mutate(self, dot):
        for i in range(LIFESPAN):
            if random.uniform(0, 1) < MUTATION_RATE:
                dot.dna[i] = pygame.Vector2(random.uniform(-1, 1), random.uniform(-1, 1))

    def save(self):
        data = {
            "generation": self.generation,
            "dots": [dot.to_dict() for dot in self.dots]
        }
        with open(SAVE_FILE, "w") as f:
            json.dump(data, f)

    @classmethod
    def load(cls):
        if not os.path.exists(SAVE_FILE):
            return cls()
        with open(SAVE_FILE, "r") as f:
            data = json.load(f)
        population = cls()
        population.generation = data["generation"]
        population.dots = [Dot.from_dict(dot_data) for dot_data in data["dots"]]
        return population

# Inicialización de la población
population = Population.load()

# Bucle principal
running = True
frame = 0
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            population.save()
            running = False

    population.update()
    population.draw()

    frame += 1
    if frame == LIFESPAN:
        frame = 0
        population.evaluate()
        population.select()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()