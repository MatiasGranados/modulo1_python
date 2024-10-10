def promedio(listado):
  suma_notas = float(sum(listado))
  prom = (suma_notas / 3)
  return(print("EL PROMEDIO ES:",round(prom, 2)))
listado = []
for i in range(0, 3):
  nota = float(input("INGRESE NOTA:"))
  listado.append(nota)
pass
promedio(listado)