import markdown
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def sub(value, arg):
    return value - arg

@register.filter
def mark(value):
    extensions = [
        'abbr',
        'extra',
        'attr_list',
        'def_list',
        'nl2br',
        'legacy_attrs',
        'legacy_em',
        'meta',
        'sane_lists',
        'smarty',
        'wikilinks',
        'fenced_code',
        'footnotes',
        'tables',
        'codehilite',
        'tables',
        'toc',
        'admonition',
    ]
    return mark_safe(markdown.markdown(value, extensions=extensions))