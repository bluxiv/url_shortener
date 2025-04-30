import secrets
import string


def generate_short_code():
    """Generates a random string of fixed length for the short code."""
    length = 8
    characters = string.ascii_letters + string.digits
    random_code = "".join(secrets.choice(characters) for _ in range(length))

    return random_code

def get_client_ip(request):
    """Gets the real client IP address from a request."""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        # 'HTTP_X_FORWARDED_FOR' can be a comma-separated list of IPs.
        # The first one is usually the original client IP.
        ip = x_forwarded_for.split(',')[0]
    else:
        # Fallback to REMOTE_ADDR if X-Forwarded-For is not set.
        ip = request.META.get('REMOTE_ADDR')
    return ip
