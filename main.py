def main():
  print("Hello learners!")

import urllib.request
import json

def dish_fetch(num):
    enlace = f"https://api-colombia.com/api/v1/TypicalDish/{num}"
    respuesta = urllib.request.urlopen(enlace)
    return json.loads(respuesta.read().decode('utf-8'))

def main():
    print("Hello learners!")
    
    while True:
        print("\n--- MENÚ DE PLATOS ---")
        entrada = input("Ingresa el número del plato (o escribe 'salir' para terminar): ")
        
        if entrada.lower() == 'salir':
            print("¡Hasta luego!")
            break
            
        try:
            num = int(entrada)
            plato = dish_fetch(num)
            
            print("\nResultado:")
            print("Plato:", plato.get('name'))
            print("Descripcion:", plato.get('description'))
        except Exception:
            print("Hubo un error o el plato no existe. Intenta con otro número.")

if __name__ == "__main__":
    main()