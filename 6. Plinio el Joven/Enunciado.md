# Plinio el Joven

Plinio el Joven fue un abogado, escritor y científico de la antigua Roma. Ilustre orador seguidor de Cicerón, su primera obra, una tragedia en griego, la escribió con solo 14 años. Aunque la mayoría de sus escritos se han perdido, destacó en poesía y es considerado por algunos críticos el inventor del género literario de la carta escrita para ser publicada.

Una de sus cartas más famosas es la que dirigió a Tácito, historiador romano, describiendo la erupción del monte Vesubio en la que murió su tío, Plinio el Viejo. Debido a ella, las erupciones de ese tipo se conocen hoy como plinias.

Plinio el Joven fue joven toda su vida porque, según cuenta la leyenda1, nació un 29 de febrero, por lo que solo cumplía años una vez de cada cuatro.

Dada una fecha, ¿podrías decirnos el siguiente cumpleaños de Plinio?

## Entrada

El programa deberá leer, de la entrada estándar, un primer número indicando cuántos casos de prueba deberán procesarse.

Cada caso de prueba está compuesto por una fecha en formato `DD/MM/AAAA`, indicando el día, mes y año de la fecha a consultar, que será siempre correcta. El año estará entre 60 y 1581.

### Ejemplo

```
3
04/12/0061
29/02/1500
01/01/0444
```

## Salida

Por cada caso de prueba el programa escribirá, en el mismo formato, la fecha del siguiente cumpleaños de Plinio el Joven, es decir el siguiente 29 de febrero. Los años consultados son anteriores a la reforma Gregoriana ideada por Clavius e impulsada por el papa Gregorio XIII, por lo que se consideran bisiestos todos los años divisibles por 4.

Si la fecha de entrada es el cumpleaños de Plinio, se indicará el siguiente.

### Ejemplo

```
29/02/0064
29/02/1504
29/02/0444
```