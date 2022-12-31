# Ascensor con nivel

Kevin acaba de empezar a trabajar en la multinacional PorNiveles, cuyas oficinas se encuentran en uno de los rascacielos más altos de la ciudad. Por supuesto, Kevin ha comenzado como simple becario y su puesto de trabajo se encuentra en un despacho compartido en la primera planta. Su jefe directo tampoco es muy importante y su oficina se encuentra en la segunda planta. Normalmente Kevin solo se mueve entre esas dos plantas, cuyas ventanas tienen unas vistas nada llamativas. A él le gustaría subir al último piso desde donde le han dicho que se puede ver toda la ciudad y más allá.

Pero la empresa está fuertemente jerarquizada y todos los empleados se distribuyen entre una serie de niveles que influyen en todos los aspectos, desde el sueldo a determinados privilegios, como el piso del rascacielos hasta el que uno puede subir.

El enorme y altísimo edificio tiene un intrincado sistema de ascensores. No todos van desde la planta baja a la azotea, sino que cada ascensor se mueve entre dos plantas concretas, A y B, permitiendo viajes entre cualesquiera plantas entre esas dos. Pero si uno quiere subir por encima de B o bajar por debajo de A tendría que cambiar de ascensor. Además el acceso a los ascensores está restringido. Cada ascensor también tiene asignado un nivel y solamente los empleados con ese nivel o superior pueden utilizarlo.

Kevin ha comprobado ya que con su nivel de becario no puede subir muy alto y se pregunta qué nivel es el que hace falta para alcanzar la última planta.

## Entrada

La entrada está formada por diferentes casos de prueba. La primera línea de cada caso contiene el número N de ascensores en el edificio (1 ≤ N ≤ 100.000). A continuación aparecen N líneas, cada una describiendo un ascensor con tres números, la planta más baja y la más alta que conecta el ascensor y el nivel necesario para poder utilizarlo. Las plantas están numeradas empezando por la 0 (la planta baja) y un edificio nunca tiene más de un millón de plantas. Los niveles varían entre 1 y 1.000.000. Se garantiza que siempre es posible (con el nivel apropiado) subir en ascensor desde la planta 0 a la más alta.

### Ejemplo

```
5
0 3 3
3 10 11
0 4 2
2 8 6
8 10 8
```

## Salida

Para cada caso de prueba se escribirá cuál es el nivel mínimo necesario para poder subir en ascensor desde la planta 0 hasta la última planta del edificio.

### Ejemplo

```
8
```