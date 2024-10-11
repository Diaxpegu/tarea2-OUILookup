#Integrantes

- Diego Peña Gutièrrez - diego.penag@alumnos.uv.cl

#OUILookup
OUILookup es una herramienta en Pythom que consulta sobre los fabricantes de direcciones MAC, al utilizar una API para obtener detalles del fabricante asociado a una MAC especifica.

#Caracteristicas
-Consilta el fabricante de una direcciòn MAC.
-Muestra una tabla ARP simulada con ejemplos de direcciones MAC y sus fabricantes
-Soporta argumentos de linea de comandos para facilitar su uso.

#Requisitos
-Python 3.x
-Biblioteca "requests"

#Instalaciòn
pip install requests
git clone https://github.com/Diaxpegu/tarea2-OUILookup
cd OUILookup

#Uso
-Consultar un fabricante por direcciòn MAC
python3 OUILookup --mac <mac>
Ejemplo
python3 OUILookup --mac aa:bb:cc:00:00:00

-Mostrar tabla ARP simulada
python3 OUILookup --arp
-Ayuda
python3 OUILookup --help

