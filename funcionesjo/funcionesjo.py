import locale
import calendar
from typing import List, Tuple
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

def hoy(formato="%Y-%m-%d", inicio_de_mes=False) -> str:
    """
    Esta función retorna la fecha de hoy en el formato proporcionado.

    Parámetros:
    formato: str - Formato en el que se desea obtener la fecha. (Por defecto es "%Y-%m-%d").
    inicio_de_mes: bool - Si es True, el día será el primer día del mes (Por defecto es False).

    Retorna:
    str - La fecha de hoy en el formato proporcionado.

    Excepciones:
    ValueError - Si el formato proporcionado no es válido.
    """
    if not isinstance(formato, str):
        raise ValueError("El formato debe ser una cadena de texto.")

    if inicio_de_mes and "%d" in formato:
        formato = formato.replace("%d", "01")
    return datetime.today().strftime(formato)

def day_after(fecha: str, formato='%Y-%m-%d') -> str:
    """
    Esta función retorna la fecha que se obtiene al agregar un día a la fecha proporcionada.

    Parámetros:
    fecha: str - Fecha a la que se desea agregar un día.
    formato: str - Formato en el que se proporciona la fecha. (Por defecto es '%Y-%m-%d')

    Retorna:
    str - La fecha que se obtiene al agregar un día a la fecha proporcionada en el formato original.

    Excepciones:
    ValueError - Si la fecha o el formato proporcionado no es válido.
    """
    try:
        fecha_datetime = datetime.strptime(fecha, formato)
        fecha_mas_un_dia = fecha_datetime + timedelta(days=1)
        fecha_texto = fecha_mas_un_dia.strftime(formato)
        return fecha_texto
    except ValueError:
        raise ValueError("La fecha o el formato proporcionado no es válido.")

from dateutil.relativedelta import relativedelta

def year_ago(fecha: str, formato='%Y-%m-%d', inicio_de_mes=False, inicio_de_anio=False) -> str:
    """
    Esta función retorna la fecha que se obtiene al restar un año a la fecha proporcionada.

    Parámetros:
    fecha: str - Fecha a la que se desea restar un año.
    formato: str - Formato en el que se proporciona la fecha. (Por defecto es '%Y-%m-%d')
    inicio_de_mes: bool - Si es True, el día será el primer día del mes. (Por defecto es False)
    inicio_de_anio: bool - Si es True, el mes y el día serán el primer mes y día del año. (Por defecto es False)

    Retorna:
    str - La fecha que se obtiene al restar un año a la fecha proporcionada en el formato original.

    Excepciones:
    ValueError - Si la fecha o el formato proporcionado no es válido.
    """
    try:
        fecha_datetime = datetime.strptime(fecha, formato)
        fecha_un_ano_antes = fecha_datetime - relativedelta(years=1)
        if inicio_de_mes:
            fecha_un_ano_antes = fecha_un_ano_antes.replace(day=1)
        if inicio_de_anio:
            fecha_un_ano_antes = fecha_un_ano_antes.replace(month=1, day=1)
        fecha_texto = fecha_un_ano_antes.strftime(formato)
        return fecha_texto
    except ValueError:
        raise ValueError("La fecha o el formato proporcionado no es válido.")

def month_after(fecha: str, formato='%Y-%m-%d') -> str:
    """
    Esta función retorna la fecha que se obtiene al agregar un mes a la fecha proporcionada.

    Parámetros:
    fecha: str - Fecha a la que se desea agregar un mes.
    formato: str - Formato en el que se proporciona la fecha. (Por defecto es '%Y-%m-%d')

    Retorna:
    str - La fecha que se obtiene al agregar un mes a la fecha proporcionada en el formato original.

    Excepciones:
    ValueError - Si la fecha o el formato proporcionado no es válido.
    """
    try:
        fecha_datetime = datetime.strptime(fecha, formato)
        fecha_un_mes_despues = fecha_datetime + relativedelta(months=1)
        fecha_texto = fecha_un_mes_despues.strftime(formato)
        return fecha_texto
    except ValueError:
        raise ValueError("La fecha o el formato proporcionado no es válido.")

