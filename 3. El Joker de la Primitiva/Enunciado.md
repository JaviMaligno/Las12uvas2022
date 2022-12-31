# El Jóker de la Primitiva

La Lotería Primitiva celebró su primer sorteo el 10 de diciembre de 1763, como un medio del Estado para recaudar dinero sin crear un nuevo impuesto. Originalmente denominada, simplemente, Lotería por números, se renombró a Lotería primitiva cuando se introdujo, en 1812, la que se llamó Lotería moderna que fue el germen de la que hoy se conoce como Lotería Nacional de España.

La celebración de la Lotería Primitiva se interrumpió en 1862, y volvió a recuperarse, más de un siglo después, en 1985, celebrándose desde entonces. En 2012 se introdujo la posibilidad de jugar, con el mismo boleto, a un sorteo asociado y opcional llamado JOKER.

En este sorteo secundario cada participante recibe un número aleatorio de 7 cifras asignado por la administración. Durante el sorteo, de un bombo que contiene bolas numeradas con los dígitos del 0 al 9 se extraen 7 números, reincorporando al bombo la bola elegida tras cada extracción. La persona ganadora es aquella cuyo número de 7 cifras coincida con la combinación formada por los números extraídos del bombo en el mismo orden.

Las malas lenguas dicen que, durante los primeros borradores de la especificación del sorteo, los creadores olvidaron especificar la coletilla "en el mismo orden". Afortunadamente alguien se dio cuenta a tiempo y evitó que el sorteo fuera deficitario para las arcas del Estado.

## Entrada

La entrada recibida por el programa comienza con un número indicando cuántos casos de prueba deberán ser procesados.

Cada caso está compuesto por dos números de 7 dígitos indicando, respectivamente, los dígitos extraídos en el sorteo del JOKER y los del número de un boleto concreto.

### Ejemplo

```
4
1234567 7654321
0011223 0112233
1234567 1234567
0123450 0012345
```

## Salida

Por cada caso de prueba se escribirá `GANA` si el boleto resulta ganador con la definición errónea del sorteo, en la que se habría faltado la coletilla de "en el mismo orden". En otro caso se escribirá `PIERDE`.

### Ejemplo

```
GANA
PIERDE
GANA
GANA
``` 