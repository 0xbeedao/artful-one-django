from django import template

register = template.Library()


@register.inclusion_tag("includes/carousel.html")
def carousel(photoset):
    return {"photoset": photoset}
