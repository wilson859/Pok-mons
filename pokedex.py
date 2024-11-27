import csv
import random

# 1. Función para cargar el archivo CSV
def cargar_pokedex(nombre_archivo):
    pokedex = []
    with open(nombre_archivo, mode='r', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            fila = {key: (int(value) if value.isdigit() else value) for key, value in fila.items()}
            pokedex.append(fila)
    return pokedex

# 2. Función para guardar la Pokédex en un archivo CSV
def guardar_pokedex(nombre_archivo, pokedex):
    if pokedex:
        with open(nombre_archivo, mode='w', newline='', encoding='utf-8') as archivo:
            escritor = csv.DictWriter(archivo, fieldnames=pokedex[0].keys())
            escritor.writeheader()
            escritor.writerows(pokedex)

# 3. Función para agregar un nuevo Pokémon
def agregar_pokemon(pokedex, nuevo_pokemon):
    pokedex.append(nuevo_pokemon)
    print(f"Pokémon {nuevo_pokemon['name']} agregado exitosamente.")

# 4. Función para modificar un Pokémon existente
def modificar_pokemon(pokedex, pokemon_id, nuevas_caracteristicas):
    for pokemon in pokedex:
        if str(pokemon["pokedex_number"]) == str(pokemon_id) or pokemon["name"] == pokemon_id:
            pokemon.update(nuevas_caracteristicas)
            print(f"Pokémon {pokemon['name']} modificado exitosamente.")
            return
    print("Pokémon no encontrado.")

# 5. Función para eliminar un Pokémon
def eliminar_pokemon(pokedex, pokemon_id):
    for pokemon in pokedex:
        if str(pokemon["pokedex_number"]) == str(pokemon_id) or pokemon["name"] == pokemon_id:
            pokedex.remove(pokemon)
            print(f"Pokémon {pokemon['name']} eliminado exitosamente.")
            return
    print("Pokémon no encontrado.")

# 6. Función para simular una batalla entre dos Pokémon
def batalla_pokemon(pokemon1, pokemon2):
    print(f"\n¡Comienza la batalla entre {pokemon1['name']} y {pokemon2['name']}!")

    puntos1 = pokemon1["attack"] + pokemon1["speed"] - pokemon2["defense"]
    puntos2 = pokemon2["attack"] + pokemon2["speed"] - pokemon1["defense"]

    puntos1 += random.randint(-10, 10)
    puntos2 += random.randint(-10, 10)

    if puntos1 > puntos2:
        print(f"¡{pokemon1['name']} gana la batalla!")
        return pokemon1
    elif puntos2 > puntos1:
        print(f"¡{pokemon2['name']} gana la batalla!")
        return pokemon2
    else:
        print("¡La batalla termina en empate!")
        return None

# 7. Función principal para ejecutar el proyecto
def main():
    archivo_csv = 'pokemon.csv'
    pokedex = cargar_pokedex(archivo_csv)

    while True:
        print("\n--- Menú de Opciones ---")
        print("1. Agregar Pokémon")
        print("2. Modificar Pokémon")
        print("3. Eliminar Pokémon")
        print("4. Simular Batalla")
        print("5. Guardar y Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            nuevo_pokemon = {
                "pokedex_number": int(input("Número de Pokédex: ")),
                "name": input("Nombre: "),
                "type_1": input("Tipo 1: "),
                "type_2": input("Tipo 2 (opcional): ") or None,
                "attack": int(input("Ataque: ")),
                "defense": int(input("Defensa: ")),
                "speed": int(input("Velocidad: ")),
                "hp": int(input("HP: "))
            }
            agregar_pokemon(pokedex, nuevo_pokemon)

        elif opcion == '2':
            pokemon_id = input("Ingrese el número o nombre del Pokémon a modificar: ")
            nuevas_caracteristicas = {}
            while True:
                campo = input("Campo a modificar (escriba 'salir' para finalizar): ")
                if campo.lower() == 'salir':
                    break
                valor = input(f"Nuevo valor para {campo}: ")
                nuevas_caracteristicas[campo] = int(valor) if valor.isdigit() else valor
            modificar_pokemon(pokedex, pokemon_id, nuevas_caracteristicas)

        elif opcion == '3':
            pokemon_id = input("Ingrese el número o nombre del Pokémon a eliminar: ")
            eliminar_pokemon(pokedex, pokemon_id)

        elif opcion == '4':
            nombre1 = input("Nombre del primer Pokémon: ")
            nombre2 = input("Nombre del segundo Pokémon: ")
            pokemon1 = next((p for p in pokedex if p['name'] == nombre1), None)
            pokemon2 = next((p for p in pokedex if p['name'] == nombre2), None)
            if pokemon1 and pokemon2:
                batalla_pokemon(pokemon1, pokemon2)
            else:
                print("Uno o ambos Pokémon no fueron encontrados.")

        elif opcion == '5':
            guardar_pokedex(archivo_csv, pokedex)
            print("Pokédex guardada. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == '__main__':
    main()
