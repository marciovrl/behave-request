from faker import Faker


class Data:
    def create_post(self):
        return {'titlle': Faker().word(ext_word_list=None),
                'body': Faker().text(max_nb_chars=200, ext_word_list=None)}
