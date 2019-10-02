from faker import Faker


class FakePosts:

    def __init__(self):
        self.titlle = Faker().word(ext_word_list=None)
        self.body = Faker().text(max_nb_chars=200, ext_word_list=None)
