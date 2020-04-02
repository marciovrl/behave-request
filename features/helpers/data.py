from faker import Faker
import os


def create_post():
    ''' Returns a valid post payload '''

    return {
        'tittle': Faker().word(ext_word_list=None),
        'body': Faker().text(max_nb_chars=200, ext_word_list=None)
    }


def create_token():
    ''' Returns the value of the token that is in the environment variables '''

    return os.getenv('TOKEN', 'var token does not exist')
