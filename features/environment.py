from features.helpers.settings import create_environment


def before_all(context):
    print('Starting Testing')
    create_environment()


def after_all(context):
    print('Finish Testing')