def month_before(fecha: str, formato='%Y-%m-%d') -> str:
    """
    Esta función retorna la fecha que se obtiene al restar un mes a la fecha proporcionada.

    Parámetros:
    fecha: str - Fecha a la que se desea restar un mes.
    formato: str - Formato en el que se proporciona la fecha. (Por defecto es '%Y-%m-%d')

    Retorna:
    str - La fecha que se obtiene al restar un mes a la fecha proporcionada en el formato original.

    Excepciones:
    ValueError - Si la fecha o el formato proporcionado no es válido.
    """
    try:
        fecha_datetime = datetime.strptime(fecha, formato)
        fecha_un_mes_antes = fecha_datetime - relativedelta(months=1)
        fecha_texto = fecha_un_mes_antes.strftime(formato)
        return fecha_texto
    except ValueError:
        raise ValueError("La fecha o el formato proporcionado no es válido.")

def date_mini(fecha: str, formato='%Y-%m-%d') -> str:
    """
    Esta función retorna la fecha proporcionada en formato "Año-Mes".

    Parámetros:
    fecha: str - Fecha que se desea convertir.
    formato: str - Formato en el que se proporciona la fecha. (Por defecto es '%Y-%m-%d')

    Retorna:
    str - La fecha proporcionada en formato "Año-Mes".

    Excepciones:
    ValueError - Si la fecha o el formato proporcionado no es válido.
    """
    try:
        fecha_datetime = datetime.strptime(fecha, formato)
        fecha_mini = fecha_datetime.strftime('%Y-%m')
        return fecha_mini
    except ValueError:
        raise ValueError("La fecha o el formato proporcionado no es válido.")

def mes_by_ordinal(ordinal: str | int, abreviado = True, mes_anterior = False) -> str:
    """
    Esta función retorna el nombre del mes correspondiente al número ordinal proporcionado.

    Parámetros:
    ordinal: str - Número ordinal del mes.
    abreviado: bool - Si se debe retornar el nombre del mes abreviado. (Por defecto es True)
    mes_anterior: bool - Si se debe retornar el nombre del mes anterior al proporcionado. (Por defecto es False)

    Retorna:
    str - El nombre del mes correspondiente al número ordinal proporcionado.

    Excepciones:
    ValueError - Si el número ordinal está fuera de rango.
    """
    try:
        ordinal = int(ordinal)
        if mes_anterior:
            ordinal -= 1
        if not 1 <= ordinal <= 12:
            raise ValueError("El número ordinal está fuera de rango.")
        nombres_meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
        nombre_mes = nombres_meses[ordinal - 1]
        if abreviado:
            nombre_mes = nombre_mes[0:3]
        return nombre_mes
    except:
        raise ValueError("La entrada no es válida.")

def mes_anio_by_abreviacion(abreviacion: str, mayuscula: bool=False, mmaa: bool=False) -> str:
    """
    Esta función convierte una abreviatura de mes-año a una forma más legible.

    Parámetros:
    abreviacion: str - Abreviatura de mes-año.
    capON: bool - Si la salida debe tener la primera letra en mayúsculas. (Por defecto es False)
    mmaa: bool - Si la abreviatura es en formato mes-año. (Por defecto es False)

    Retorna:
    str - La abreviatura de mes-año en una forma más legible.

    Excepciones:
    ValueError - Si la abreviatura no es válida.
    """
    ABREVIATURAS = {
        "Ene":"enero",
        "Feb":"febrero",
        "Mar":"marzo",
        "Abr":"abril",
        "May":"mayo",
        "Jun":"junio",
        "Jul":"julio",
        "Ago":"agosto",
        "Sep":"septiembre",
        "Oct":"octubre",
        "Nov":"noviembre",
        "Dic":"diciembre"}
    try:
        anio, mes = abreviacion.split("-")
        if mmaa:
            mes, anio = anio, mes
        mes = ABREVIATURAS[mes]
        if mayuscula:
            mes = mes.capitalize()
        return f"{mes} {anio}"
    except KeyError:
        raise ValueError("La abreviatura no es válida.")

