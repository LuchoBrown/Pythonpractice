#def saludo(name):
    #return ("Bienvenido " + name)

#Saludo_a = saludo("Lucho") 
#print (Saludo_a)

def get_seconds(hours, minutes, seconds):
    return 3600*hours + 60*minutes + seconds
amount_a = get_seconds(1,2,0)
amount_b = get_seconds(1,2,3)
result = amount_a + amount_b
print(result)

# FloorDivision: Divide a number and takes the integer part of the division as a result.

def convert_seconds(seconds):
    #Definimos 3 variables
    hours = seconds // 3600 #Calculamos cuantas hs hay en x cantidad de segundos
    minutes = (seconds - hours*3600) // 60 #Calcula cuantos minutos quedan cuando restamos x horas 
    remaining_seconds = seconds - hours*3600 - minutes*60 #Calcula cuantos segundos quedan cuando restamos minutos.
    return hours, minutes, remaining_seconds #La funcion devuelve 3 valores.

hours, minutes, seconds = convert_seconds(16000)
print(hours, minutes, seconds)



