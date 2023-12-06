import math

def coordenadas_polares_a_cartesianas(r, theta):
    # Convertir el ángulo de grados a radianes
    theta_rad = math.radians(theta)
    
    # Calcular las coordenadas cartesianas
    x = r * math.cos(theta_rad)
    y = r * math.sin(theta_rad)
    
    return x, y

# Ejemplo de uso
r = 5
theta = 30  # Ángulo en grados

x, y = coordenadas_polares_a_cartesianas(r, theta)
print(f"Coordenadas polares ({r}, {theta}°) se convierten en coordenadas cartesianas: ({x}, {y})")
