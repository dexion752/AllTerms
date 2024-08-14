import markdown
from django import template
from django.utils.safestring import mark_safe
from re import IGNORECASE, compile, escape as rescape

register = template.Library()

@register.filter
def sub(value, arg):
    return value - arg


# 하이라이팅을 위한 필터
# to-do: 코드가 완성되면 common, southterms앱의 템플릿태그 폴더로 옮길 것.
@register.filter(name='highlight')
def highlight(text, search):
    rgx = compile(rescape(search), IGNORECASE)
    return mark_safe(
        rgx.sub(
            lambda m: '<b class="text text-danger">{}</b>'.format(m.group()),
            text
        )
    )


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