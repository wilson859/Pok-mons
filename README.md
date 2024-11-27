# Proyecto de Gestión de la Pokédex

Este proyecto está diseñado para gestionar una Pokédex de Pokémon, permitiendo realizar operaciones básicas como agregar, modificar y eliminar Pokémon, así como simular batallas entre ellos. El script se maneja mediante un archivo CSV que almacena la información de los Pokémon, y las modificaciones realizadas en el programa se guardan de vuelta en este archivo.

## Funciones principales

### 1. Cargar la Pokédex
La función `cargar_pokedex(nombre_archivo)` permite cargar la información de los Pokémon desde un archivo CSV. Los Pokémon se almacenan en una lista de diccionarios, donde cada diccionario contiene la información de un Pokémon.

### 2. Guardar la Pokédex
La función `guardar_pokedex(nombre_archivo, pokedex)` guarda la Pokédex actual (lista de Pokémon) en un archivo CSV, preservando la estructura de columnas y valores.

### 3. Agregar un nuevo Pokémon
La función `agregar_pokemon(pokedex, nuevo_pokemon)` permite añadir un nuevo Pokémon a la Pokédex, solicitando al usuario los detalles como el número de Pokédex, nombre, tipo, estadísticas, etc.

### 4. Modificar un Pokémon
La función `modificar_pokemon(pokedex, pokemon_id, nuevas_caracteristicas)` permite modificar las características de un Pokémon existente, ya sea por número de Pokédex o por nombre. El usuario puede elegir los campos que desea cambiar.

### 5. Eliminar un Pokémon
La función `eliminar_pokemon(pokedex, pokemon_id)` permite eliminar un Pokémon de la Pokédex, basándose en su número de Pokédex o su nombre.

### 6. Simular una batalla entre dos Pokémon
La función `batalla_pokemon(pokemon1, pokemon2)` simula una batalla entre dos Pokémon seleccionados por el usuario, comparando sus estadísticas de ataque, defensa y velocidad para determinar el ganador.

## Estructura del archivo CSV

El archivo CSV que utiliza el programa tiene las siguientes columnas:

- `pokedex_number`: Número de Pokédex del Pokémon.
- `name`: Nombre del Pokémon.
- `german_name`: Nombre del Pokémon en alemán.
- `japanese_name`: Nombre del Pokémon en japonés.
- `generation`: Generación a la que pertenece el Pokémon.
- `status`: Estado del Pokémon (si está disponible o no).
- `species`: Especie del Pokémon (ej. "Seed", "Lizard", etc.).
- `type_number`: Número de tipos del Pokémon.
- `type_1`: Tipo primario del Pokémon (ej. "Fire", "Water").
- `type_2`: Tipo secundario del Pokémon (opcional).
- `height_m`: Altura del Pokémon en metros.
- `weight_kg`: Peso del Pokémon en kilogramos.
- `abilities_number`: Número de habilidades del Pokémon.
- `ability_1`, `ability_2`, `ability_hidden`: Habilidades del Pokémon.
- `total_points`: Suma total de las estadísticas del Pokémon.
- `hp`, `attack`, `defense`, `sp_attack`, `sp_defense`, `speed`: Estadísticas individuales del Pokémon.
- `catch_rate`: Tasa de captura del Pokémon.
- `base_friendship`: Amistad base del Pokémon.
- `base_experience`: Experiencia base del Pokémon.
- `growth_rate`: Tasa de crecimiento del Pokémon.
- `egg_type_number`: Número de tipos de huevo.
- `egg_type_1`, `egg_type_2`: Tipos de huevo del Pokémon.
- `percentage_male`: Porcentaje de Pokémon macho.
- `egg_cycles`: Ciclos de huevo para la eclosión.
- `against_*`: Eficiencia del Pokémon contra otros tipos.

### Ejemplo de fila en el archivo CSV:

```csv
pokedex_number,name,german_name,japanese_name,generation,status,species,type_number,type_1,type_2,height_m,weight_kg,abilities_number,ability_1,ability_2,ability_hidden,total_points,hp,attack,defense,sp_attack,sp_defense,speed,catch_rate,base_friendship,base_experience,growth_rate,egg_type_number,egg_type_1,egg_type_2,percentage_male,egg_cycles,against_normal,against_fire,against_water,against_electric,against_grass,against_ice,against_fight,against_poison,against_ground,against_flying,against_psychic,against_bug,against_rock,against_ghost,against_dragon,against_dark,against_steel,against_fairy
1,Bulbasaur,Bulbasaur,フシギダネ,1,Available,Seed,2,Grass,Poison,0.7,6.9,2,Overgrow,Chlorophyll,,318,45,49,49,65,65,45,45,50,64,medium_slow,2,Monster,Grass,87.5,20,1,1,1,1,1,1,1,1,1,1,1,1,1,1
