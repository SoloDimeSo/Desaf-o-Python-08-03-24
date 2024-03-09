import sys

if len(sys.argv) < 2:
    print("Debe decir nombre de archivo")
else:
    with open(sys.argv[1], "r") as archivo:
        texto = archivo.read()
        
        Palabra = len(set(texto.split(" ")))
        print(f"El total de las palabras unicas del texto es {sys.argv[1]} son:{Palabra}")
        letras = len(set(texto))
        print(f"El total de las letras unicas del texto es {sys.argv[1]} son:{letras}")
