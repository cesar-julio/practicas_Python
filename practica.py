"""
 * Enunciado: Dado un array de números enteros positivos, donde cada uno
 * representa unidades de bloques apilados, debemos calcular cuantas unidades
 * de agua quedarán atrapadas entre ellos.
 *
 * - Ejemplo: Dado el array [4, 0, 3, 6, 1, 3].
 *
 *         ⏹
 *         ⏹
 *   ⏹💧💧⏹
 *   ⏹💧⏹⏹💧⏹
 *   ⏹💧⏹⏹💧⏹
 *   ⏹💧⏹⏹⏹⏹
 *
 *   Representando bloque con ⏹︎ y agua con 💧, quedarán atrapadas 7 unidades
 *   de agua. Suponemos que existe un suelo impermeable en la parte inferior
 *   que retiene el agua.
 """
array_list = [4, 0, 3, 6, 1, 3]
def water_container(array):
    num_max = max(array)
    for elm in range(0,num_max):
        num_line = num_max - elm
        text_line = ""
        for num in array:
            if num_line - num > 0:
                text_line += "*"
            else:
                text_line += "O"
                
        print(text_line)

water_container(array_list)
    
