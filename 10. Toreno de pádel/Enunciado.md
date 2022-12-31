# Torneo de pádel

Poco después de que terminara la obra de construcción de mi urbanización y nos dieran las llaves a los flamantes nuevos propietarios, aquello se llenó de camiones de mudanza de contentos vecinos deseosos de estrenar su nueva casa. En general reinaba un ambiente de felicidad propicio para que muchos de esos desconocidos entablaran una rápida amistad.

Con ese caldo de cultivo pronto hubo quien propuso organizar un torneo de pádel en la, aún por estrenar, pista comunitaria. Dicho y hecho, ese entusiasta grupo de vecinos organizó el que llamaron Primer Torneo de Pádel "Lo importante es la gente" y, ni cortos ni perezosos, nos apuntaron a todos los demás sin preguntar.

El torneo fue en modo campeonato. Aprovechando que el número de viviendas es una potencia de dos, lo organizaron con distintas eliminatorias a un único partido. Si ganabas el partido pasabas a la siguiente ronda y si perdías quedabas descalificado.

No es de extrañar, claro, que muchos de nosotros no fuéramos a los partidos. Afortunadamente la normativa estaba preparada para eso. Si a un partido faltaba uno de los jugadores, el otro ganaba automáticamente sin jugar. Si faltaban los dos, no se jugaba tampoco el partido de la siguiente ronda, clasificándose automáticamente el otro jugador (si lo había).

A la vista de la intención de cada vecino de participar o no en el torneo, ¿cuántos partidos se jugaron en las primeras rondas?

## Entrada

La entrada está compuesta de distintos casos de prueba, cada uno en dos líneas.

La primera línea de cada caso de prueba indica el número de jugadores (siempre una potencia de dos entre 2 y 218) seguido del número de rondas sobre las que se quiere conocer los partidos jugados.

A continuación aparece una línea con tantos números como jugadores. Un 1 indica que ese jugador se presentará a todos sus partidos, mientras que un 0 indica que el vecino no tiene intención de jugar. El orden de los jugadores está dado de forma que en la primera ronda se enfrentan el primer jugador contra el segundo, el tercero contra el cuarto y así sucesivamente. Además están colocados de forma que en la final se enfrentan el ganador de la primera mitad de jugadores con el ganador de la segunda mitad y este esquema se repite para conocer los ganadores de ambas mitades.

La entrada termina con una línea con dos ceros que no debe procesarse.

### Ejemplo

```
4 2
1111
4 1
1111
4 2
0110
8 2
10101010
0 0
```

## Salida

Por cada caso de prueba se escribirá una única línea con el número de partidos jugados en las rondas indicadas.

### Ejemplo

```
3
2
1
2
```