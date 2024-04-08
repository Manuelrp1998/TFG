tareas = {
    "1": "Arreglar el ascensor", 
    "2": "Reparar la nevera", 
    "3": "Regar los jardines", 
    "4": "Limpiar las ventanas"
}
print(tareas)

opcion = int(input("Elige una opción:\n"))
numero_tarea = tareas.keys()

while tareas.keys() == numero_tarea:
    if opcion == 1:
        print("\nTarea elegida: ", tareas[str(opcion)])
    elif opcion == 2: 
        print("\nTarea elegida: ", tareas[str(opcion)])
    elif opcion == 3: 
        print("\nTarea elegida: ", tareas[str(opcion)])
    elif opcion == 4:
        print("\nTarea elegida: ", tareas[str(opcion)])
    else:
        print("Va a salir del programa")
        break