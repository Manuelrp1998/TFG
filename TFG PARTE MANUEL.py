numero = 0

while numero <=5:
        print("1- Comprar PC")
        print("2- Comprar portátil")
        print("3- Comprar MAC")
        print("4- Comprar iPhone")
        opcion = int(input("Elige una opción: 1/2/3/4\n"))
        if opcion == 1:
           print("\nLa tarea elegida es comprar PC\n\n")
        elif opcion == 2: 
           print("\nLa tarea elegida es comprar portátil\n\n")
        elif opcion == 3: 
           print("\nLa tarea elegida es comprar MAC\n\n")
        elif opcion == 4:
           print("\nLa tarea elegida es comprar iPhone\n\n")
        else:
           print("Va a salir del programa")
           break