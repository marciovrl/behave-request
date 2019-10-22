from features.helpers.api import API
from features.helpers.data import Data


@step(u'use endpoint "{endpoint}"')
def step_impl(context, endpoint):
    context.api = API(context.config.userdata['url'] + endpoint)


@step(u'I want to read the posts')
def step_impl(context):
    context.res = context.api.get()


@step(u'I get the code "{code}"')
def step_impl(context, code):
    assert str(context.res.status_code) == code


@step(u'add item Post')
def step_impl(context):
    context.post = Data().create_post()

    context.res = context.api.post(context.post)
