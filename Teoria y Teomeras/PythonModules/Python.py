print("Datos Compuestos");
print("");

Lista = ["Elemento 1", "Elemento 2", "Elemento 3"];
#Modificable
Tupla = ("Elemento 1", "Elemento 2", "Elemento 3");
#No modificable. Se puede redifinir
Conjunto = {"Elemento 1", "Elemento 2", "Elemento 3"};
#No modificable. Se puede redifinir. No accede por indice
Diccionario = {
    'Elemento 1': "Papaya",
    'Elemento 2': 125,
    'Elemento 3': True
}
print(Diccionario['Elemento 1']);

print("Condicionales y operadores lógicos")
print("");

Condicion = 3;

if (Condicion == 1):
    
    print(f"Número {Condicion}");
    
elif (Condicion == 2):
    
    print(f"Núemro {Condicion}");
    
else:
    
    print(f"Número {Condicion}");

print("Fuera del condicional");

print("Metodos de Cadena y funciones de cadena")
print("");

Cadena1 = "Elemento 1";
Valor1 = 1;

(dir(Cadena1)) 
#Funcion. Muestra todos los métodos que se pueden utilizar para cierto tipo de dato

print(Cadena1.find("E"));
#Muestra la posición del caracter a buscar. Devuelve -1 si no existe
print(Cadena1.index("E"))
#Muestra la posición del caracter a buscar. Devuelve -un error si no existe

print(Cadena1.isnumeric());
print(Cadena1.isalpha());

print(Cadena1.count("e"));
#Cuenta la cantidad de caracteres repetidos de una cadena

Cadena1.startswith("H");
Cadena1.endswith("H");

Hola = "Hola";
Hola = Hola.replace("la", "stia");
print(Hola)

Comas = "Hola,Como,estás"
Espacios = Comas.replace(",", " ");
print(Espacios);

CadenaSeparada = Cadena1.split(); #Método
print(CadenaSeparada);
CadenaSeparadaCaracter = list(Cadena1); #Función
print(CadenaSeparadaCaracter);

print("Agregando elementos a la lista");

CadenaSeparadaCaracter.append("Ultimo Elemento");
CadenaSeparadaCaracter.insert(1, "Agregando en posición 1");
CadenaSeparadaCaracter.extend(["Final", "Final+1"]); #Agregando varios elementos de una lista
print(CadenaSeparadaCaracter)

print("Eliminando elementos de una lista");
CadenaSeparadaCaracter.pop(0); #Elimina porposición. con números negativos borra desde el final para adelante

CadenaSeparadaCaracter.remove("Final+1"); #Elimina el parametro. Si no encuentra, error

#CadenaSeparadaCaracter.clear(); Elimina todo xdxd
#CadenaSeparadaCaracter.sort(reverse=true) Ordena una lista de forma ascendente, primero los false, true, números. Con reverse es invertido

CadenaSeparadaCaracter.reverse() #Invierte el orden de la lista

print("")
print("Funciones con Diccionarios");

Diccionario.clear();

Diccionario = {
        "Nombre" : "Sis",
        "Wasa" : True,
        "Insanez" : 100
}
print(Diccionario.keys()); #Devuelve los indices clave
print(Diccionario.get("Nombre")); #Devuelve valor de la clave, devuleve none si nada

print(" ");

Diccionario.clear();
print(Diccionario)

Diccionario = dict(Nombre = "Sis", Wasa = True, Insanez = 100);
print(Diccionario)
Diccionario.clear();
Diccionario = dict.fromkeys(["Nombre", "Wasa", "Insanez"]);
print(Diccionario)
Diccionario.clear();
Diccionario = dict.fromkeys("12345", "Oks");
print(Diccionario)

print(" ");
print("Bucles");

Lista1 = [1 , 2 , 3];
Lista2 = ["Increible", "Waos", "Genial"];

for Numero, Genial in zip(Lista1, Lista2):
    
    print(f"Recorriendo la lista de números = {Numero}");
    print(f"Recorriendo la lista de números = {Genial}");
    
for Numero in enumerate(Lista1):
    
    print(f"Indice = {Numero[0]} Valor = {Numero[1]}");

else:
    
    print("El bucle terminó");

print("Numero sale como Tupla");

Diccionario.clear();
Diccionario = {
        "Nombre" : "Sis",
        "Wasa" : True,
        "Insanez" : 100
}

for Key in Diccionario.items():
    
    print(Key);
    
    if (Key[0] == False):
        continue; #Se salta todo lo que le sigue

Numeros = [1 ,2, 3];
DuplicarNumero = [i*2 for i in Numeros];
print(DuplicarNumero);

print(" ");
print("funciones integradas");

print(max(Numeros));
print(min(Numeros));

Numero = 12.123456789;
print(round(Numero, 2));

print(bool()); #Retorna un False si: 0, False, Arreglo vacio, none. Retorna un True si: != 0, true, arreglo
print(all([1, False])); #Lo mismo que bool pero en iterables

print(sum(Numeros));

try:
    
    print("Si este trozo de código lanza una excepción, no se ejecutará");

except:
    
    print("Si try da un error esto se ejecuta");

