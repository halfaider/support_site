"""Shared helpers for bounded image downloads and request-local cookies."""
from copy import copy
from urllib.parse import urlsplit

MAX_IMAGE_BYTES = 32 * 1024 * 1024


class SSRFRejected(ValueError):
    """Retained exception name for rejected or oversized remote media."""

    def __init__(self):
        super().__init__('Remote media request denied')


def _redirect_cookies(url, headers, *sources):
    """Build a request-local cookie jar without losing cookie scope metadata."""
    from http.cookiejar import CookieJar
    from http.cookies import SimpleCookie
    from requests.cookies import create_cookie

    jar = CookieJar()
    host = urlsplit(url).hostname

    def seed(name, value):
        cookie = create_cookie(name, value, domain=host, path='/')
        cookie.domain_specified = False
        jar.set_cookie(cookie)

    for source in sources:
        source = getattr(source, 'jar', source)
        if isinstance(source, CookieJar):
            for cookie in source:
                jar.set_cookie(copy(cookie))
        elif source:
            for name, value in dict(source).items():
                seed(name, value)

    raw = next((value for key, value in headers.items() if key.lower() == 'cookie'), None)
    if raw:
        parsed = SimpleCookie()
        parsed.load(raw)
        for name, morsel in parsed.items():
            seed(name, morsel.value)

    return jar
