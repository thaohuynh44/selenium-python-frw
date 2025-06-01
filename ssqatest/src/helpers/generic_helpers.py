import random
import string
import logging as logger

def generate_random_email(domain=None, email_prefix=None):

    if not domain:
        domain = 'ssqa.com'
    if not email_prefix:
        email_prefix = 'testuser'

    rand_email_string_length = 10
    rand_string = ''.join(random.choices(string.ascii_lowercase, k=rand_email_string_length))

    email = email_prefix + '_' + rand_string + '@' + domain

    logger.info(f'Generated random email: {email}')

    return email