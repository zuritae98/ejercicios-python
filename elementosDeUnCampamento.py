def Primera_eleccion():
    while True:
        print("¿Sobre que tema de campismo quieres aprender un poco mas?")
        print("opcion 1 ¿te gustaria aprender sobre carpas?")
        print("opcion 2 ¿te gustaria aprender sobre fogatas?")
        print("opcion 3 ¿te gustaria aprender sobre amarres scout?")
        opcion=int(input("menciona la opcion que mas te guste"))

        if opcion == 1:
            carpa()
            print("excelente vamos a aprender un poco de sobre los tipos de carpas")
        elif opcion==2:
            fogatas()
            print("excelente vamos a aprender un poco de sobre los tipos de fogatas")
        elif opcion==3:
            amarres()
            print("excelente vamos a aprender un poco de sobre los tipos de amarres scout")
        else:
            print("opcion no es valida, por favor elige un numero entre 1 - 3")
def carpa():
    while True:
        print("unos tipos de carpas son:")
        print("opcion 1: carpa canadiense")
        print("opcion 2: carpa iglu")
        print("opcion 3: carpa tunel")
        print("opcion 4: volver al menu principal")
        opcion= int(input("menciona la opcion que mas te guste"))

        if opcion== 1:
            print("La carpa canadiense es una tienda tradicional en forma de A, hecha generalmente de lona resistente, ideal para campamentos scouts debido a su gran estabilidad, buena ventilación, resistencia al mal clima y facilidad para montarse con postes y cuerdas, lo que la convierte en una excelente opción para aprender técnicas básicas de campismo.")
        if opcion== 2:
            print("La carpa iglú es una tienda moderna de estructura curva y flexible, fácil de montar gracias a sus varillas entrecruzadas, ligera y compacta para transportar, ideal para campamentos cortos o de mochileros, ofreciendo buena resistencia al viento y una forma aerodinámica que la hace muy práctica en condiciones cambiantes.")
        if opcion== 3:
            print("La carpa tipo túnel es una tienda alargada con estructura de arcos paralelos, muy espaciosa y cómoda para grupos o familias, fácil de montar en terreno plano, con excelente ventilación y aprovechamiento del espacio interior, aunque requiere una buena fijación al suelo ya que no se sostiene por sí sola sin tensores.")
        if opcion== 4:
            break
        else:
            print("la opcion no es valida")
def fogatas():
    while True:
        print("unos tipos de fogatas son:")
        print("opcion 1: fogata tipi")
        print("opcion 2: fogata estrella")
        print("opcion 3: fogata trinchete")
        print("opcion 4: volver al menu principal")
        opcion= int(input("menciona la opcion que mas te guste"))

        if opcion==1:
            print("La fogata tipi es una fogata tradicional en forma de cono, construida colocando palos inclinados apoyados entre sí como una tienda tipi, ideal para encender rápidamente el fuego ya que permite una excelente circulación de aire, siendo perfecta para cocinar o como fuente inicial de calor en campamentos scouts.")
        if opcion==2:
            print("La fogata estrella se construye colocando troncos de madera en forma radial alrededor de un punto central, con las ramas más grandes apuntando hacia afuera, lo que permite que el fuego se mantenga constante y uniforme, ideal para mantener el calor por largo tiempo y facilitar la cocción de alimentos en campamentos scouts.")
        if opcion==3:
            print("La fogata trinchete es una fogata en la que se colocan tres troncos grandes en forma de trípode, entrelazados en la parte superior, dejando un espacio central donde se enciende el fuego; es muy útil para cocinar en el centro del fuego, permitiendo una buena distribución del calor y estabilidad para colgar ollas o utensilios de cocina en campamentos scouts")
        if opcion== 4:
            break
        else:
            print("la opcion no es valida")
def amarres():
    while True:
        print("unos tipos de de amarres scouts son:")
        print("opcion 1: amarre cuadrado")
        print("opcion 2: amarre tripode")
        print("opcion 3: amarre continuo")
        print("opcion 4: volver al menu principal")
        opcion= int(input("menciona la opcion que mas te guste"))

        if opcion==1:
            print("El amarre cuadrado es un nudo básico y muy utilizado en campismo, que se realiza cruzando dos cuerdas en forma de un cuadrado, asegurando que queden firmemente atadas sin deslizarse; es ideal para unir dos objetos de manera estable y resistente, como al montar una estructura o sujetar una carpa en campamentos scouts.")
        if opcion==2:
            print("El **amarre trípode** es un nudo utilizado para unir tres cuerdas o tres postes en forma de triángulo, creando una estructura estable y resistente, ideal para construir una base sólida para una fogata o colgar utensilios de cocina, como parte de las construcciones scouts o en actividades de campismo donde se necesita un soporte seguro.")
        if opcion==3:
            print("El amarre continuo es una técnica de amarre que se utiliza para atar varias cuerdas o elementos de forma que el nudo se mantenga firme y seguro a lo largo del tiempo, permitiendo que la cuerda se extienda sin que se deslice o se suelte; es útil en campismo para unir estructuras o asegurar objetos de manera duradera, especialmente cuando se necesita una sujeción constante y confiable.")
        if opcion== 4:
            break       
        else:
            print("la opcion no es valida")
Primera_eleccion()

            

        