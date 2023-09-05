from django import template

register = template.Library()  #register the template
#custom filter
def  cut(value,arg):
    """ 
        this cuts all value of  arg from the string
    """
    return value.replace(arg,"")


register.filter('cut',cut)