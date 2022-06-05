#Variables para una calificación

calificacion = input("Introduce tu calificación de la AZ-900: ")

calificacion = int(calificacion)

#If en una sola linea
if calificacion < 700 : 
    print("Reprobaste por no estudiar")
elif calificacion > 1000:
    print("Mientes!!! Eso es mentira")
else :
    print("Aprobaste")

#Verificar de mayoria de edad

edad = input("Introduce tu edad ")
edad = int(edad)

if edad >= 18 and edad<=100 :
    print("Bienvenido al manitas")
elif edad > 100:
 print("Si vienes acompañado de tus abuelitos, si te podemos fiar")
elif edad < 0:
    print("No manches")
else:
    print("Eres un chamaco")

    #En python no hay swtich case