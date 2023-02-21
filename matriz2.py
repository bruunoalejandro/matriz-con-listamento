colores =[

[["verde","amarillo","azul"],["rojo","blanco","verde"],["amarillo",
"naranjo","azul"]],

[["verde","amarillo","azul"],["rojo","blanco","verde"],["amarillo",
"naranjo","azul"]],

[["verde","amarillo","azul"],["rojo","blanco","verde"],["amarillo",
"naranjo","azul"]] ]
contVerde=0
contAmarillo=0
contAzul=0
contRojo=0
contBlanco=0
contNaranjo=0
for i in range(3):
    for j in range(3):
        for k in range(3):
            if (colores[i][j][k] == "verde"):
                contVerde = contVerde + 1
            if (colores[i][j][k] == "rojo"):
                contRojo = contRojo + 1
            if (colores[i][j][k] == "azul"):
                contAzul = contAzul + 1
            if (colores[i][j][k] == "naranjo"):
                contNaranjo = contNaranjo + 1
            if (colores[i][j][k] == "blanco"):
                contBlanco = contBlanco + 1
print("La cantidad de rojos es: ", contRojo)
print("La cantidad de naranjos es: ", contNaranjo)
print("La cantidad de verdes es: ", contVerde)
print("La cantidad de azul es: ", contAzul)
print("La cantidad de blanco es: ", contBlanco)