from django import template
import jdatetime

register = template.Library()

@register.filter(name='persian_numbers')
def persian_numbers(value):
    persian_digits = "۰۱۲۳۴۵۶۷۸۹"
    english_digits = "0123456789"
    translation_table = str.maketrans(english_digits, persian_digits)
    return str(value).translate(translation_table)


@register.filter(name='to_jalali')
def to_jalali(date):
    if date:
        jalali_date = jdatetime.date.fromgregorian(date=date)
        jdate = jalali_date.strftime('%d %B %Y').split(' ')
        
        month_names = {
            'Farvardin': 'فروردین',
            'Ordibehesht': 'اردیبهشت',
            'Khordad': 'خرداد',
            'Tir': 'تیر',
            'Mordad': 'مرداد',
            'Shahrivar': 'شهریور',
            'Mehr': 'مهر',
            'Aban': 'آبان',
            'Azar': 'آذر',
            'Dey': 'دی',
            'Bahman': 'بهمن',
            'Esfand': 'اسفند'
        }

        if jdate[1] in month_names:
            jdate[1] = month_names[jdate[1]]
        
        return ' '.join(jdate)
    return ''