lab.to_string()
# imprimir la Pila
lab.imprimir_camino()

while  not lab.es_salida( lab.get_pos_actual()[0] , lab.get_pos_actual()[1] ) :
    print("probar")
    lab.resolver_laberinto()
    lab.imprimir_camino()
    time.sleep(1.0)
