from interpolacion_segmentada import interpolacion_segmentada

print("=" * 60)
print("   EJERCICIO 5: INTERPOLACION SEGMENTADA (SPLINE LINEAL)")
print("   Perfil de un terreno")
print("=" * 60)

# Datos del problema
# Puntos topograficos: (1,2), (2,3), (3,5), (4,4)
# Interpolar en x = 2.5
# Resultado esperado: 4.0

puntos = [(1.0, 2.0), (2.0, 3.0), (3.0, 5.0), (4.0, 4.0)]
x_interpolar = 2.5

print(f"\nPuntos dados: {puntos}")
print(f"Valor a interpolar: x = {x_interpolar}\n")

y_resultado, pt0, pt1 = interpolacion_segmentada(puntos, x_interpolar)

print(f"El valor x = {x_interpolar} cae en el segmento entre {pt0} y {pt1}")
print(f"\nAplicando interpolacion lineal en ese segmento:")
print(f"  y = {pt0[1]} + (({pt1[1]} - {pt0[1]}) / ({pt1[0]} - {pt0[0]})) * ({x_interpolar} - {pt0[0]})")
pendiente = (pt1[1] - pt0[1]) / (pt1[0] - pt0[0])
print(f"  y = {pt0[1]} + {pendiente} * {x_interpolar - pt0[0]}")
print(f"  y = {pt0[1]} + {pendiente * (x_interpolar - pt0[0])}")
print(f"\nResultado: y({x_interpolar}) = {y_resultado}")
