import numpy as np
import matplotlib.pyplot as plt


def plot_contact_angle(angle_degrees):
    angle_radians = np.radians(angle_degrees)

    # Parâmetros para a gota de líquido
    r = 1
    x = np.linspace(-r, r, 1000)
    y = np.sqrt(r ** 2 - x ** 2)

    # Plotando a gota de líquido
    plt.plot(x, y, label='Líquido')

    # Plotando a superfície sólida
    plt.axhline(0, color='gray', linestyle='--', label='Superfície sólida')

    # Plotando o ângulo de contato
    x_angle = np.linspace(0, r * np.cos(angle_radians), 100)
    y_angle = x_angle * np.tan(angle_radians)
    plt.plot(x_angle, y_angle, linestyle=':', color='red', label=f'Ângulo: {angle_degrees}°')
    plt.legend()

    # Configurando o gráfico
    plt.title('Ilustração do ângulo de contato')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.axis('equal')
    plt.grid(True)
    plt.show()


# Altere o ângulo de contato aqui (em graus)
contact_angle_degrees = 45
plot_contact_angle(contact_angle_degrees)
