# Asignamos valores iniciales a las variables
j, k = 90, 56   # j = 90, k = 56

# Sumamos ambos valores y lo guardamos en j
j = j + k       # j = 90 + 56 = 146   → ahora j tiene la suma total de ambos números

# Restamos el valor actual de k a j (que contiene la suma)
# Esto nos da el valor original de j, así que lo guardamos en k
k = j - k       # k = 146 - 56 = 90   → k ahora tiene el valor original de j

# Restamos el nuevo valor de k (que es el valor original de j) a j (que es la suma)
# Esto nos da el valor original de k, así que lo guardamos en j
j = j - k       # j = 146 - 90 = 56   → j ahora tiene el valor original de k

# Mostramos los resultados finales
print("x:", j)  # j = 56
print("k:", k)  # k = 90


