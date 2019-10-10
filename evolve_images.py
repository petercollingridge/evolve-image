import random
import pygame
from pygame import *


pygame.init()

LINES = 128
POPULATION_SIZE = 16
BACKGROUND = (255, 255, 255)
INK_COLOR = (0, 0, 0)
MAX_THICKNESS = 16


def get_image(filename):
    try:
        return pygame.image.load('checkerboard.png')
    except:
        print("Couldn't load image.")


def evolve_image(target_image):
    image_size = target_image.get_size()
    (width, height) = image_size

    # Maximum value for each gene parameter
    # Values represent, x, y1, y2, and thickness
    max_values = (width, height, height, MAX_THICKNESS)

    # Get an initial population of random genomes
    population = [initilise_genome(LINES, max_values) for _ in range(POPULATION_SIZE)]

    genome_surface = pygame.Surface(image_size)

    for genome in population:
        genome_image = get_phenotype(genome, genome_surface)
        fitness = get_fitness(genome_image, target_image, width, height)

    # screen = pygame.display.set_mode(image_size)
    # display_image(screen, genome_image)


def display_image(screen, image):
    screen.blit(image, (0, 0))
    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


def initilise_genome(number_of_genes, max_values):
    genome = []
    for _ in range(number_of_genes):
        genome += [random.randint(0, max_value) for max_value in max_values]
    return genome


def get_phenotype(genome, surface):
    surface.fill(BACKGROUND)

    for i in range(0, len(genome), 4):
        pygame.draw.line(
            surface,
            INK_COLOR,
            (genome[i], genome[i + 1]),
            (genome[i], genome[i + 2]),
            genome[i + 3]
        )

    return surface


def get_fitness(source, target, width, height):
    d = 0

    for x in range(width):
        for y in range(height):
            (r1, g1, b1, a) = source.get_at((x, y))
            (r2, g2, b2, a) = target.get_at((x, y))
            # d += (r1 - r2) ** 2 + (g1 - g2) ** 2 + (b1 - b2) ** 2
            d += (r1 - r2) * (r1 - r2)

    return d

if __name__ == '__main__':
    target_image = get_image('checkerboard.png')
    evolve_image(target_image)
