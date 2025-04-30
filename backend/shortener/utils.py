from shortener.models import Link
import secrets
import string

def generate_short_code():
    """Generates a random string of fixed length for the short code."""
    length = 8
    characters = string.ascii_letters + string.digits
    random_code = "".join(secrets.choice(characters) for _ in range(length))

    # Ensure the generated code doesn't already exist
    while Link.objects.filter(short_code=random_code).exists():
        random_code = "".join(secrets.choice(characters) for _ in range(length))
    return random_code