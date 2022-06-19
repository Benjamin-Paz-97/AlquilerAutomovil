def Alquiler_Horas(Horas,precio):
    cont = 0
    Costo = 0 
    Costo = Horas * precio
    while (Horas > 10):
        Horas = Horas - 10
        cont = cont + 1     
    Costo = Costo - (cont * precio);	
    return Costo


#descuento por dia es del 10% cuando es 2 dias a 5, 15% de 5 a una semana, y 18% si es mas de una semaa.
#pero con una taza de precio fijo que es de 5 la hora

def Alquiler_Dia( Dias):
	precio = 5	
	if (Dias > 7):
		Costo = ((precio * 24) * Dias) - (((precio * 24) * Dias) * 0.18)
	else:
		if (Dias > 5 and Dias <= 7):
			Costo = ((precio * 24) * Dias) - (((precio * 24) * Dias) * 0.15)
		else:
			if (Dias > 1 and Dias <= 5):
				Costo = ((precio * 24) * Dias) - (((precio * 24) * Dias) * 0.10)
			else:
				Costo = precio * 24
	return Costo

#Precio de alquiler por kilometro recorrido, precio 1.5 soles por kilometro

def Alquiler_km(km):
	Costo = km * 1.5
	return Costo

horas = 11 
precio = 2
Dia = 8
km = 120
print("el precio del alquiler por horas es : S/." + str(Alquiler_Horas(horas, precio)))
print("el precio del alquiler por horas es : S/."+ str(Alquiler_Dia(Dia)))
print("el precio del alquiler por Kilometro recorrido es : S/."+ str(Alquiler_km(km)))
