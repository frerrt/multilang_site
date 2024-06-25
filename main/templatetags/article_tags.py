from django import template


register = template.Library()


@register.filter

def get_translated_value(article, field_name, language_code):

    if language_code == 'en':

        return getattr(article, f'{field_name}_en')

    elif language_code == 'fr':

        return getattr(article, f'{field_name}_fr')

    else:

        return getattr(article, field_name)