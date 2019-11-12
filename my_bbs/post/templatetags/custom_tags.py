from django import template

register = template.Library()

@register.simple_tag
def prefix_tag(cur_str):
    return 'Hello %s' % cur_str

@register.simple_tag(takes_context=True)
def prefix_tag(contex, cur_str):
    return '%s %s' % (context['prefix'], cur_str)


@register.simple_tag(takes_context=True, name='prefix')
def prefix_tag(contex, cur_str):
    return '%s %s' % (context['prefix'], cur_str)


@register.inclusion_tag('post/inclusion.html', takes_context=True)
def hello_inclusion_tag(context, cur_str):
    return {'hello': '%s %s' % (context['prefix'], cur_str)}


@register.simple_tag
def hello_assignment_tag(cur_str):
    return 'Hello: %s' % cur_str


@register.filter
def replace_django(value):
    return value.replace('django', 'Django')

@register.filter(name='r_django')
def replace_django(value, base):
    return value.replace('django', base)
