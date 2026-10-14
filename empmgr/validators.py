# validators.py

def parse_salary(text):

    try:
        return float(text)

    except ValueError:
        return None
    
    if salary < 0:
        return None
    return salary

# Validate email
def is_valid_email(input_email: str) -> bool:
    """Return True if input_email has one @, a dot in the domain, and only allowed characters."""
    allowed_characters = list("abcdefghijklmnopqrstuvwxyz1234567890-_.")
    found_at_sign = False
    count_at_sign = 0
    count_dot_in_domain = 0
    username_half = ""
    domain_half = ""

    # Iterate input email string
    for character in input_email:
        # Flag @ symbol
        if character == "@":
            count_at_sign += 1
            found_at_sign = True
            continue

        # Separate username and domain
        if not found_at_sign:
            username_half += character
        else:
            domain_half += character

    # Check total @ sign
    if count_at_sign != 1:
        return False

    # Check empty username and domain
    if username_half == "" or domain_half == "":
        return False

    for character in username_half:
        # Check for illegal characters including space in username half
        if character.lower() not in allowed_characters:
            return False

    for character in domain_half:
        # Check for illegal characters including space in domain half
        if character.lower() not in allowed_characters:
            return False

        # Count total "." in domain
        if character == ".":
            count_dot_in_domain += 1

    # Domain must start and end with a letter or digit (rejects "a@.com" and "a@b.")
    if not domain_half[0].isalnum() or not domain_half[-1].isalnum():
        return False

    if count_dot_in_domain < 1:
        return False

    return True