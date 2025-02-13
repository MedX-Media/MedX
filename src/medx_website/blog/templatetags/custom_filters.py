from django import template  # Importing Django's template module
import jdatetime  # Importing the jdatetime library for working with Jalali dates

register = template.Library()  # Creating a template library to register custom filters

# Custom template filter to convert English digits to Persian digits
@register.filter(name='persian_numbers')  # Registering the filter with a name
def persian_numbers(value):
    persian_digits = "۰۱۲۳۴۵۶۷۸۹"  # Persian digit characters
    english_digits = "0123456789"  # English digit characters
    translation_table = str.maketrans(english_digits, persian_digits)  # Creating a translation table
    return str(value).translate(translation_table)  # Translating the input value to Persian digits
    
# Custom template filter to convert Gregorian dates to Jalali dates
@register.filter(name='to_jalali')  # Registering the filter with a name
def to_jalali(date):
    if date:  # Checking if the date is not None
        jalali_date = jdatetime.date.fromgregorian(date=date)  # Converting the Gregorian date to Jalali
        jdate = jalali_date.strftime('%d %B %Y').split(' ')  # Formatting the Jalali date

        # Mapping Gregorian month names to Persian month names
        month_names = {
            "Farvardin": "فروردین",
            "Ordibehesht": "اردیبهشت",
            "Khordad": "خرداد",
            "Tir": "تیر",
            "Mordad": "مرداد",
            "Shahrivar": "شهریور",
            "Mehr": "مهر",
            "Aban": "آبان",
            "Azar": "آذر",
            "Dey": "دی",
            "Bahman": "بهمن",
            "Esfand": "اسفند",
        }

        # Replacing the month name in the formatted date with its Persian equivalent
        if jdate[1] in month_names:
            jdate[1] = month_names[jdate[1]]
        
        return ' '.join(jdate)  # Joining the day, month, and year to return the formatted Jalali date
    return ''  # Returning an empty string if the date is None