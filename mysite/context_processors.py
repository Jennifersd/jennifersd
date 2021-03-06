from django.conf import settings

def site(request):

    SITE_PROTOCOL_RELATIVE_URL = '//' + settings.SITE_URL

    SITE_PROTOCOL = 'http'
    if request.is_secure():
        SITE_PROTOCOL = 'https'

    SITE_PROTOCOL_URL = SITE_PROTOCOL + '://' + settings.SITE_URL

    return {
        'SITE_URL': settings.SITE_URL,
        'SITE_PROTOCOL': SITE_PROTOCOL,
        'SITE_PROTOCOL_URL': SITE_PROTOCOL_URL,
        'SITE_PROTOCOL_RELATIVE_URL': SITE_PROTOCOL_RELATIVE_URL
    }