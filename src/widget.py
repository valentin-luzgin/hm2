def date_conversion(date: str) -> str | None:
    '''Преобразует дату формата ГГГГ-ММ-ДД в формат ДД-ММ-ГГГГ'''
    return f'{date[8:10]}.{date[5:7]}.{date[0:4]}'