def anio_mes(fecha: str, formato='%Y-%m-%d') -> str:
    """
    Esta función toma una fecha y devuelve el año seguido del nombre del mes.

    Parámetros:
    fecha: str - La fecha en formato de cadena de texto.
    formato: str - El formato de la fecha en formato de cadena de texto. (Por defecto es '%Y-%m-%d')

    Retorna:
    str - El año seguido del nombre del mes.

    Excepciones:
    ValueError - Si la fecha no cumple con el formato.
    """
    try:
        # Guardar la configuración de idioma actual
        old_locale = locale.getlocale(locale.LC_TIME)
        
        # Cambiar la configuración de idioma a español
        locale.setlocale(locale.LC_TIME, ("es_ES", "UTF-8"))
        
        fecha_datetime = datetime.strptime(fecha, formato)
        
        # Formatear la fecha y capitalizar el nombre del mes
        resultado = fecha_datetime.strftime('%Y-%b')
        
        # Restaurar la configuración de idioma original
        locale.setlocale(locale.LC_TIME, old_locale)

        # Convierte el nombre del mes a la forma correcta (la primera letra en mayúsculas, el resto en minúsculas)
        anio, mes = resultado.split('-')
        mes = mes.capitalize()
        mes = mes.replace('.', '')
        
        return f"{anio}-{mes}"
    except ValueError:
        raise ValueError("La fecha no cumple con el formato.")

def ultimo_dia_del_mes(fecha:str, formato='%Y-%m-%d') -> str:
    """
    Esta función toma una fecha y devuelve la fecha correspondiente al último día del mes de la fecha proporcionada.

    Parámetros:
    fecha: str - La fecha en formato de cadena de texto.
    formato: str - El formato de la fecha en formato de cadena de texto. (Por defecto es '%Y-%m-%d')

    Retorna:
    str - La fecha correspondiente al último día del mes de la fecha proporcionada.

    Excepciones:
    ValueError - Si la fecha no cumple con el formato.
    """
    try:
        fecha_datetime = datetime.strptime(fecha, formato)
        ultimo_dia = calendar.monthrange(fecha_datetime.year, fecha_datetime.month)[1]
        fecha_datetime = fecha_datetime.replace(day=ultimo_dia)
        return fecha_datetime.strftime(formato)
    except ValueError:
        raise ValueError("La fecha no cumple con el formato.")

def es_bisiesto(anio: int) -> bool:
    """
    Esta función verifica si un año es bisiesto.

    Parámetros:
    anio: int - El año a verificar.

    Retorna:
    bool - Verdadero si el año es bisiesto, falso de lo contrario.
    """
    return anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)

from typing import List, Tuple

def invertir_orden(data: List[Tuple], Qfecha: bool = True) -> List[Tuple]:
    """
    Esta función toma una lista de tuplas y devuelve una lista de tuplas con los elementos en orden invertido.
    Si el primer elemento de la tupla es una fecha, también se invierte el orden de la fecha.

    Parámetros:
    data: List[Tuple] - La lista de tuplas a invertir.
    Qfecha: bool - Indicador si el primer elemento de la tupla es una fecha.

    Retorna:
    List[Tuple] - La lista de tuplas con el orden invertido.

    Excepciones:
    ValueError - Si el primer elemento de la tupla no cumple con el formato de fecha.
    """
    data_salida = []
    if Qfecha:
        for dato in data:
            try:
                fecha = "-".join(dato[0].split("-")[::-1])
                data_salida.append((fecha, dato[1]))
            except:
                raise ValueError("El primer elemento de la tupla no cumple con el formato de fecha.")
    else:
        for dato in data:
            data_salida.append(dato[::-1])
    return data_salida

def r0und(numero: float, precicion: int = 2) -> float:
    """
    Esta función redondea un número con una precisión dada.

    Parámetros:
    numero: float - El número a redondear.
    precicion: int - La cantidad de dígitos decimales a redondear. (Por defecto es 2)

    Retorna:
    float - El número redondeado.

    Excepciones:
    ValueError - Si el número no es un float o la precisión no es un int.
    """
    if not isinstance(numero, float) or not isinstance(precicion, int):
        raise ValueError("El número debe ser un float y la precisión debe ser un int.")
    
    numero = round(numero, precicion)
    return 0.0 if numero == -0.0 else numero
