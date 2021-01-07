from colas import colas
q1=colas()
q1.enqueue(3)
q1.enqueue(33)
q1.enqueue(23)
print(q1.to_string())

print("prueba 2 de colas")
c1={"id":1, "nombre":"Mario", "balance": 20.5}
c2={"id":2, "nombre":"Diana", "balance": 3456.5}
c3={"id":3, "nombre":"Bartolo", "balance": 1000000.0}

atencion=colas()
atencion.enqueue(c1)
atencion.enqueue(c2)
atencion.enqueue(c3)
print(atencion.to_string())
siguiente=atencion.dequeue()
print(f"Bienvenido sr.{siguiente["nombre"]}, en que podemos servirle el dia de hoy ")
print(atencion.to_string())

print("Pruebas de las colas con prioridad acotada")

from colas import BoundedPriorityQueue

maestres={"prioridad": 4, "descripcion":"maestre", personas:["Juan", "Diego H"]}
niños={"prioridad": 2, "descripcion":"niños", personas:["Santi H", "Angel H"]}
mecanicos={"prioridad": 4, "descripcion":"mecanicos", personas:["Diana Y", "Maria z"]}

cpa= BoundedPriorityQueue(7)
cpa.enqueue(maestres["prioridad"], maestres)
cpa.enqueue(niños["prioridad"], niños)
cpa.enqueue(mecanicos["prioridad"], mecanicos)
cpa.to_string()
