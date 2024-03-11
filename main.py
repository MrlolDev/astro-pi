# Importar las bibliotecas
from sense_hat import SenseHat
from time import sleep

# Configurar el Sense HAT
sense = SenseHat()
sense.set_rotation(270)

# Configurar el sensor de color
sense.color.gain = 60 # Establecer la sensibilidad del sensor
sense.color.integration_cycles = 64 # El intervalo en el que se tomará la lectura
for i in range(28):
    # Agregar variables de color e imagen
    m = (255,201,210) # Rosa Oscuro
    r = (252, 163, 177) # Rosa Claro
    q = (0, 0, 0) # Negro
    y = (189,121,132) # Rosa Oscuro
    t = (111,57,57) # Rosa profundo
    b = (255,255,255)
    imagen = [
    r,r,r,r,r,r,r,r,
    r,r,r,r,r,r,r,r,
    r,r,r,r,r,r,r,r,
    q,b,r,r,r,r,b,q,
    r,r,m,m,m,m,r,r,
    r,r,t,y,y,t,r,r,
    r,r,m,m,m,m,r,r,
    r,r,r,r,r,r,r,r
    ]
    
    # Mostrar la imagen
    sense.set_pixels(imagen)
    sleep(1)
sense.clear()
