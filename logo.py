# Importar las bibliotecas
from sense_hat import SenseHat
from time import sleep

# Configurar el Sense HAT
sense = SenseHat()
sense.set_rotation(270)

# Configurar el sensor de color
sense.color.gain = 60 # Establecer la sensibilidad del sensor
sense.color.integration_cycles = 64 # El intervalo en el que se tomará la lectura
# Agregar variables de color e imagen
m = (70,111,17) # Rosa Oscuro
r = (137, 170, 1) # Rosa Claro
n = (0, 0, 0) # Negro
b = (255,255,255)
for i in range(27):
    rgb = sense.color # obtener el color del sensor
    b = (rgb.red, rgb.green, rgb.blue)
    imagen = [
        b,b,b,b,b,b,b,b,
        b,b,m,m,r,b,b,b,
        b,b,m,m,m,b,b,m,
        m,b,b,b,b,b,m,m,
        m,m,b,b,b,m,m,b,
        b,m,m,b,b,m,b,b,
        b,b,m,m,m,b,b,b,
        b,b,b,m,b,b,b,b
    ]
    
    # Mostrar la imagen
    sense.set_pixels(imagen)
    sleep(1)
sense.clear()
