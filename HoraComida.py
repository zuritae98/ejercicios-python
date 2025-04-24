from datetime import datetime

def seleccionar_comida():
    
    hora = datetime.now().hour
    optionValida = False  

    
    while not optionValida:
        if hora < 12:
            print("Es hora del desayuno, ¿Qué quieres para desayunar?")
            print("Pulsa 1 para tostadas")
            print("Pulsa 2 para café con leche")
            print("Pulsa 3 para cereales")
            plato = int(input("¿Cuál opción eliges? "))
            if plato == 1:
                optionValida = True
                print("Disfruta de tu tostada")
            elif plato == 2:
                optionValida = True
                print("Disfruta de tu café con leche")
            elif plato == 3:
                optionValida = True
                print("Disfruta de tus cereales")
            else:
                print("Opción no válida, por favor elige una opción entre 1 y 3.")

        elif 12 <= hora < 18:
            print("Es hora de la comida, ¿Qué quieres para almorzar?")
            print("Pulsa 1 para espaguetis")
            print("Pulsa 2 para pescado al horno")
            print("Pulsa 3 para sopa de verduras")
            plato = int(input("¿Cuál opción eliges? "))
            if plato == 1:
                optionValida = True
                print("Disfruta de tus espaguetis")
            elif plato == 2:
                optionValida = True
                print("Disfruta de tu pescado al horno")
            elif plato == 3:
                optionValida = True
                print("Disfruta de tu sopa de verduras")
            else:
                print("Opción no válida, por favor elige una opción entre 1 y 3.")

        elif 18 <= hora < 20:
            print("Es hora de merienda, ¿Qué quieres para merendar?")
            print("Pulsa 1 para sandwich")
            print("Pulsa 2 para barrita energética")
            print("Pulsa 3 para yogurt")
            plato = int(input("¿Cuál opción eliges? "))
            if plato == 1:
                optionValida = True
                print("Disfruta de tu sandwich")
            elif plato == 2:
                optionValida = True
                print("Disfruta de tu barrita energética")
            elif plato == 3:
                optionValida = True
                print("Disfruta de tu yogurt")
            else:
                print("Opción no válida, por favor elige una opción entre 1 y 3.")

        elif 20 <= hora < 24:
            print("Es hora de cenar, ¿Qué quieres para cenar?")
            print("Pulsa 1 para pizza")
            print("Pulsa 2 para salchipapa")
            print("Pulsa 3 para hamburguesa")
            plato = int(input("¿Cuál opción eliges? "))
            if plato == 1:
                optionValida = True
                print("Disfruta de tu pizza")
            elif plato == 2:
                optionValida = True
                print("Disfruta de tu salchipapa")
            elif plato == 3:
                optionValida = True
                print("Disfruta de tu hamburguesa")
            else:
                print("Opción no válida, por favor elige una opción entre 1 y 3.")


seleccionar_comida()