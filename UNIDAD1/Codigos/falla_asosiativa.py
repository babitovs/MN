a = 1.0e20   # Un número gigante
b = -1.0e20  # El inverso del gigante
c = 3.14159  # Un número pequeño

# (A+B)+C
operacion1 = (a + b) + c

# A+(B+C)
operacion2 = a + (b + c)

print("--- Propiedad Asociativa (A+B)+C == A+(B+C) ---")
print(f"(a + b) + c = {operacion1}") # Devuelve 3.14159
print(f"a + (b + c) = {operacion2}") # Devuelve 0.0 debido a pérdida de precisión
print(f"¿Son iguales? {operacion1 == operacion2}")