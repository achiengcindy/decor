from django.conf import settings

def decor(request):
    return {
    'site_name': settings.SITE_NAME,
    'meta_description': settings.META_DESCRIPTION,
    'request': request
    }