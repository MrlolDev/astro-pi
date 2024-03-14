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
m = (255,201,210) # Rosa Oscuro
r = (255, 118, 185) # Rosa Claro
q = (0, 0, 0) # Negro
y = (189,121,132) # Rosa Oscuro
t = (111,57,57) # Rosa profundo
b = (255,255,255)
for i in range(25):
    rgb = sense.color # obtener el color del sensor
    r = (rgb.red, rgb.green, rgb.blue)
    imagen = [
    t,t,r,r,r,r,t,t,
    r,t,r,r,r,r,t,r,
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
