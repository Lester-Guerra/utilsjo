# utilsjo

[![License Badge](https://img.shields.io/github/license/1u1s4/utilsjo)](https://github.com/1u1s4/utilsjo/blob/main/LICENSE)
[![Issues Badge](https://img.shields.io/github/issues/1u1s4/utilsjo)](https://github.com/1u1s4/utilsjo/issues)
[![Pull Requests Badge](https://img.shields.io/github/issues-pr/1u1s4/utilsjo)](https://github.com/1u1s4/utilsjo/pulls)
[![Contributors Badge](https://img.shields.io/github/contributors/1u1s4/utilsjo)](https://github.com/1u1s4/utilsjo/graphs/contributors)
[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/dwyl/esta/issues)

**utilsjo** is a Python package that provides a collection of functions for date manipulation and other useful operations. It offers various functionalities to simplify working with dates, such as getting the current date, calculating the next day, finding the last day of the month, and more.

## Installation

To install **utilsjo**, you can use the following command:

```shell
pip install utilsjo
```

## Dependencies

The codebase has a dependency on the `python-dateutil` package. Make sure to install it before using **utilsjo**.

## Functionalities

The main functionalities provided by **utilsjo** include:

- `hoy()`: Returns the current date in the format "YYYY-MM-DD" by default, or in a custom format specified by the user.
- `day_after(date)`: Calculates the day after the given date.
- `year_ago(date)`: Calculates the date one year ago from the given date.
- `month_after(date)`: Calculates the date one month after the given date.
- `month_before(date)`: Calculates the date one month before the given date.
- `date_mini(date)`: Returns the date in the format "YYYY-MM-DD" without the time component.
- `mes_by_ordinal(ordinal)`: Returns the month name corresponding to the given ordinal number.
- `mes_anio_by_abreviacion(abreviacion)`: Returns the month name and year corresponding to the given abbreviation.
- `anio_mes(date)`: Returns the year and month in the format "YYYY-MM" from the given date.
- `ultimo_dia_del_mes(date)`: Finds the last day of the month for the given date.
- `es_bisiesto(year)`: Checks if the given year is a leap year.
- `invertir_orden(dates)`: Inverts the order of dates in a list of tuples.
- `r0und(number, decimals=2)`: Rounds the given number to the specified number of decimal places.

## Usage

Here are some examples of how to use the functions provided by **utilsjo**:

```python
from utilsjo import hoy, day_after, ultimo_dia_del_mes, es_bisiesto

# Get the current date
current_date = hoy()
print(current_date)  # Output: "2022-12-31"

# Calculate the day after a given date
next_day = day_after('2022-12-31')
print(next_day)  # Output: "2023-01-01"

# Find the last day of the month
last_day = ultimo_dia_del_mes('2023-02-01')
print(last_day)  # Output: "2023-02-28"

# Check if a year is a leap year
leap_year = es_bisiesto(2024)
print(leap_year)  # Output: True
```

## Authors

**utilsjo** is authored by Luis Alfredo Alvarado Rodríguez. You can contact the author via email at laalvarado@ine.gob.gt.

## Contributing

Contributions to **utilsjo** are welcome! If you encounter any issues or have suggestions for improvements, please open an issue on the [GitHub repository](https://github.com/1u1s4/utilsjo/issues).

## Support

If you need support or have any questions, feel free to reach out to the author at laalvarado@ine.gob.gt.

## Donation

If you would like to make a donation to support the development of **utilsjo**, please contact the author at laalvarado@ine.gob.gt.

