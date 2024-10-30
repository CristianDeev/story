import random
personajes = ["Una Princesa", "Un Mago", "Un Futbolista", "Una Viejita"]
lugares = ["En un castillo", "En el bosque", "En la casa de Adam Sandler"]
acciones = ["Lucha contra", "Hablan con", "Baila con", "Huye de"]
personaje = random.choice(personajes)
lugar = random.choice(lugares)
accion = random.choice(acciones)

if personaje == "Una Princesa":
    print("Es hora de una historia de princesas")
else:
    print("Esta historia seria de aventura")


def generar_historia():
    personaje = random.choice(personajes)
    lugar = random.choice(lugares)
    accion = random.choice(acciones)
    historia = f"{personaje} {lugar} {accion} con Chayane"
    return historia

print("Primeras Historias: \n")
for i in range(5):
  historia = generar_historia()
  print(f"Historia {i+1}: {historia}")

print("\n--------------------------\n")

# Permitir al usuario agregar nuevo personaje
newPersonaje = input("Escribe el nuevo personaje: ")
newLugar = input("Escribe el nuevo lugar: ")
newAccion = input("Escribe la nueva acción: ")
personajes.append(newPersonaje)
lugares.append(newLugar)
acciones.append(newAccion)

print("Historias nuevas: \n")
for i in range(5):
  historia = generar_historia()
  print(f"Historia {i+1}: {historia}")