# Mad Libs Game 
# F-String Reemplazar valores de una Variable con Clean Code

print("Completa los espacios en blanco con lo primero que pienses para así obtener una historia sin igual: \n ¡Progamar es tan ________! Siempre me emociona porque encanta ________ problemas. !Aprende a _______ con FreeCodeCamp y alcanza tus _________! ")

adj = input("Adjetivo #1: ")
verbo1 = input("Verbo #2: ")
verbo2 = input("Verbo #3: ")
sustantivo_plural = input("Sustantivo(plural): ")
madlibs = f"¡Progamar es tan {adj}! Siempre me emociona porque encanta {verbo1} problemas. !Aprende a {verbo2} con FreeCodeCamp y alcanza tus {sustantivo_plural}!" #Alt + Z Aparesca la misma linea dividida 

print(madlibs)
