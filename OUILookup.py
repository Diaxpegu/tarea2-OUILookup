import requests
import getopt
import sys
import time

def obtener_detalles_mac(mac):
    """Consulta el fabricante de una dirección MAC usando la API de maclookup.app."""
    url = f"https://api.maclookup.app/v2/macs/{mac}"
    try:
        respuesta = requests.get(url)
        respuesta.raise_for_status()  # Levanta una excepción si la respuesta es un error HTTP
        datos = respuesta.json()
        
        if 'success' in datos and datos['success'] and 'company' in datos and datos['company']:
            return datos['company']
        else:
            return "Not found"
    except requests.exceptions.HTTPError:
        return "Not found"
    except Exception as e:
        return f"Ha ocurrido un error: {str(e)}"

def mostrar_detalles_mac(mac):
    """Muestra detalles de la dirección MAC."""
    tiempo_inicio = time.time()
    fabricante = obtener_detalles_mac(mac)
    tiempo_respuesta = (time.time() - tiempo_inicio) * 1000  # Convertir a milisegundos

    print(f"Dirección MAC : {mac}")
    print(f"Fabricante : {fabricante}")
    print(f"Tiempo de respuesta: {int(tiempo_respuesta)}ms")

def main(argv):
    """Función principal que maneja los argumentos y ejecuta la aplicación."""
    try:
        opciones, argumentos = getopt.getopt(argv, "", ["mac=", "help"])
    except getopt.GetoptError:
        print('Uso: python OUILookup.py --mac <mac> | [--help]')
        sys.exit(2)

    for opt, arg in opciones:
        if opt == "--mac":
            mac = arg
            mostrar_detalles_mac(mac)
        elif opt == "--help":
            print('Uso: python OUILookup.py --mac <mac> | [--help]')
            print('--mac: MAC a consultar. P.e. aa:bb:cc:00:00:00.')
            print('--help: muestra este mensaje y termina.')
            sys.exit()
        else:
            print('Uso: python OUILookup.py --mac <mac> | [--help]')
            sys.exit(2)

if __name__ == "__main__":
    main(sys.argv[1:])
