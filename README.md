# Mi Proyecto Python de Manipulación de Fechas

Este proyecto contiene una colección de funciones útiles para manipular y convertir fechas. Las funciones cubren una variedad de tareas comunes, desde la obtención de la fecha de hoy hasta el cálculo de la fecha hace un año.

## Funciones Incluidas

A continuación se presenta una descripción detallada de cada función en este paquete.

- `hoy()`: Esta función retorna la fecha de hoy en un formato proporcionado.
- `day_after()`: Esta función retorna la fecha que se obtiene al agregar un día a la fecha proporcionada.
- `year_ago()`: Esta función retorna la fecha que se obtiene al restar un año a la fecha proporcionada.
- `month_after()`: Esta función retorna la fecha que se obtiene al agregar un mes a la fecha proporcionada.
- `month_before()`: Esta función retorna la fecha que se obtiene al restar un mes a la fecha proporcionada.
- `date_mini()`: Esta función retorna la fecha proporcionada en formato "Año-Mes".
- `mes_by_ordinal()`: Esta función retorna el nombre del mes correspondiente al número ordinal proporcionado.
- `mes_anio_by_abreviacion()`: Esta función convierte una abreviatura de mes-año a una forma más legible.
- `anio_mes()`: Esta función toma una fecha y devuelve el año seguido del nombre del mes.
- `ultimo_dia_del_mes()`: Esta función toma una fecha y devuelve la fecha correspondiente al último día del mes de la fecha proporcionada.
- `es_bisiesto()`: Esta función verifica si un año es bisiesto.
- `invertir_orden()`: Esta función toma una lista de tuplas y devuelve una lista de tuplas con los elementos en orden invertido.
- `r0und()`: Esta función redondea un número con una precisión dada.

## Cómo Usar

Este es un módulo de Python y puede ser importado en su proyecto de Python con la instrucción `import`. Después de importarlo, puede llamar a cualquier función con `nombre_del_módulo.nombre_de_la_función`. 

Por ejemplo:

```python
import funcionesjo

hoy = funcionesjo.hoy()
print(hoy)
