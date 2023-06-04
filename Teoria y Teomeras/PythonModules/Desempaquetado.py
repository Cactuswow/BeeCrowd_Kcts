numeros = (1, 2, 3 , 4);
Dato1, Dato2, Dato3, Dato4 = numeros;
print(f"{Dato1} {Dato2} {Dato3} {Dato4}");

""" Guardamos el sobrante en un arreglo """

Valor1, Valor2,  *ValorResto = numeros;
print(f"{Valor1} {Valor2} {ValorResto}")

""" Con un *_ No guardamos el resto """
#Con _ Nos saltamos posiciones

